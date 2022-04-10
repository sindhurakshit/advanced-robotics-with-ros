#!/usr/bin/env python
# Author : Kumar Sindhurakshit
# Student Id: 200854641
# Date : 22-Feb-2022
# Version: 1.0
# Last Modified : 23-Feb-2022

# This node should subscribe to the ROS Topic created by path generator node, read the desired
# p0, pf, v0, vf, t0, tf published every 20 seconds, and to compute the a0,a1,a2,a3 coefficients
# of the cubic polynonial trajectory of thei form p(t) = a0 + a1*t + a2*t^2 + a3*t^3 that best fit
# those requirements. To compute the coefficients, the will call a "compute_cubic_traj" Service made
# available by Node 3. Then, the Node should publish the a0,a1,a2,a3 coefficients and t0,tf time 
# parameters on a ROS Topic, using the cubic_traj_coeffs message.

import rospy
#from std_msgs.msg import Float64 
from  ar_week5_test.srv import compute_cubic_traj
from  ar_week5_test.msg import cubic_traj_param
from  ar_week5_test.msg import cubic_traj_coeffs


def callback(param):     # param is of type cubic_traj_param
    # After recieving parameters from point generator log and request computaion of 
    # coefficients from compute_cubic_coeff service 
    # rospy.loginfo(rospy.get_caller_id() + 'I heard %s', param)
    rospy.wait_for_service('compute_cubic_coeff')
    try:
        compute_cubic_coeff = rospy.ServiceProxy('compute_cubic_coeff',compute_cubic_traj)
        resp = compute_cubic_coeff(param)
        #print("Recieved response from compute_cubic_coeff-->", resp)
        #now publish coefiecients recieved from compute_cubic_coeff service
        pub.publish(resp.coeff)  # publish message of type cubic_traj_coeffs
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)



def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('trajectory_planner', anonymous=True)
    # subscribe to the topic generated_points
    rospy.Subscriber('generated_points', cubic_traj_param, callback)
    
    #Create publisher 
    global pub
    pub = rospy.Publisher('computed_cubic_traj_coeffs',  cubic_traj_coeffs, queue_size=10) # Creating publisher instance



    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
