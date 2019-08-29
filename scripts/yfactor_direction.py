#!/usr/bin/env python3

name = 'yfactor_for_spectrum'

import sys
import rospy
import time
import std_msgs.msg
import argparse

sys.path.append("~/ros/src/necst-core/scripts")
sys.path.append("~/ros/src/necst-sisrx_2sb/scripts")

import controller
import core_controller

rospy.init_node(name)

sis = controller.sis()
logger = core_controller.logger()

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
file_name_hot = name  + '/hot/' + date + '.necstdb'
file_name_cold = name + '/cold/' + date + '.necstdb'
print(file_name)

sis_v = input("")
sis.set_v()
time.sleep(1)
input('READY HOT MEASUREMENT? PRESS ENTER!!')
logger.start(file_name_hot)
time.sleep(5)
logger.stop()

input('READY COLD MEASUREMENT? PRESS ENTER!!')
logger.start(file_name_cold)
time.sleep(5)
logger.stop()
