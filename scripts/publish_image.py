#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image

from image_tools import ImageTools

class StringPublisher(object):
    def __init__(self):
        self._image_tools = ImageTools()
        self._image = self._image_tools.load_from_file('../lena.png')
        self._image_msg = self._image_tools.convert_cv2_to_ros_msg(self._image)
        # 512x512 png image
        self._pub = rospy.Publisher('/my_image', Image, queue_size=10)

    def run(self):
        rospy.loginfo("Publishing as fast as possible (Python)")
        r = rospy.Rate(100)
        while not rospy.is_shutdown():
            self._image_msg.header.stamp = rospy.Time.now()
            self._pub.publish(self._image_msg)
            r.sleep()


if __name__ == '__main__':
    rospy.init_node('test_image_pub')
    sp = StringPublisher()
    sp.run()