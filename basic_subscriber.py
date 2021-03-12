#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

class GetData():

	def __init__(self):

		# subscribing to the named topic to get data of Odometry type
		self.sub = rospy.Subscribers("/robot/robotnim_base_control/odom",Odometry, self.callback)


	def callback(self,msg):

		# printing the subscribed data in form of msg.pose.pose
		rospy.loginfo("Robot Current Pose :%s", msg.pose.pose)

if __name__ == '__main__':

	# initialising the node 
	rospy.init_node("get_data_subscriber")
	getdata_object = GetData()
	rospy.spin()
