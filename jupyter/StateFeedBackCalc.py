import scipy
from sympy import *
import numpy as np
from numpy import linalg as LA
import control

def get_characteristicPoly(poles):
    s = symbols('s')
    df=1
    for roots in poles:
        df = Poly(df*(s-roots))
    return df.all_coeffs()


def get_feedbackGains(A,B,poles):
    eigenVals = LA.eig(A) #Get eigenvalues of A
    Coeff_des = np.array(get_characteristicPoly(poles)) # get the coeffficients of the desired polynomial
    Coeff_orig = np.array(get_characteristicPoly(eigenVals[0])) # get the coeffficients of the original polynomial
    kb = Coeff_des-Coeff_orig # Get the kb row vector
    kb = np.split(kb,[1])[1] # Drop the first element since its always going to be 0 and is not required
    
    n = len(A)
    ctrb_mat = control.ctrb(A,B) #Get the controlability matrix of the the system
    
    # Get the C_bar matrix formed by using the coefficients of the original polynomial in the upper triangular part of the matrix
    # [[1 alpha1 alpha2],
    #  [0   1    alpha1],
    #  [0   0       1 ]]
    try:
        Q = np.identity(n)
        for i in range(1,n):
            for j in range(0,n-1):
                Q[j][i] = Coeff_orig[i-j]
                
        # Get the desired Gains k such that the poles are in the required spots
        Q = np.dot(LA.inv(Q),LA.inv(ctrb_mat))
        k = np.dot(kb,Q)
    except:
        print("An error occured")
    
    return k
    