#!/usr/bin/env python
# Author : Kumar Sindhurakshit
# Student Id: 200854641
# Date : 22-Feb-2022
# Version: 1.0
# Last Modified : 23-Feb-2022

# This node generates 4 diffrent different random values for initial and final position, p0, pf, 
# initial and final velocity, v0, vf, initial and final time, t0, tf, every 20 seconds, and publish
# them on a ROS Topic using the cubic_traj_params message. Positions should not exceed a maximum/minimum
# value P_MAX= +/- 10; velocities should not exceed a mximum/minimum value V_MAX = +/- 10. For the time, t0
# should always be 0, and tf should be tf = t0 + dt, with dt a random real number (i.e.float) between 5 and 10.

import rospy
import numpy as np
from std_msgs.msg import Float64
from ar_week5_test.msg import cubic_traj_param
def generator() :
    P_MIN = -10
    P_MAX =  10
    V_MIN = -10
    V_MAX =  10
    DT_MIN = 5
    DT_MAX = 10
    t0=0
    pub = rospy.Publisher('generated_points', cubic_traj_param, queue_size=10) # Creating publisher instance
    rospy.init_node('generator', anonymous=True)  # Node name iss generator , it can not contain slashesh it have to be base name
    rate = rospy.Rate(.05) # .05hz  it tells that we sshould go through loop n every 20 second with rate.sleep method
    while not rospy.is_shutdown():
        param = cubic_traj_param()
        param.p0 = np.random.uniform(low=P_MIN, high=P_MAX)
        param.pf = np.random.uniform(low=P_MIN, high=P_MAX)
        param.v0 = np.random.uniform(low=V_MIN, high=V_MAX)
        param.vf = np.random.uniform(low=V_MIN, high=V_MAX)
        dt=  np.random.uniform(low=DT_MIN, high=DT_MAX)
        param.t0=t0
        param.tf=t0+dt
        pub.publish(param)
        rospy.loginfo(param) # writes information both at console and log file
        rate.sleep()

if __name__ == '__main__':
    try:
        generator()
    except rospy.ROSInterruptException:
        pass
