#!/usr/bin/env python3

name = 'sis-i-v-curve'

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

sis_vgap = numpy.arange(-1.5, 1.5, 0.01)
sis.set_vgap(-1.5)
time.sleep(3)
logger.start(file_name)
for vgap in sis_vgap:
    sis.set_vgap(vgap)
    time.sleep(0.2)
    continue
logger.stop()
sis.set_vgap(0)
