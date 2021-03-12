#!/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node('simple_publisher')
pub = rospy.Publisher('/new_topic',String,queue_size=1)
msg = String()
msg.data = " Hello ROS Developers"
rate = rospy.rate(1)

while not rospy.is_shutdown():
	pub.publish(msg)
	rate.sleep()