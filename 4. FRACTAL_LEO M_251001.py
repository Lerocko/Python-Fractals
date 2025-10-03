import matplotlib.pyplot as plt
import numpy as np
import random

def ask_num_vertices():
    """"Ask user for number of vertices."""
    while True:
        try:
            n = int(input("Enter the number of vertices major or equals to 3 (e.g., 3 for triangle, 4 for square): "))
            if n < 3:
                print("Number of vertices must be at least 3.")
                continue
            return n
        except ValueError:
            print("Invalid input. Please enter an integer.")

def ask_regular():
    """Ask user if they want a regular or random fractal."""
    while True:
        choice_regular = input("Do you want the fractal to be regular? (y/n): ").lower()
        if choice_regular in ['y', 'n']:
            return choice_regular == 'y'
        print("Invalid input. Please enter 'y' or 'n'.")

def ask_inverse_fractal():
    """Ask user if they want to invert the fractal."""
    while True:
        choice_inverse = input("Do you want to invert the fractal? (y/n): ").lower()
        if choice_inverse in ['y', 'n']:
            return choice_inverse == 'y'
        print("Invalid input. Please enter 'y' or 'n'.")

def ask_continue():
    """Ask user if they want to continue."""
    while True:
        cont = input("Would you like to draw another fractal? (y/n): ").lower()
        if cont in ['y', 'n']:
            return cont == 'y'
        print("Invalid input. Please enter 'y' or 'n'.")

def drawKochSF(A, B, is_regular=True, choice_inverse=False):
    """Draw Koch Snowflake segment from point A to B."""
    d = np.linalg.norm(B - A)
    r = d / 3.0
    n = -np.array([(A[1] - B[1]) / d, (B[0] - A[0]) / d]) # Normal vector
    
    # Invert normal vector if user chose to
    if choice_inverse:
        n = -n  # Invert normal vector if user chose to
    
    # Height of the equilateral triangle
    h = r * np.sqrt(3) / 2.0 # Height of the equilateral triangle
    
    # For random fractals, vary the height of the pike
    if is_regular == False:
        h = r * np.sqrt(3) / 2.0 * random.uniform(0.5, 1.5) # Random height factor
        
    # Calculate points
    p1 = (2*A + B) / 3.0
    p3 = (A + 2*B) / 3.0
    C = (A + B) / 2.0
    p2 = C + h * n

    # Recursive case
    if d > 10:
        # flake #1
        drawKochSF(A, p1, is_regular, choice_inverse)
        # flake #2
        drawKochSF(p1, p2, is_regular, choice_inverse)
        # flake #3
        drawKochSF(p2, p3, is_regular, choice_inverse)
        # flake #4
        drawKochSF(p3, B, is_regular, choice_inverse)
    # Base case
    else:
        # draw lines
        x_coords = [A[0], p1[0], p2[0], p3[0], B[0]]
        y_coords = [A[1], p1[1], p2[1], p3[1], B[1]]
        plt.plot(x_coords, y_coords, color='red')
        plt.axis('equal')
        plt.draw
        plt.pause(0.00001)

def generate_vertices(num_vertices = 3, radius=250):
    """Generate vertices of a equilater regular polygon circunscrite."""
    angles = (2*np.pi/num_vertices)
    for i in range(num_vertices):
        yield (radius * np.cos(i*angles), radius * np.sin(i*angles))

def draw_fractal(num_vertices, is_regular, choice_inverse):
    """Draw the complete fractal based on user inputs."""
    plt.clf() # Clear the current figure
    vertices = list(generate_vertices(num_vertices))
    for i in range(len(vertices)):
        A = np.array(vertices[i])
        B = np.array(vertices[(i + 1) % len(vertices)])
        drawKochSF(A, B, is_regular, choice_inverse)
    plt.draw()
    plt.pause(0.1)

def main():
    print("Let's play whit fractals!")
    plt.figure()
    plt.ion()
    plt.title("Koch Snowflake Fractal")
    
    while True:
        n = ask_num_vertices()
        is_regular = ask_regular()
        choice_inverse = ask_inverse_fractal()
        draw_fractal(n, is_regular, choice_inverse)
        
        if not ask_continue():
            print("Thank you for using the fractal generator. Goodbye!")
            break
    
    plt.ioff()
    plt.show()

if __name__ == "__main__":
    main()
    
    

    




