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

