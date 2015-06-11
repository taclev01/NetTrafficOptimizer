# NetTrafficOptimizer
Attempts to test Neural Network Optimization on-the-fly for traffic grids

*** Dependencies: vPython (http://vpython.org), Python 2.7.9, gcc 4.8

This package provides a framework to test on-the-fly neural network optimization for grid-based traffic flow.  Waiting at stoplights is a particularly annoying delay, costing cities, companies and individuals both time and money.  We attempt to quantify the potential improvement of a smart grid that reoptimizes traffic light timing based on current traffic flow instead of relying on archaic manual adjustments of traffic light timing that is essentially a waste of manpower

Implemented so far:
 * ability to draw roads, cars, stoplights and animate them

Still to implement:
 * v0.1
   * Stoplight animation
   * Vehicle detection of red lights
   * Vehicle destinations (cars should attempt to move toward a goal)
   * Pathfinding algorithm to guide cars along roads
 * v0.2
   * Neural network interface
