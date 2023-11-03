# What is Matplotlib?
    
    Matplotlib is a low level graph plotting library in python that serves as a visualization utility.

    Matplotlib was created by John D. Hunter.

    Matplotlib is open source and we can use it freely.

    Matplotlib is mostly written in python, a few segments are written in C, Objective-C and Javascript for Platform compatibility.

# Where is the Matplotlib Codebase?

    The source code for Matplotlib is located at this github repository https://github.com/matplotlib/matplotlib


## Installation of Matplotlib

    If you have Python and PIP already installed on a system, then installation of Matplotlib is very easy.

   ## Install it using this command:

    pip install matplotlib

   ### Importing the package

    import matplotlib as matplt

   ### Check the version
    print("Matplotlib version:",matplt.__version__)

# Plotting x and y points
    The plot() function is used to draw points (markers) in a diagram.
    The function takes parameters for specifying points in the diagram.
    Parameter 1 is for the x-axis and Parameter 2 is for the y-axis.
    If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.
    Example:
    --------
    import matplotlib.pyplot as plt
    import numpy as np
    xpoints = np.array([1, 8])
    ypoints = np.array([3, 10])
    plt.plot(xpoints, ypoints)
    plt.show()

### Plotting Without Line 

    xpoints1 = np.array([1, 8])
    ypoints1 = np.array([3, 10])

    plt.plot(xpoints1, ypoints1, '*')       # In bracket we can mention in symbol
    plt.show()

   ### Multiple Points

    xpoints2 = np.array([1, 2, 6, 8])
    ypoints2 = np.array([3, 8, 1, 10])

    plt.plot(xpoints2, ypoints2)
    plt.show()


   ### Default X-Points
    Bydefault x value will takes as 0,1,2,3...etc or depend upon y value
    ypoints3 = np.array([3, 8, 1, 10, 7])

    plt.plot(ypoints3)
    plt.show()

# Marker
You can use the keyword argument marker to emphasize each point with a specified marker:
It will point the coordinates(https://www.w3schools.com/python/matplotlib_markers.asp)

    plt.plot(ypoints,marker="o")
    plt.show()

### "Marker | Line | Color "
    ypoints1 = np.array([3, 8, 1, 10])
    plt.plot(ypoints1, 'o:r')       ## here o means coordinate symble, : means dotted, r means red color
    plt.show()

### Marker Size
    ypoints2 = np.array([3, 8, 1, 10])
    plt.plot(ypoints2, marker = 'o', ms = 20)
    plt.show()

### Marker Color   
#### Marker Edge Color
    ypoints3 = np.array([3, 8, 1, 10])
    plt.title("Marker Edge Color Red ")
    plt.plot(ypoints3, marker = 'o', ms = 20, mec = 'r')  #mec -> marker edge color
    plt.show()

#### Marker Face Color
    ypoints = np.array([3, 8, 1, 10])
    plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'y')
    plt.show()

#### Marker | Size | Edge Color | Face Color
    plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
    plt.show()
