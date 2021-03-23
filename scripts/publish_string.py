#!/usr/bin/env python

import rospy
from std_msgs.msg import String

class StringPublisher(object):
    def __init__(self):
        self._pub = rospy.Publisher('/my_string', String, queue_size=10)

    def run(self):
        msg = String("test")
        rospy.loginfo("Publishing as fast as possible (Python)")
        r = rospy.Rate(100)
        while not rospy.is_shutdown():
            self._pub.publish(msg)
            r.sleep()


if __name__ == '__main__':
    rospy.init_node('test_string_pub2')
    sp = StringPublisher()
    sp.run()