#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class Publishdata():

	def __init__(self):

		self.pub = rospy.Publisher("/robot_topic",Twist,queue_size=1)
		self.msg = Twist()
		self.msg.linear.x = 0.2
		self.rate = rospy.Rate()

	def publish_msg(self):
		while not rospy.is_shutdown():
			rospy.loginfo("Publishing Twist message...")
			self.pub.publish(self.msg)
			self.rate.sleep()

if __name__ == '__main__':
	rospy.init_node("publish_data")
	publishdata_object = PublishData()
	publishdata_object.publish_msg()
