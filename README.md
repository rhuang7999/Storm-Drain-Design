# Storm-Drain-Diameter-Design

This program will aid the design of storm drains given the parameters of the location and specifications of the client.

Assumptions:

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


The pipe diameter can be calculated by rearranging Manning's equation:
Q = (k / n) * A * (R ^ 2 / 3) * (S ^ 1 / 2)  
Q = Flowrate in pipe\
k = Units factor\
n = Manning friction factor\
A = Area of pipe = π * (d ^ 2) / 4\
R = Hydraulic radis = A / P = (π * (d ^ 2) / 4) / (π * d) = d / 4\
S = Slope
