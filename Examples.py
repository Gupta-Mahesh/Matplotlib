
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

xpoints1 = np.array([1, 8])
ypoints1 = np.array([3, 10])

plt.plot(xpoints1, ypoints1, '*')       # In bracket we can mention in symbol
plt.show()

#Multiple Points

xpoints2 = np.array([1, 2, 6, 8])
ypoints2 = np.array([3, 8, 1, 10])

plt.plot(xpoints2, ypoints2)
plt.show()


#Default X-Points
# Bydefault x value will takes as 0,1,2,3...etc or depend upon y value
ypoints3 = np.array([3, 8, 1, 10, 7])

plt.plot(ypoints3)
plt.show()


#Marker

ypoints4 = np.array([3, 8, 1, 10, 7])
plt.plot(ypoints4,marker="o")
plt.show()