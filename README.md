# Bovarin_aiip
Python assessment
from __future__ import print_function
import time  # for delaying in second
import random  # to simulate 16 float readings between 0 and 1
import datetime
from random import choice
import logging
from pathlib import path
# Dummy dataset for 32 sensors with 16 float readings each.
Sensors = []sensor1 = {'ID':'sensor1', 'readings1': 'r1'} # data stream for sensor 1 referenced to pipeline region 1
Sensors.append(sensor1)count = 16  # represents 16 float readingsfor i in range( 0, count ):    
r1 = random.random()  # generates random number between 0 and 1    
