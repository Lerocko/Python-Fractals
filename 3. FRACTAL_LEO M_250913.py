import matplotlib.pyplot as plt
import numpy as np

phi = (np.sqrt(5) - 1) / 2

def input_coords():
    A = np.array(list(map(float, input("Enter coordinates of point A (x y): ").split())))
    B = np.array(list(map(float, input("Enter coordinates of point B (x y): ").split())))
    return A, B


def cartesian_coords(A, B):
    V = B - A # vector from A to B
    d = np.linalg.norm(V) # distance from A to B
    theta = np.arctan2(V[1], V[0]) # angle in radians
    R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]) # rotation matrix
    p1 = A + (1-phi) * (B - A) # first division point
    p3 = A + phi * (B - A) # second division point
    p1p3 = np.linalg.norm(p3 - p1) # lenght of the base of the triangle
    L1 = np.linalg.norm(B - p3) # length 1 of the sides of the triangle
    L2 = np.linalg.norm(p1 - A) # length 2 of the sides of the triangle
    p2_x = (L1**2 - L2**2 + p1p3**2) / (2*p1p3) # x coordinate of the point p2
    p2_y = np.sqrt(L1**2 - p2_x**2) # y coordinate of the point p2
    p2_prev = np.array([p2_x, p2_y]) # point p2 in local coordinates
    p2_rotated = np.dot(R, p2_prev) # rotate point p2
    p2 = p2_rotated + A # translate point p2 to global
    if d > 10:
         # flake #1
        cartesian_coords(A, p1)
        # flake #2
        cartesian_coords(p1, p2)
        # flake #3
        cartesian_coords(p2, p3)
        # flake #4
        cartesian_coords(p3, B)
    else:
        # draw the smallest triangle of the fractal
        x_coords = [A[0], p1[0], p2[0], p3[0], B[0]]
        y_coords = [A[1], p1[1], p2[1], p3[1], B[1]]
        plt.plot(x_coords, y_coords, color='blue')  # draw lines connecting the points
        plt.axis('equal')  # keep the x and y axes at the same scale
        plt.pause(0.05)  # pause to update the plot
        

def main():
    print('Drawing the Koch Snowflake...')
    A, B = input_coords()
    plt.ion()  # turn on interactive mode
    cartesian_coords(A, B)
    plt.ioff()  # turn off interactive mode
    plt.show()  # keep the plot open

if __name__ == "__main__":
    main()