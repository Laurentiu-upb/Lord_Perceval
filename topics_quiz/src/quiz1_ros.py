#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):
    move = Twist()

    front = msg.ranges[360]
    right = msg.ranges[180]
    left = msg.ranges[540]

    if front > 1.0:
        move.linear.x = 0.5
        move.angular.z = 0.0
    elif front < 1.0:
        move.linear.x = 0.0
        move.angular.z = 0.5
    elif right < 1.0:
        move.linear.x = 0.0
        move.angular.z = 0.5
    elif left < 1.0:
        move.linear.x = 0.0
        move.angular.z = -0.5

    pub.publish(move)

rospy.init_node('quiz1_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
sub = rospy.Subscriber('/laser/scan', LaserScan, callback)

rospy.spin()
