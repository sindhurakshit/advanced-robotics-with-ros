# advanced-robotics-with-ros
Basic framework for ros programming covering services, messages, publishing and reading from topics, pakage creation etc in python
Package : ar_week5_test

OVERVIEW : This package is developed to demonstrate development of basic ROS programming and creating package  for distribution. It consist four nodes to generated random points, compute coeficients service, planning trajectory, and a ploter to plot position, veleocity, and acceleration using rqt topics. 

**Keywords:** ros example, trajectory planning, rqt_plot, rosrun

#HOW TO RUN 
1. unzip ar_week5_test to your ros work space.
2. make catkin work space , using “catkin_make”
3. run launch file in your terminal window with  “roslaunch ar_week5_test cubic_traj_gen_launch”

**NODES :** 
1. points_generator.py : This node generates different random values for intital and final values  for poistion, velocity and time

2. cubic_traj_planner.py This node should subscribe to the ROS Topic created by above node, read the desired p0, pf, v0, vf, t0, tf published every 20 seconds, and  computes the a0,a1,a2,a3 coefficients of the cubic polynonial trajectory by calling “compute_cubic_traj" service provided by node 3. 
3. compute_cubic_coeffs.py : This node makes "compute_cubic_traj"  service available to any external node requesting it.
4. plot_cubic_traj.py: This mode subscribes to the ROS Topic created by node 2 and read the a0,a1,a2,a3 coefficients and t0,tf time parameters published every 20 seconds, and publish three separate ROS topics: position trajectory, velocity trajectory and acceleration trajectory.

**MESSAGES:**
1) cubic_traj_params:  contains 6 real values (Float64): p0, pf, v0, vf, t0, tf; i.e.  initial and final position, initial and final velocity, initial and final time.
2) cubic_traj_coeffs, which contains 6 real values (Float64): a0, a1, a2, a3, t0, tf; i.e. the four coefficients of a cubic polynomial trajectory, plus the initial and final time.

**ROS REFRENCE :** Visit http://www.ros.org for additinal documentation on ROS
