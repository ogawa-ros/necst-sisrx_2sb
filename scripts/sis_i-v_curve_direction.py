#!/usr/bin/env python3

name = 'sis_i-v_curve'

import sys
import rospy
import time
import std_msgs.msg
import numpy
import argparse
import datetime

sys.path.append("../../necst-core/scripts")

import controller
import core_controller

rospy.init_node(name)

logger = core_controller.logger()
sis = controller.sis()

date = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')
file_name = name + '/' + date + '.necstdb'
print(file_name)

sis_vgap = numpy.arange(0.3, 1, 0.01)
sis.set_vgap(0.3)
time.sleep(3)
logger.start(file_name)
for vgap in sis_vgap:
    sis.set_vgap(vgap)
    time.sleep(0.03)
    continue
logger.stop()
sis.set_vgap(0)
