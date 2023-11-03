
import matplotlib.pyplot as plt
import numpy as np

#Marker
# It will point the coordinates  (https://www.w3schools.com/python/matplotlib_markers.asp)
ypoints = np.array([3, 8, 1, 10, 7])
plt.title("Marker")
plt.plot(ypoints,marker="o")
plt.show()

#Format Strings fmt
    # You can also use the shortcut string notation parameter to specify the marker.
"""
    '-'	    Solid line	
    ':'	    Dotted line	
    '--'	Dashed line	
    '-.'	Dashed/dotted line
"""
ypoints1 = np.array([3, 8, 1, 10])
plt.title("Marker | Line | Color ")
plt.plot(ypoints1, 'o:r')       ## here o means coordinate symble, : means dotted, r means red color
plt.show()

# Marker Size
    # You can use the keyword argument markersize or the shorter version, ms to set the size of the markers:

ypoints2 = np.array([3, 8, 1, 10])
plt.title("Marker Size")
plt.plot(ypoints2, marker = 'o', ms = 20)
plt.show()

# Marker Color    
# Marker Edge Color
ypoints3 = np.array([3, 8, 1, 10])
plt.title("Marker Edge Color Red ")
plt.plot(ypoints3, marker = 'o', ms = 20, mec = 'r')  #mec -> marker edge color
plt.show()

# Marker Face Color
ypoints = np.array([3, 8, 1, 10])
plt.title("Marker Face Color Yellow")
plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'y')
plt.show()

# Marker | Size | Edge Color | Face Color
plt.title("Marker | Size | Edge Color | Face Color")
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
plt.show()
