
#PES2UG19CS468
#YOUSHA MAHAMUNI
import numpy as np


class KMeansClustering:
    """
    K-Means Clustering Model

    Args:
        n_clusters: Number of clusters(int)
    """

    def __init__(self, n_clusters, n_init=10, max_iter=1000, delta=0.001):

        self.n_cluster = n_clusters
        self.n_init = n_init
        self.max_iter = max_iter
        self.delta = delta

    def init_centroids(self, data):
        idx = np.random.choice(
            data.shape[0], size=self.n_cluster, replace=False)
        self.centroids = np.copy(data[idx, :])

    def fit(self, data):
        """
        Fit the model to the training dataset.
        Args:
            data: M x D Matrix(M data points with D attributes each)(numpy float)
        Returns:
            The object itself
        """
        if data.shape[0] < self.n_cluster:
            raise ValueError(
                'Number of clusters is grater than number of datapoints')

        best_centroids = None
        m_score = float('inf')

        for _ in range(self.n_init):
            self.init_centroids(data)

            for _ in range(self.max_iter):
                cluster_assign = self.e_step(data)
                old_centroid = np.copy(self.centroids)
                self.m_step(data, cluster_assign)

                if np.abs(old_centroid - self.centroids).sum() < self.delta:
                    break

            cur_score = self.evaluate(data)

            if cur_score < m_score:
                m_score = cur_score
                best_centroids = np.copy(self.centroids)

        self.centroids = best_centroids

        return self

    def e_step(self, data):
        """
        Expectation Step.
        Finding the cluster assignments of all the points in the data passed
        based on the current centroids
        Args:
            data: M x D Matrix (M training samples with D attributes each)(numpy float)
        Returns:
            Cluster assignment of all the samples in the training data
            (M) Vector (M number of samples in the train dataset)(numpy int)
        """
        #TODO
        arr1=[]
        cnt=0
        for i in data:
            m=1e9
            cnt=0
            c=0
            for j in self.centroids:
                x=np.linalg.norm(j-i)
                if(m>x):
                    m=x
                    c=cnt
                cnt+=1
            arr1.append(c)
        return arr1

    def m_step(self, data, cluster_assgn):
        """
        Maximization Step.
        Compute the centroids
        Args:
            data: M x D Matrix(M training samples with D attributes each)(numpy float)
            cluster_assign: Cluster Assignment
        Change self.centroids
        """
        #TODO
        dict1={}
        
        for i in range(0,self.n_cluster):
            dict1[i]=[]
        for i in range(0,len(data)):
            dict1[cluster_assgn[i]].append(data[i])
        arr2=[]
        for j in dict1:
            mean1=np.mean(dict1[j],axis=0,dtype=np.float64)
            arr2.append(mean1)
        self.centroids=(arr2)
        return self
    def evaluate(self, data, cluster_assign):
        """
        K-Means Objective
        Args:
            data: Test data (M x D) matrix (numpy float)
            cluster_assign: M vector, Cluster assignment of all the samples in `data`
        Returns:
            metric : (float.)
        """
        #TODO
        sum1=0
        dict1={}
        k=self.n_cluster
        for i in range(0,k):
            dict1[i]=[]
        for i in range(0,len(data)):
            dict1[cluster_assign[i]].append(data[i])
        for key,val in dict1.items():
            for i in val:
                y=np.linalg.norm(i-self.centroids[key])
                sum1+=(y*y)
        return sum1
