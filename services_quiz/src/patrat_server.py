#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from services_quiz.srv import SquareMove, SquareMoveResponse

def my_callback(request):
    rospy.loginfo("Executa serviciul")

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rate = rospy.Rate(1)
    move = Twist()
    turn = Twist()

    move.linear.x = 0.2
    turn.angular.z = 1.57

    for r in range(request.repetitions):
        for i in range(4):
            rospy.loginfo("Merge inainte...")
            pub.publish(move)
            rospy.sleep(request.side / move.linear.x)

            rospy.loginfo("Vireaza dreapta...")
            pub.publish(turn)
            rospy.sleep(1.0)

    pub.publish(Twist())  # Stop
    rospy.loginfo("Termina miscarea")

    response = SquareMoveResponse()
    response.success = True
    return response

rospy.init_node('square_service_server')
my_service = rospy.Service('/move_in_square', SquareMove, my_callback)
rospy.loginfo("Serviciul este gata")
rospy.spin()
