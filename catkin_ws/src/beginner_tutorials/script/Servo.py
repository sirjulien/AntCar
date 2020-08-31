#!/usr/bin/python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from i2cpwm_board.msg import ServoArray
from i2cpwm_board.msg import Servo
import time

class Servo:
    # Initialiser un moteur et le message a envoyer
    def __init__(self,pwm1,pwm2):
        self.pub = rospy.Publisher('/servos_absolute', ServoArray,queue_size=100)
        rospy.init_node('Servo', anonymous=True)
        rospy.on_shutdown(self.arret)
        self.rate = rospy.Rate(50) # 10hz
        self.msg=ServoArray()
        self.Servo1=Servo()
        self.Servo2=Servo()
        self.Servo1.servo=pwm1
        self.Servo1.value=0
        self.Servo2.servo=pwm2
        self.Servo2.value=0
        self.msg.servos=[self.Servo1, self.Servo2]
    # Procedure d'arret
    def arret(self):
        print "STOP !"
        self.Servo1.value=0
        self.Servo2.value=0
        self.msg.servos=[self.Servo1, self.Servo2]
        rospy.loginfo(self.msg)
        self.pub.publish(self.msg)
    # Publication du message sur le topic
    def Pub_msg(self,value):
        self.Servo1.value=value
        self.Servo2.value=value
        self.msg.servos=[self.Servo1, self.Servo2]
        self.debut=time.time()
        while not rospy.is_shutdown():

            if time.time()-self.debut>60:
                rospy.signal_shutdown("We are done here!")
            #rospy.loginfo(self.msg)
            self.pub.publish(self.msg)



if __name__ == '__main__':
    try:

        #time.sleep(60)
        Servo=Servo(1,3)
        #Servo.Pub_msg(345)
        #time.sleep(20)
        #Servo.Pub_msg(545)
        #time.sleep(20)
        #Servo.Pub_msg(345)
        #time.sleep(20)
        #Servo.arret()

    except rospy.ROSInterruptException:
        pass
