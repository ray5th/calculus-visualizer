import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos, tan, exp, log, pi


equation = ""
def f(x):
    return eval(equation)

def calculus_demo():
    global equation
    equation = input("What function do you want to use: ").lower()
    mode = input("Do you want to Integrate of Differentiate: ").lower()
    if mode == "integrate":
        integrate()
    elif mode == "differentiate":
        differentiate()
    else:
        print("check for any spelling errors ._.")
        calculus_demo()

def integrate():
    start = float(input("Start of interval: "))
    end = float(input("End of interval: "))
    n = int(input("Number of rectangles: "))
    method = input("Riemann method (left, right, center): ").lower()
    dx = (end-start)/n
    if method == 'left':
        x = np.linspace(start, end-dx, n)
    elif method == 'right':
        x = np.linspace(start + dx, end, n)
    else:
        x = np.linspace(start + dx/2, end - dx/2, n)
    y = f(x)
    area = np.sum(y * dx)
    x_smooth = np.linspace(start, end, int((end - start) * 100))
    y_smooth = f(x_smooth)
    plt.figure(figsize=(10, 6))
    plt.plot(x_smooth, y_smooth, label='f(x)', color='blue')
    for xi, yi in zip(x, y):
        rect_x = xi
        if method == 'right':
            rect_x = xi - dx
        align = 'center' if method in ['midpoint', 'center'] else 'edge'
        plt.bar(rect_x, yi, width=dx, align=align, color='orange', edgecolor='black', alpha=0.5)
    plt.title(f"{method.capitalize()} Riemann Sum (Area ≈ {area:.6f})")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.show()
    calculus_demo()
    
def differentiate():
    x = float(input("What value do you want to find the derivitive of: "))
    mode = input("Want to use a left, right, center aproximation to brute force the derivitive: ").lower()
    h = float(input("How far should our 2 points be: "))
    if mode == "left":
        x0 = x - h
        x1 = x
    elif mode == "right":
        x0 = x
        x1 = x + h
    else:  # center
        x0 = x - h / 2
        x1 = x + h / 2
    y0 = f(x0)
    y1 = f(x1)
    derivative = (y1 - y0) / (x1 - x0)
    x_vals = np.linspace(x0, x1)
    y_vals = f(x_vals)
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label='f(x)', color='blue')
    plt.plot([x0, x1], [y0, y1], 'ro', label='Points used')
    plt.plot([x0, x1], [y0, y1], 'r--', label='Secant line (slope ≈ derivative)')
    plt.axvline(x, color='green', linestyle=':', label=f"x = {x}")
    plt.title(f"{mode.capitalize()} Approximation of Derivative at x = {x}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()
    calculus_demo()
calculus_demo()
