#!/usr/bin/env python3

name = 'yfactor_with_v'

import sys
import rospy
import time
import std_msgs.msg
import numpy as np
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

vol = np.linespace(0, 8, 800)   #search optimal SIS voltage value
sis.set_v(0)
logger.start(file_name)
for v in vol:             #measure y-factor
    sis.set_v(v)
    time.sleep(0.03)
    continue
logger.stop()
sis.set_v(0)
