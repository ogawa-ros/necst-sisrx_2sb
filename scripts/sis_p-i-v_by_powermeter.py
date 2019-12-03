#!/usr/bin/env python3

name = 'sis_p-i-v_by_spectrometer'

import sys
import rospy
import time
import std_msgs.msg
import argparse
import datetime


sys.path.append("../../necst-core/scripts")

import controller
import core_controller

rospy.init_node(name)

sis = controller.sis()
logger = core_controller.logger()

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
file_name = name + '/' + date + '.necstdb'
print(file_name)



logger.start(file_name_hot)

for i in range(num):
    v = start_v + int_v * i
    sis.set_v(v)
    time.sleep(ii_time)

logger.stop()
