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

The first input is whether the units are in US or SI. It should be inputted capitalized.\
The next input is the desired design flowrate of the storm drain in cubic feet per second.\
The next input is the slope given by the topographic conditions. If no slope is given, enter the length of the pipe and the headloss.\
The final input is the material of the pipe. It should be inputted all capitalized. Which would give the friction factor.


Given, the design flowrate, slope, and material of the pipe,\
the diameter can be calculated by rearranging Manning's equation:
Q = (k / n) * A * (R ^ 2 / 3) * (S ^ 1 / 2)  
Q = Flowrate in pipe\
k = Units factor\
n = Manning friction factor\
A = Area of pipe = π * (d ^ 2) / 4\
R = Hydraulic radius = A / P = (π * (d ^ 2) / 4) / (π * d) = d / 4\
S = Slope\


