
Supported Example Functions
===========================

You can input any function of x using standard Python math syntax. Here are some examples:

1. Power / Polynomial
   - x**2 + 3*x + 5       → Quadratic function

2. Trigonometric
   - sin(x)               → Sine function (in radians)
   - cos(x) + 2           → Cosine function
   - 2*sin(x)**2          → Sine squared

3. Exponential
   - exp(x)               → e^x
   - exp(-x**2)           → Gaussian curve

4. Logarithmic
   - log(x)               → Natural log (ln)

5. Constants
   - pi                   → Pi (≈ 3.1416)

6. Mixed / Composite
   - x**2 * sin(x)        → Mixed trigonometric and polynomial
   - 1 / (1 + x**2)       → Rational function

Syntax Tips
-----------
- Use `**` for powers (not `^`)
- Use lowercase functions: sin, cos, log, exp
- Input must be a valid Python expression using x
- Trig functions use radians, not degrees

Invalid Examples (will NOT work)
--------------------------------
- x^2         → use x**2 instead
- Sin(x)      → use lowercase sin(x)
- 1/x-2)      → mismatched parentheses
- sqrt(x)     → not supported unless manually added
