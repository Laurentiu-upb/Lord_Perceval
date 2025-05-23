#! /usr/bin/env python
import rospy
import actionlib
from std_msgs.msg import Empty
from actiune_drona.msg import ComandaDronaAction, ComandaDronaFeedback

class ServerDrona:
    def _init_(self):
        self.server = actionlib.SimpleActionServer('/actiune_drona', ComandaDronaAction, self.callback, False)
        self.server.start()
        self.pub_decolare = rospy.Publisher('/ardrone/takeoff', Empty, queue_size=1)
        self.pub_aterizeaza = rospy.Publisher('/ardrone/land', Empty, queue_size=1)
        self.rate = rospy.Rate(1)
        self.empty = Empty()

    def callback(self, goal):
        feedback = ComandaDronaFeedback()
        if goal.comanda == "DECOLARE":
            self.pub_decolare.publish(self.empty)
            while not rospy.is_shutdown():
                if self.server.is_preempt_requested():
                    break
                feedback.status = "Decolez..."
                self.server.publish_feedback(feedback)
                self.rate.sleep()
        elif goal.comanda == "ATERIZEAZA":
            self.pub_aterizeaza.publish(self.empty)
            feedback.status = "Aterizez..."
            self.server.publish_feedback(feedback)
            self.rate.sleep()
        self.server.set_succeeded()

if __name__ == '__main__':
    rospy.init_node('server_actiune_drona')
    ServerDrona()
    rospy.spin()
