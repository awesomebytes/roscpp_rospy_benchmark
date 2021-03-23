#include "ros/ros.h"
#include "std_msgs/String.h"

#include <sstream>

/**
 * This tutorial demonstrates simple sending of messages over the ROS system.
 */
int main(int argc, char **argv)
{

  ros::init(argc, argv, "test_string_pub_cpp");

 
  ros::NodeHandle n;

  ros::Publisher pub = n.advertise<std_msgs::String>("/my_string", 10);

  ros::Rate loop_rate(100);

    std_msgs::String msg;

    std::stringstream ss;
    ss << "test";
    msg.data = ss.str();
  
  while (ros::ok())
  {

    // ROS_INFO("%s", msg.data.c_str());

    pub.publish(msg);

    ros::spinOnce();

    loop_rate.sleep();
  }


  return 0;
}