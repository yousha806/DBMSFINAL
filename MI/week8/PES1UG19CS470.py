import numpy as np


class HMM:
    """
    HMM model class
    Args:
        A: State transition matrix
        states: list of states
        emissions: list of observations
        B: Emmision probabilites
    """

    def __init__(self, A, states, emissions, pi, B):
        self.A = A
        self.B = B
        self.states = states
        self.emissions = emissions
        self.pi = pi
        self.N = len(states)
        self.M = len(emissions)
        self.make_states_dict()

    def make_states_dict(self):
        """
        Make dictionary mapping between states and indexes
        """
        self.states_dict = dict(zip(self.states, list(range(self.N))))
        self.emissions_dict = dict(
            zip(self.emissions, list(range(self.M))))

    def viterbi_algorithm(self, seq):
        """
        Function implementing the Viterbi algorithm
        Args:
            seq: Observation sequence (list of observations. must be in the emmissions dict)
        Returns:
            nu: Porbability of the hidden state at time t given an obeservation sequence
            hidden_states_sequence: Most likely state sequence 
        """
        # TODO
        Length = len(seq)
        nu = np.zeros((Length, self.N))
        t = np.zeros((Length, self.N), dtype=int)
        
        for j in range(self.N):
            nu[0, j] = self.pi[j] * self.B[j, self.emissions_dict[seq[0]]]
            t[0, j] = 0
        
        for i in range(1, Length):
            for j in range(self.N):
                n_prob_max = -1
                max_t = -1
                for k in range(self.N):
                    loc_n = nu[i - 1, k] * self.A[k, j] * \
                        self.B[j, self.emissions_dict[seq[i]]]
                    if loc_n > n_prob_max:
                        n_prob_max = loc_n
                        max_t = k
                nu[i, j] = n_prob_max
                t[i, j] = max_t
        
        n_prob_max = -1
        max_t = -1
        for j in range(self.N):
            loc_n = nu[Length - 1, j]
            if loc_n > n_prob_max:
                n_prob_max = loc_n
                max_t = j
        
        states = [max_t]
        for i in range(Length - 1, 0, -1):
            states.append(t[i, states[-1]])
        states.reverse()

        
        self.states_dict = {v: k for k, v in self.states_dict.items()}
        
        return [self.states_dict[i] for i in states]
    
        