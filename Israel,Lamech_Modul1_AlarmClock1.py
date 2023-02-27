

#########################################
# CS 1110A - Programming in Python      #
# Module 1 - Exercise 1 - Alarm Clock 1 #
# Author: Lamech Israel                 #
#                                       #
#########################################

print('Alarm Clock, Part 1')

# Input

currentTime = 5
amPm = 'am'

print('\nRight now, it is', currentTime,amPm)

# Processing

alarmHours = 83
alarmDays = int(alarmHours/24)
alarmRemander = alarmHours%24

alarmTime = currentTime + alarmRemander


if alarmTime > 11:
    if amPm == 'am':
        amPm = 'pm'
    else :
        amPm = 'am'

if alarmTime >= 12:
    alarmTime = alarmTime % 12
    
#Output
    

print('The alarm clock will ring after',alarmHours,'hours which is',alarmDays,'days from now at',alarmTime,amPm)

print('\nDone!')
    

