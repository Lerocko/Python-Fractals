import matplotlib.pyplot as plt
import numpy as np

phi = (np.sqrt(5) - 1) / 2  # proporción áurea

def input_coords():
    A = np.array(list(map(float, input("Enter coordinates of point A (x y): ").split())))
    B = np.array(list(map(float, input("Enter coordinates of point B (x y): ").split())))
    return A, B

def calculate_triangle_points(A, B):
    """Divide el segmento AB en 3 partes y calcula el punto P2 que forma el triángulo."""
    V = B - A
    d = np.linalg.norm(V)
    theta = np.arctan2(V[1], V[0])
    R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

    p1 = A + (1-phi) * V
    p3 = A + phi * V
    base_length = np.linalg.norm(p3 - p1)
    L = np.linalg.norm(p1 - A)  # lados iguales del triángulo
    p2_local = np.array([(L**2 - L**2 + base_length**2) / (2*base_length),
                         np.sqrt(L**2 - ((L**2 - L**2 + base_length**2) / (2*base_length))**2)])
    p2_global = np.dot(R, p2_local) + A
    return p1, p2_global, p3

def draw_koch_segment(A, B, min_length=10):
    """Dibuja recursivamente un segmento del copo de Koch."""
    d = np.linalg.norm(B - A)
    if d > min_length:
        p1, p2, p3 = calculate_triangle_points(A, B)
        draw_koch_segment(A, p1, min_length)
        draw_koch_segment(p1, p2, min_length)
        draw_koch_segment(p2, p3, min_length)
        draw_koch_segment(p3, B, min_length)
    else:
        # dibuja los puntos del triángulo mínimo
        p1, p2, p3 = calculate_triangle_points(A, B)
        x_coords = [A[0], p1[0], p2[0], p3[0], B[0]]
        y_coords = [A[1], p1[1], p2[1], p3[1], B[1]]
        plt.plot(x_coords, y_coords, color='blue')

def main():
    print("Drawing the Koch Snowflake...")
    A, B = input_coords()
    plt.ion()
    draw_koch_segment(A, B)
    plt.axis('equal')
    plt.ioff()
    plt.show()

if __name__ == "__main__":
    main()
