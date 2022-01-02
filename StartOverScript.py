# coding: utf-8
# %load Perturb01012022.py
from sympy import init_session
init_session(quiet=True)
w, W, r, R, m, M, dR, t, x, y, X1, Y1, X2, Y2, U12, U13, U23, K1, K2, K3, E= symbols('w W r R m M dR t x y X1 Y1 X2 Y2 U12 U13 U23 K1 K2 K3 E')
W=2*pi/sqrt(2*pi*R**3/M)
w=2*pi/sqrt(2*pi*r**3/m)
Wpert=W.subs(R,R+dR)
Wpert=Wpert.series(dR,0,2).removeO()
Wpert.subs(sqrt(2)*sqrt(pi)/sqrt(R**3)*sqrt(M),W)
Wrel = powsimp(factor(Wpert/W),force=True)
Wrel.subs(sqrt(R**3),R**(3/2))
Wrel.subs(R**(1.0), R)
Wrel.subs(sqrt(R**3),R**(3/2)).subs(R**(1.0), R)
Wrel=Wrel.subs(sqrt(R**3),R**(3/2)).subs(1.0,1)
Wrel=expand(Wrel)
Wprime=Wrel*W
W0,w0=symbols('W0,wo')
Wprime=W0*Wrel
x=r*cos(w0*t)
y=r*sin(w0*t)
X1=R*cos(Wrel*t)
X2=-R*cos(Wrel*t)
Y1=R*sin(Wrel*t)
Y2=-R*sin(Wrel*t)
r12=2*R+2*dR
r13=sqrt((x-X1)**2+(y-Y1)**2)
w= symbols('w')
x=r*cos(w*t)
y=r*sin(w*t)
r13=sqrt((x-X1)**2+(y-Y1)**2)
X1=R*cos(Wprime*t)
X2=-R*cos(Wprime*t)
Y2=-R*sin(Wprime*t)
Y1=R*sin(Wprime*t)
r13=sqrt((x-X1)**2+(y-Y1)**2)
r13sq=(x-X1)**2+(y-Y1)**2
