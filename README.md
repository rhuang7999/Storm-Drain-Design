# US-Storm-Drain-Design

This program will aid the design of storm drains in the United States given the parameters of the location and specifications of the client.\
Given these parameters it will provide the best pipe diameter that is available to be purchased in the United States.

Assumptions:
* Storm Drain is Designed in the United States
* Steady Uniform Flow
* Circular Channel Design
* Pipe Cross-Section, Slope, and Material are Uniform

Inputs:
* If the units are in US or SI
  * If the units are in SI, they should be converted to US
* Desired Design Flowrate
* Slope of pipe
  * Length of Pipe
  * Head Loss 
* Material of Pipe

Outputs:
* Calculated Pipe Diameter
* Storm Drain Pipe Diameter
* Maximum Flowrate
* Maximum Velocity
* Specific Energy when Full

## Setup
To use this program, this repository should be cloned/downloaded. Make sure you have have Python 3.0 installed.


## How to use the program
First enter whether the units are in US or SI. It should be inputted capitalized.\
`Units US or SI: US`\
If the units are SI, they should be converted because this is designed for the US.\
`Units US or SI: SI`\
`Convert units to US`\
`Are units converted from SI to US? (Y or N): Y`\
Next input whether the desired design flowrate of the storm drain in cubic feet per second.\
`Storm Drain Design Flowrate in cfs: 11.2`\
Next enter the slope given by the topographic conditions.\
`Slope Based on Topographic Conditions (N/A if not given): 0.02`\
If no slope is given, enter N/A and then enter the length of the pipe and the headloss in feet. The program will calcualte the headloss.\
`Length of pipe in feet: 2000`\
`Headloss in feet: 4`\
`0.002`\
Finally input the material of the pipe. It should be inputted all capitalized. Which will give the friction factor.\
`Pipe Material: STEEL`\
Given those inputs the program should output the calculated pipe diameter,\
the pipe diameter that should be purchased, and maximum flowrate and velocity\
`The calculated diameter is: 1.3080310194835059 ft`\
`The calculated diameter is: 15.69637223380207 inches`\
`For this storm drain a pipe of 18 inches should be purchased`\
`The maximum flowrate of the pipe is 16.136645744286362 cfs`\
`The maximum velocity of the pipe is 9.131473547114563 ft/s`\
`The specific energy when the pipe is full is 2.472322905099687 ft`

## Program Description
Given, the design flowrate, slope, and material of the pipe,\
the diameter can be calculated using Manning's equation:
Q = (k / n) * A * (R ^ 2 / 3) * (S ^ 1 / 2)  
Q = Flowrate in pipe\
k = Units factor\
n = Manning friction factor\
A = Area of pipe = π * (d ^ 2) / 4\
R = Hydraulic radius = A / P = (π * (d ^ 2) / 4) / (π * d) = d / 4\
S = Slope

The Manning formula uses water surface slope, cross-sectional area,\
and wetted perimeter of a length of uniform channel to determine the flow rate.\
However, Manning's equation can be rearragned to solve for diameter.\
d = ((Q * n * (4 ** (5/3))) / (pi * k * (S  ** (1/2)))) ** (3/8)

Although, Manning's equation gives us a value for pipe diameter,\
only certain size pipes are sold and the diameter is rounded up the closest higher diameter sold.

The maximum flowrate is calculated by using the Manning's equation with the new diameter.\
The maximum flowrate is calculated by dividing the maximum flowrate by the area of the pipe.\
The specific energy is calcualted using the diameter and maximum velocity.
