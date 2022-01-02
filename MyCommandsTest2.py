# coding: utf-8
from sympy import init_session
init_session(quiet=True)
Integral(sqrt(1/x),x)
x=symbols('x')
Integral(x**2,x)
integrate(x**2,x)
integrate(exp(-x),(x,0,oo))
