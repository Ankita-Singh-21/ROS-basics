#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

class ProcessData():

	def __init__(self):
		self.pub = rospy.Subscriber("/robot/front_laser/scan" , LaserScan, self.callback)

	def callback(self,msg):
		self.forward_laser = msg.ranges[210]
		rospy.loginfo("Laser Value: %s", self.forward_laser)
		self.process_data()

	def process_data(self):
		if self.forward_laser >1:
			rospy.loginfo(" Keep going")
		else:
			rospy.loginfo(" CAUTION!: You are getting close to an obstacle.")

if __name__ == '__main__':
	rospy.init_node(" process_data_subscriber")
	processdata_object = ProcessData()
	rospy.spin()
