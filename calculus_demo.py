import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos, tan, exp, log, pi


equation = ""
def f(x):
    return eval(equation)

def calculus_demo():
    global equation
    equation = input("What funtion do you want to use: ").lower()
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
    print("Approximated area under the curve: ", calculate(start, end, n, method))
    awn = input("Press Enter to restart...")
    calculus_demo()
    
def differentiate():
    x = float(input("What value do you want to find the derivitive of: "))
    mode = input("Want to use a left, right, center aproximation to brute force the derivitive: ").lower()
    h = float(input("How far should our 2 points be: "))
    if mode = "left":
        return (f(x) - f(x-h))/h
    elif mode = "right":
        return (f(x+h) - f(x))/h
    else:
        return (f(x+h/2) - f(x-h/2))/h
    

def calculate(start, end, n, method):
    dx = (end-start)/n
    if method == 'left':
        x = np.linspace(start, end-dx, n)
    elif method == 'right':
        x = np.linspace(start + dx, end, n)
    else:
        x = np.linspace(start + dx/2, end - dx/2, n)
    y = f(x)
    area = np.sum(y * dx)
    graph = True
    if graph:
        x_smooth = np.linspace(start, end, int((end - start) * 100))
        y_smooth = f(x_smooth)

        plt.figure(figsize=(10, 6))
        plt.plot(x_smooth, y_smooth, label='f(x)', color='blue')

        for xi, yi in zip(x, y):
            rect_x = xi
            if method == 'right':
                rect_x = xi - dx  # Shift right rectangle to left edge
            align = 'center' if method in ['midpoint', 'center'] else 'edge'
            plt.bar(rect_x, yi, width=dx, align=align, color='orange', edgecolor='black', alpha=0.5)

        plt.title(f"{method.capitalize()} Riemann Sum (Area ≈ {area:.6f})")
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.legend()
        plt.show()
    return area
calculus_demo()
