#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
import cv2
import sys
import numpy as np
from cv_bridge import CvBridge, CvBridgeError

def webcam_pub():
    pub = rospy.Publisher('webcam/image_raw', Image, queue_size=1)
    rospy.init_node('webcam_pub', anonymous=True)
    rate = rospy.Rate(60) # 60hz

    bridge = CvBridge()
    frameWidth = 752
    frameHeight = 480
    
    

    while not rospy.is_shutdown():
	cam = cv2.VideoCapture('DJI.mp4')
        cam.set(3, frameWidth)
        cam.set(4, frameHeight)

	while(True):
        	ret, frame1 = cam.read()
		frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
		print(ret)
        	
        	if not ret:
			rospy.loginfo("Capturing image failed.")

        	pub.publish(bridge.cv2_to_imgmsg(frame, "mono8"))
		print(frame.shape)
        	rate.sleep()
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break


if __name__ == '__main__':
    try:
        webcam_pub()
    except rospy.ROSInterruptException:
        pass
cv2.destroyAllWindows()
