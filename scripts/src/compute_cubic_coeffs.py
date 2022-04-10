#!/usr/bin/env python
#!/usr/bin/env python
# Author : Kumar Sindhurakshit
# Student Id: 200854641
# Date : 22-Feb-2022
# Version: 1.0
# Last Modified : 23-Feb-2022

# This takes as input one full set of cubic trajectory parameters (initial and final
# position, initial and final velocity, initial and final time), and returns the four
# coefficients of the cubic polynomial trajectory (a0, a1, a2, a3).


from __future__ import print_function

from  ar_week5_test.srv  import compute_cubic_traj
from ar_week5_test.msg   import cubic_traj_coeffs
import rospy
import numpy as np

def handle_compute_cubic_coeff(req):
    req=req.param
    #M*A=C
    #Compute A= inv(M)*C
    #Create M from the recieved parameters 
    M = np.empty((4,4), float)
    M[0] = [ 1, req.t0, req.t0**2 , req.t0**3   ]
    M[1] = [ 0, 1,      2*req.t0  , 3*req.t0**2 ]
    M[2] = [ 1, req.tf, req.tf**2 , req.tf**3   ]
    M[3] = [ 0, 1,      2*req.tf  , 3*req.tf**2 ]
    #Create C
    C= np.array([req.p0 , req.v0, req.pf, req.vf], ndmin=2).T

    A = np.matmul(np.linalg.inv(M), C)
    res = cubic_traj_coeffs()
    res.a0=A[0]
    res.a1=A[1]
    res.a2=A[2]
    res.a3=A[3]
    res.t0=req.t0
    res.tf=req.tf
    return res

def compute_cubic_coeff_server():
    rospy.init_node('compute_cubic_coeff_server')
    s = rospy.Service('compute_cubic_coeff', compute_cubic_traj,  handle_compute_cubic_coeff)
    print("Service ready to compute cubic coefficients... ")
    rospy.spin()

if __name__ == "__main__":
    compute_cubic_coeff_server()

