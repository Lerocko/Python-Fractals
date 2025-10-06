import numpy as np
import matplotlib.pyplot as plt
import math
import time

def generate_points(R = 150, r = 77, d = 69):
    k = r / R
    l = d / r
    numerator = round(R - r) # rounding numerator to avoid floating point issues
    denominator = round(r) # rounding denominator to avoid floating point issues
    g = math.gcd(numerator, denominator) # greatest common divisor
    q = (denominator // g) + 1 # number of rotations

    plt.ion() # turn on interactive mode
    fig, ax = plt.subplots(figsize=(8, 8)) # create a figure and axis
    ax.set_aspect('equal') # set equal aspect ratio
    ax.set_title('Hipotrochoid Drawing...') # set title
    line, = ax.plot([], [], lw=1.5) # create a line object

    xs = []
    ys = []
    for theta in range(0, 360 * q, 5):
        theta_rad = np.radians(theta)
        x = R*((1-k)*np.cos(theta_rad) + l*k*np.cos(((1-k)/k)*theta_rad))
        y = R*((1-k)*np.sin(theta_rad) - l*k*np.sin(((1-k)/k)*theta_rad))
        xs.append(x)
        ys.append(y)

        # Update the plot
        line.set_data(xs, ys) # update line data
        plt.pause(0.05) # speed of drawing

    ax.set_title('Hipotrochoid Completed!') # update title
    plt.ioff() # turn off interactive mode
    plt.show() # show the final plot


def main():
    generate_points()
    
        
        
if __name__ == "__main__":
    main()