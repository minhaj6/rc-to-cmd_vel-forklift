from geometry_msgs.msg import Twist, TwistStamped
from std_msgs.msg import Header
from mavros_msgs.msg import RCIn
import rospy
import sys, time

rospy.init_node('mhr_rc_node')

rate = rospy.Rate(10)    # 10 Hz

vel_msg = Twist()
data_head = Header()
vel_stamped = TwistStamped

data_head.seq = 0

def sub_callback(data):
    data_head.seq += 1
    data_head.stamp = rospy.Time.now()
    data_head.frame_id = "base_link"
    
    vel_msg.linear.x = data.channels[2]   # up down of right gimbal
    vel_msg.linear.z = data.channels[0]   # left right of right gimbal

    vel_stamped.header = data_head
#    vel_stamped.twist = vel_msg

    rospy.loginfo(rospy.get_caller_id() + "Publishing velocity...")

    pub.publish(vel_msg)


pub = rospy.Publisher('/mhr/cmd_vel', Twist, queue_size = 20)
sub = rospy.Subscriber("mavros/rc/in", RCIn, sub_callback)

rospy.spin()
