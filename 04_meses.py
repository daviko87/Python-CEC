# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 10:15:16 2019

@author: CEC
"""
def isYearLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
def daysInMonth(year, month):
    if year < 1500 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = days[month - 1]
    if month == 2 and isYearLeap(year):
        res = 29
    return res
print(daysInMonth(2020,2 ))



























