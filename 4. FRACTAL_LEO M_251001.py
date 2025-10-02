import matplotlib.pyplot as plt
import numpy as np
import random

def drawKochSF(A, B):
    """Draw Koch Snowflake segment from point A to B."""
    global is_regular # Use global variable to determine if fractal is regular or random
    d = np.linalg.norm(B - A)
    r = d / 3.0
    n = -np.array([(A[1] - B[1]) / d, (B[0] - A[0]) / d]) # Normal vector
    # For random fractals, vary the height of the pike
    if is_regular == False:
        h = r * np.sqrt(3) / 2.0 * random.uniform(0.5, 1.5) # Random height factor
        if random.choice([True, False]):
            n = -n  # Invert normal vector randomly for asymmetry
    h = r * np.sqrt(3) / 2.0 # Regular height
    p1 = (2*A + B) / 3.0
    p3 = (A + 2*B) / 3.0
    C = (A + B) / 2.0
    p2 = C + h * n
    if d > 10:
        # flake #1
        drawKochSF(A, p1)
        # flake #2
        drawKochSF(p1, p2)
        # flake #3
        drawKochSF(p2, p3)
        # flake #4
        drawKochSF(p3, B)
    else:
        # draw lines
        x_coords = [A[0], p1[0], p2[0], p3[0], B[0]]
        y_coords = [A[1], p1[1], p2[1], p3[1], B[1]]
        plt.plot(x_coords, y_coords, color='red')
        plt.axis('equal')

def generate_vertices(num_vertices = 3, radius=250):
    """Generate vertices of a equilater regular polygon circunscrite."""
    angles = (2*np.pi/num_vertices)
    for i in range(num_vertices):
        yield (radius * np.cos(i*angles), radius * np.sin(i*angles))

def main():
    global is_regular # Declare global variable
    plt.figure()
    print("Let's play whit fractals!")
    plt.title("Koch Snowflake Fractal")
    plt.ion()
    while True:
        plt.clf()
        # Ask user for number of vertices
        while True:
            try:
                n = int(input("Enter the number of vertices major or equals to 3 (e.g., 3 for triangle, 4 for square): "))
                if n < 3:
                    print("Number of vertices must be at least 3.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
        # Ask user if they want a regular or random fractal
        while True:
            choice_random = input("Do you want the fractal to be regular? (y/n): ").lower()
            if not choice_random in ['y','n']:
                print("Invalid input. Please enter 'y' or 'n'.")
                continue
            else:
                is_regular = choice_random == 'y'
                break
        # Generate vertices and draw Koch Snowflake
        vertices = list(generate_vertices(n))
        plt.ion()
        for vertex in range(len(vertices)):
            A = np.array(vertices[vertex])
            B = np.array(vertices[(vertex + 1) % len(vertices)])
            drawKochSF(A, B)
        plt.ioff()
        plt.show()
        plt.pause(0.1)
        while True:
            cont = input("Would you like to draw another fractal? (y/n): ").lower()
            if cont in ['y', 'n']:
                break
            print("Invalid input. Please enter 'y' or 'n'.")
        if cont == 'n':
            print("Thank you for using the fractal generator. Goodbye!")
            break

if __name__ == "__main__":
    main()
    
    

    




