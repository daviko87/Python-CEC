# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:43:09 2019

@author: CEC
"""
import datetime
oTime = datetime.datetime.now()
print (oTime.isoformat())


from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))