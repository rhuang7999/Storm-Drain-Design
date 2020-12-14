# Storm-Drain-Diameter-Design

This program will aid the design of storm drains given the parameters of the location and specifications of the client.

Assumptions:
* Steady Uniform Flow
* Circular Channel Design

Inputs:
* If the units are in US or SI
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

## Setup
To use this program, this repository should be cloned/downloaded, then navigate to the local directory and create a virtual environment with:

## How to use the program
First enter whether the units are in US or SI. It should be inputted capitalized.\
`Units US or SI: US`\
Next input whether the desired design flowrate of the storm drain in cubic feet per second.\
`Storm Drain Design Flowrate in cfs: 11.2`\
Next enter the slope given by the topographic conditions. If no slope is given, enter N/A and then enter the length of the pipe and the headloss.\
`Slope Based on Topographic Conditions (N/A if not given): 0.02`\
Finally input the material of the pipe. It should be inputted all capitalized. Which will give the friction factor.\
`Pipe Material: STEEL`

## Program Description
Given, the design flowrate, slope, and material of the pipe,\
the diameter can be calculated by rearranging Manning's equation:
Q = (k / n) * A * (R ^ 2 / 3) * (S ^ 1 / 2)  
Q = Flowrate in pipe\
k = Units factor\
n = Manning friction factor\
A = Area of pipe = π * (d ^ 2) / 4\
R = Hydraulic radius = A / P = (π * (d ^ 2) / 4) / (π * d) = d / 4\
S = Slope\

The Manning's equation to solve for the diameter.
d = ((Q * n * (4 ** (5/3))) / (math.pi * k * (S  ** (1/2)))) ** (3/8)
