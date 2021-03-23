#!/usr/bin/env python

import rospy
from roscpp_to_rospy import ROSCppPublisher
from std_msgs.msg import String


class StringPublisher(object):
    def __init__(self):
        #self._pub = rospy.Publisher('/my_string', String, queue_size=10)
        self._pub = ROSCppPublisher(rospy.get_name().replace('/', '') + '_cpp', '/my_string', String._type, queue_size=10)    

    def run(self):
        msg = String("test")
        rospy.loginfo("Publishing as fast as possible (Python)")
        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            print("pub")
            self._pub.publish(msg)
            print("pub done")
            r.sleep()
            print("sleep done")


if __name__ == '__main__':
    rospy.init_node('test_string_pub', disable_signals=True)

    sp = StringPublisher()
    sp.run()