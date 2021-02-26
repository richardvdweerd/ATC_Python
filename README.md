(WORK IN PROGRESS)

# ATC_Python
Automatic Train Control in Python (to make it platform independent - more or less)

## History
Twenty years ago I developped a program for controlling my digital model railway. Recently I found back my old notes. Now I try to revive this program.

## Purpose of this program
Controlling a random digital model railway. Editing the track has to be simpel and flexibel.
Every train has the possibility to follow a timetable, but avoiding collissions by slowing down or stopping unscheduled.

## Functions
"Traffic Control" has to control every train individual. The program calculates the braking distance according to the speed and deceleration of the train. 
Every train has some properties: speed, direction, deceleration, acceleration, desired speed, desired direction, location on the layout.

