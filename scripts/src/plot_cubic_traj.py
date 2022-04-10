#!/usr/bin/env python
# Author : Kumar Sindhurakshit
# Student Id: 200854641
# Date : 22-Feb-2022
# Version: 1.0
# Last Modified : 23-Feb-2022

# This Node subscribes to the ROS Topic created by Node 2, read the a0,a1,a2,a3 coefficients 
# and t0,tf time parameters published every 20 seconds, and publishes three separate ROS topics:
# position trajectory, velocity trajectory and acceleration trajectory. These trajectories 
# are then visualized with the rqt_plot GUI, on the same plot, with different colors.
# The three trajectories should appear on the GUI at the same time, and last for tf seconds.

import rospy
import numpy as np
from  ar_week5_test.srv  import compute_cubic_traj
from  ar_week5_test.msg  import cubic_traj_coeffs
from  std_msgs.msg        import Float64

# Function computes position , velocity and acceleration trajectories from coeffs
def compute_trajectories(coeffs):
    #print("Coefficient for computation", coeffs)
    
    pos = coeffs.a0 + coeffs.a1*coeffs.tf + coeffs.a2*coeffs.tf**2 + coeffs.a3*coeffs.tf**3  # Position trajectory 
    vel = coeffs.a1 + 2*coeffs.a2*coeffs.tf + 3*coeffs.a3*coeffs.tf**2                       # Veleocity trajecory
    accl= 2*coeffs.a2 + 3*2*coeffs.a3*coeffs.tf                                                   # Acceleration trajectory
    return pos, vel, accl


def callback(param):     # param is of type cubic_traj_coeffs
    rospy.loginfo(rospy.get_caller_id() + 'Coeffs  %s', param)
    tf_max=param.tf
    try:
        for tf in  np.linspace(0,tf_max,20): #calulate value every second
            param.tf=tf
            pos,vel,accl = compute_trajectories(param)
            pub_pt.publish(pos)
            pub_vt.publish(vel)
            pub_at.publish(accl)
            rospy.sleep(1)   #sleep for a second publishing next values for plotting

    except rospy.ServiceException as e:
        print("Unable to publish plotting parameters: %s"%e)




def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('trajectory_plotter', anonymous=True)
    rospy.Subscriber('computed_cubic_traj_coeffs', cubic_traj_coeffs, callback)
    global pub_pt, pub_vt, pub_at  #variables to hold publisher instances
    pub_pt = rospy.Publisher('trjpos',  Float64, queue_size=10) # Creating position trajectory publisher instance
    pub_vt = rospy.Publisher('trjvel',  Float64, queue_size=10) # Creating velocity trajecotory publisher instance
    pub_at = rospy.Publisher('trjacl',  Float64  , queue_size=10) # Creating acceleration trajectory publisher instance

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
