# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   date：   '2019-01-23'
-------------------------------------------------
"""

from enum import  Enum
__author__ = 'mini'

class Cash(Enum):
    ANR = "ANR"
    I_ANR = 0
    CRASH = "CRASH"
    I_CRASH = 0
    EXCEPTION = "Exception"
    I_EXCEPTION = 0

# finish实际已经测试完设备个数
# devices 测试设备个数
info = []
finish = 0
