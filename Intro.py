
#Import Matplotlib
import matplotlib as mplt
import matplotlib.pyplot as plt
import numpy as np

#Checking Matplotlib Version
print("Matplotlib version:",mplt.__version__)

"""
Example
Get your own Python Server
Draw a line in a diagram from position (0,0) to position (6,250):
"""
#Plotting x and y points
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()



#Plotting Without Line