import numpy as np


class HMM:
    """
    HMM model class
    Args:
        A: State transition matrix
        s: list of s
        emissions: list of observations
        B: Emmision probabilites
    """

    def __init__(self, A, s, emissions, pi, B):
        self.A = A
        self.B = B
        self.s = s
        self.emissions = emissions
        self.pi = pi
        self.N = len(s)
        self.M = len(emissions)
        self.make_states_dict()

    def make_states_dict(self):
        """
        Make dictionary mapping between s and indexes
        """
        self.states_dict = dict(zip(self.s, list(range(self.N))))
        self.emissions_dict = dict(
            zip(self.emissions, list(range(self.M))))

    def viterbi_algorithm(self, seq):
        """
        Function implementing the Viterbi algorithm
        Args:
            seq: Observation sequence (list of observations. must be in the emmissions dict)
        Returns:
            nu: Probability of the hidden state at time t given an obeservation sequence
            hidden_states_sequence: Most likely state sequence 
        """
        lenT = len(seq)
        nu = np.zeros((lenT, self.N))
        var = np.zeros((lenT, self.N), dtype=int)
        for j in range(self.N):
            nu[0, j] = self.pi[j] * self.B[j, self.emissions_dict[seq[0]]]
            var[0, j] = 0
        for i in range(1, lenT):
            for j in range(self.N):
                nmax = -1
                Tmax = -1
                for k in range(self.N):
                    nui = nu[i - 1, k] * self.A[k, j] * \
                        self.B[j, self.emissions_dict[seq[i]]]
                    if nui > nmax:
                        nmax = nui
                        Tmax = k
                nu[i, j] = nmax
                var[i, j] = Tmax
        nmax = -1
        Tmax = -1
        for j in range(self.N):
            nui = nu[lenT - 1, j]
            if nui > nmax:
                nmax = nui
                Tmax = j
        s = [Tmax]
        for i in range(lenT - 1, 0, -1):
            s.append(var[i, s[-1]])
        s.reverse()

        self.states_dict = {v: k for k, v in self.states_dict.items()}
        return [self.states_dict[i] for i in s]

        