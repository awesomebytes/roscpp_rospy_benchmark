#!/usr/bin/env python

import rospy
from std_msgs.msg import String

class StringSubscriber(object):
    def __init__(self):
        self._last_msg = None
        self._sub = rospy.Subscriber('/my_string', String, self._cb)


    def _cb(self, msg):
        self._last_msg = msg


if __name__ == '__main__':
    rospy.init_node('test_string_sub')
    rospy.loginfo("Subscribing")
    sp = StringSubscriber()
    
    rospy.spin()