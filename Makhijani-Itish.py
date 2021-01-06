# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 15:02:55 2020

@author: itish
"""

import numpy as np

class robo_filters:
    def __init__ (self,D=None):
        self.matrix=[[]]
        self.D=D
    '''Used clip function() to limit the value of the matrix tp lower and upper bounds'''     
    def filter1_rangechange(self,matrix1):
        matrix2=np.clip(matrix1,a_min=0.03,a_max=None)
        return (matrix2)
    
    @staticmethod
    def compute_median(matrix):
        return np.median(matrix,axis=0)
    
    def update(self,mat):
        '''Used instance to check whether passed 2D array is actually an ndarray'''
        if isinstance(mat, np.ndarray):
            print("Numpy Array")
        elif isinstance(mat, list):
            print("Input array is a list. Converting to numpy array.")
            mat=np.array(mat)
        
        '''the algorithm would still work for >2 dims, but would compute median
           along undesired axis'''
        
        assert mat.ndim == 2, f"Shape mismatch. mat:{mat}, shape: {mat.shape}"
        
        ''' Used map function() to apply compute_mediantimestamp function to
            hence returning a list, also I used map function () as it has lower
            complexity of usage than for loops'''
            
        def compute_mediantimestamp(t):
            return robo_filters.compute_median(mat[max(0,t-self.D):t+1,])
        ans_list=np.array(list(map(compute_mediantimestamp, range(len(mat)))))
        return (ans_list)
            
''' To generate random scans of desired size for testing purposes otherwise the
    given input is mentioned below '''   
my_scans=np.random.uniform(low=0.0, high=100.0, size=(8,5))
'''my_scans=[[0., 1., 2., 1., 3.], [1., 5., 7., 1., 3.], [2., 3., 4., 1., 0.], [3., 3., 3., 1., 3.], [10., 2., 4., 0., 0.]]'''
print(my_scans)
filter1=robo_filters()
ans_matrix=[[]]
ans_matrix=filter1.filter1_rangechange(my_scans)
print("-"*20,"\n")
print(ans_matrix)
'''Value of D is provided and the algorithm is not limited to only one specific
   value of D'''
obj= robo_filters(D=3)
req_output=obj.update(ans_matrix)
print("-"*20,"\n")
print(req_output)

