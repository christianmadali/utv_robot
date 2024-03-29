#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move_forward():
    rospy.init_node('move_forward', anonymous=True)
    pub = rospy.Publisher('/polaris/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(20)  # 10hz

    move_cmd = Twist()
    move_cmd.linear.x = 100  # Move forward at 0.5 m/s
    move_cmd.angular.z = 0.0  # No rotation

    while not rospy.is_shutdown():
        pub.publish(move_cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_forward()
    except rospy.ROSInterruptException:
        pass