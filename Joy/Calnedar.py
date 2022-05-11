# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 12:05:28 2022

@author: Sai Prathap
"""
import calendar
def check_leap(year):
    if year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0:
        return True
    return False
def check_date(year  , month , date ,  leap):
    month_days = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if leap:
        month_days[2] = 29
    if date <= month_days[month]:
        return False
    return True
while(1):
    k = input('Enter date in dd/mm/yyyy format (year >= 1970) :')
    date = int(k[0:2])
    month = int(k[3:5])
    year = int(k[6:])
    leap = check_leap(year)
    if year < 1970:
        print('Invalid year , try again!')
    elif month < 1 or month > 12:
        print('Invalid month , try again!')
    elif date < 1 or check_date(year, month, date, leap):
        print('Invlid date , try again!')
    else:
        break
day_index = calendar.weekday(year, month, date)
days = ['Monday' , 'Tuesday' , 'Wednesday' , 'Thursday' , 'Friday' , 'Saturday' , 'Sunday']
print(date,"/" , month , "/" , year , "falls on",days[day_index])