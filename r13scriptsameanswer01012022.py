# coding: utf-8
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
W,w=symbols('W,w')
Wprime=W0*Wrel
x=r*cos(w*t)
y=r*sin(w*t)
X1=R*cos(W*t)
X2=-R*cos(W*t)
Y1=R*sin(W*t)
Y2=-R*sin(W*t)
r12=2*R+2*dR
r13=sqrt((x-X1)**2+(y-Y1)**2)
r13sq=(x-X1)**2+(y-Y1)**2
r13sqpert=r13sq.subs(R,R+dR)
r13sqfo=r13sqpert.series(dR,0,2).removeO()
r13sqfo=r13sqfo.subs(W,W*Wrel)
r13sqfo2=r13sqfo.series(dR,0,2).removeO()
r13sqfo2=cancel(r13sqfo2)
r13sqfirstorder=collect(r13sqfo2,dR).coeff(dR,1)
r13sqfirstorder=collect(r13sqfo2,dR)
r13sq0=r13sqfirstorder.coeff(dR,0)
r13sq1=r13sqfirstorder.coeff(dR,1)
r13sq0=trigsimp(r13sq0)
r13sq1=trigsimp(r13sq1)
r13sqapprox=r13sq0+dR*r13sq1
r13nosq=r13sq**(1/2)
r13nosqfo=r13nosq.series(dR,0,2).removeO()
r13nosq=r13sqapprox**(1/2)
r13nosqfo=r13nosq.series(dR,0,2).removeO()
r13nosqfirstorder=collect(r13nosqfo,dR)
r13nosq0=r13nosqfirstorder.coeff(dR,0)
r13nosq1=r13nosqfirstorder.coeff(dR,1)
r13nosq1=trigsimp(r13nosq1)
r13nosqapprox=r13nosq0+r13nosq1*dR
r13nosq1=r13nosq1.subs(1.0,1)
r13nosqapprox=r13nosq0+r13nosq1*dR
