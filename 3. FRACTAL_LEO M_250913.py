import matplotlib.pyplot as plt
import numpy as np

phi = (np.sqrt(5) - 1) / 2

def input_coords():
    A = np.array(list(map(float, input("Enter coordinates of point A (x y): ").split())))
    B = np.array(list(map(float, input("Enter coordinates of point B (x y): ").split())))
    return A, B


def cartesian_coords(A, B):
    # Divide the segment AB into 3 parts and calculate point P2 that forms the triangle
    V = B - A # vector from A to B
    d = np.linalg.norm(V) # distance from A to B
    theta = np.arctan2(V[1], V[0]) # angle in radians
    R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]) # rotation matrix
    
    p1 = A + (1-phi) * (B - A) # first division point
    p3 = A + phi * (B - A) # second division point
    base_length = np.linalg.norm(p3 - p1) # lenght of the base of the triangle
    L = np.linalg.norm(p1 - A) # length of the sides of the triangle
    p2_local = np.array([(L**2 - L**2 + base_length**2) / (2*base_length),
                         np.sqrt(L**2 - ((L**2 - L**2 + base_length**2) / (2*base_length))**2)])
    p2_global = np.dot(R, p2_local) + A
    return p1, p2_global, p3
    
def draw_koch_segment(A, B, min_length=10):
# Recursively draw a Koch snowflake segment
    d = np.linalg.norm(B - A)
    if d > min_length:
        p1, p2, p3 = cartesian_coords(A, B)
        draw_koch_segment(A, p1, min_length)
        draw_koch_segment(p1, p2, min_length)
        draw_koch_segment(p2, p3, min_length)
        draw_koch_segment(p3, B, min_length)
    else:
        # draw the smallest triangle of the fractal
        p1, p2, p3 = cartesian_coords(A, B)
        x_coords = [A[0], p1[0], p2[0], p3[0], B[0]]
        y_coords = [A[1], p1[1], p2[1], p3[1], B[1]]
        plt.plot(x_coords, y_coords, color='blue')  # draw lines connecting the points
        
        

def main():
    print('Drawing the Koch Snowflake...')
    A, B = input_coords()
    plt.ion()  # turn on interactive mode
    draw_koch_segment(A, B)
    plt.axis('equal')  # equal scaling for x and y axes
    plt.ioff()  # turn off interactive mode
    plt.show()  # keep the plot open

if __name__ == "__main__":
    main()