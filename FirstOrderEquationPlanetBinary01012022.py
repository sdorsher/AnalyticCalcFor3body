# coding: utf-8
get_ipython().run_line_magic('load', 'r13scriptsameanswer01012022.py')
# %load r13scriptsameanswer01012022.py
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
get_ipython().run_line_magic('load', 'StartOverScript.py')
# %load StartOverScript.py
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
get_ipython().run_line_magic('load', 'r13scriptsameanswer01012022.py')
# %load r13scriptsameanswer01012022.py
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
get_ipython().run_line_magic('load', 'r23scipt01012022.py')
# %load r23scipt01012022.py
r23=sqrt((x-X2)**2+(y-Y2)**2)
r23sq=(x-X2)**2+(y-Y2)**2
r23sqpert=r23sq.subs(R,R+dR)
r23sqfo=r23sqpert.series(dR,0,2).removeO()
r23sqfo=r23sqfo.subs(W,W*Wrel)
r23sqfo2=r23sqfo.series(dR,0,2).removeO()
r23sqfo2=cancel(r23sqfo2)
r23sqfirstorder=collect(r23sqfo2,dR).coeff(dR,1)
r23sqfirstorder=collect(r23sqfo2,dR)
r23sq0=r23sqfirstorder.coeff(dR,0)
r23sq1=r23sqfirstorder.coeff(dR,1)
r23sq0=trigsimp(r23sq0)
r23sq1=trigsimp(r23sq1)
r23sqapprox=r23sq0+dR*r23sq1
r23nosq=r23sq**(1/2)
r23nosqfo=r23nosq.series(dR,0,2).removeO()
r23nosq=r23sqapprox**(1/2)
r23nosqfo=r23nosq.series(dR,0,2).removeO()
r23nosqfirstorder=collect(r23nosqfo,dR)
r23nosq0=r23nosqfirstorder.coeff(dR,0)
r23nosq1=r23nosqfirstorder.coeff(dR,1)
r23nosq1=trigsimp(r23nosq1)
r23nosqapprox=r23nosq0+r23nosq1*dR
r23nosq1=r23nosq1.subs(1.0,1)
r23nosqapprox=r23nosq0+r23nosq1*dR
get_ipython().run_line_magic('load', 'Uscript01012022.py')
# %load Uscript01012022.py
U12 = -M**2/r12
U23 = -M*m/r23nosqapprox
U13=-M*m/r13nosqapprox
U23pert=U23.series(dR,0,2).removeO()
U23pert0=U23pert.coeff(dR,0)
U23pert1=U23pert.coeff(dR,1)
U23fo1=trigsimp(U23pert1).subs(1.0,1)
U23fo0=U23pert0
U23fo=U23fo0+U23fo1*dR
U13pert=U13.series(dR,0,2).removeO()
U13pert0=U13pert.coeff(dR,0)
U13pert1=U13pert.coeff(dR,1)
U13fo0=U13pert0
U13fo1=trigsimp(U13pert1).subs(1.0,1)
U13fo=U13fo0+U13fo1*dR
get_ipython().run_line_magic('load', 'vKEplanetEbinaryScript01012022_2.py')
# %load vKEplanetEbinaryScript01012022_2.py
# %load vKEplanetEbinaryScript01012022.py
v1, v2, v3 = symbols('v1, v2, v3')
v1 = M**2/(2*M)/R
v2=M**2/(2*M)/R
v3=M*m/(m+M)/r
v1pert=v1.subs(R,R+dR)
v2pert=v2.subs(R,R+dR)
v1fo=v1pert.series(dR,0,2).removeO()
v2fo=v2pert.series(dR,0,2).removeO()
K1=1/2*M*v1**2
K1=1/2*M*v1fo**2
K1fo=K1.series(dR,0,2).removeO()
K2fo=K1fo
K3=1/2*m*v3**2
Eplanetfo=U23fo+U13fo+K3
Eplanetfo0=Eplanetfo.coeff(dR,0)
Eplanetfo1=Eplanetfo.coeff(dR,1)
Eplanetapprox=Eplanetfo0+Eplanetfo1*dR
Eplanetapprox
Ebinaryfo=U12+K1+K2
Ebinaryfo=Ebinaryfo.series(dR,0,2).removeO()
Ebinaryfo=U12+K1fo+K2fo
U12fo=U12.series(dR,0,2).removeO()
Ebinaryfo=U12fo+K1fo+K2fo
U12orig=-M**2/2/R
K1orig=1/2*v1**2*M
K2orig=K1orig
K3orig=K3
U13orig=-M*m/r13
U12orig=-M*m/r12
U23orig=-M*m/r23
Eplanetfo0-U13orig-U23orig-K3orig
trigsimp(Eplanetfo0-U13orig-U23orig-K3orig)
Ebinaryfo0=Ebinaryfo.coeff(dR,0)
Ebinaryfo1=Ebinaryfo.coeff(dR,1)
U12orig=-M**2/2/R
Ebinaryfo0-U12orig-K1orig-K2orig
Eplanetfo1-Ebinaryfo1
Eqn=EplanetrgtR-Ebinaryfo1
limrgtREplanet=Eplanetfo1.series(R,0,2).removeO()
EplanetrgtR=cancel(limrgtREplanet).subs(1.0,1).subs(9.0,9).subs(6.0,6).subs(2.0,2)
EplanetrgtR=factor(EplanetrgtR)
EplanetrgtR=trigsimp(EplanetrgtR)
EplanetrgtR-Ebinaryfo1
Eqn=EplanetrgtR-Ebinaryfo1
Eqn2=Eqn.subs(R,M*z)
Eqn3=2*Eqn3
Eqn3=Eqn2.subs(m,m/kcoeff*k)
kcoeff=Eqn2.coeff(z,1)
Eqn3=Eqn2.subs(m,m/kcoeff*k)
Eqn3=2*z**3*Eqn3
Eqn3
Eqn3=cancel(Eqn3)
Eqn3
Eqn
