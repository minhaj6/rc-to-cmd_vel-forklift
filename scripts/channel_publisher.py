from geometry_msgs.msg import Twist
from mavros_msgs.msg import RCIn
import rospy
import sys, time

rospy.init_node('mhr_rc_node')

rate = rospy.Rate(10)    # 10 Hz

vel_msg = Twist()

def sub_callback(data):
    vel_msg.linear.x = data.channels[2]   # up down of right gimbal
    vel_msg.linear.y = data.channels[0]   # left right steering
    vel_msg.linear.z = data.channels[5]   # up down of stepper (3 pos switch)

    rospy.loginfo(rospy.get_caller_id() + "Publishing velocity...")

    pub.publish(vel_msg)


pub = rospy.Publisher('/mhr/cmd_vel', Twist, queue_size = 20)
sub = rospy.Subscriber("mavros/rc/in", RCIn, sub_callback)

rospy.spin()
