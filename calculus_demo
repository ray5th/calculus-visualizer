import numpy as np
import matplotlib.pyplot as mp
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
    print("work in progress")
    calculus_demo()

def calculate(start, end, n, method):
    dx = (end-start)/n
    if method == 'left':
        x = np.linspace(start, end-dx, n)
    elif method == 'right':
        x = np.linspace(start + dx, end, n)
    else:
        x = np.linspace(start + dx/2, end - dx/2, n)
    y = f(x)
    return np.sum(y * dx)
calculus_demo()
