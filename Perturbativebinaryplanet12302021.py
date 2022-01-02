# coding: utf-8
symbols('w W r R m M dR t x y X1 Y1 X2 Y2 U12 U13 U23 K1 K2 K3 E'
}
symbols('w W r R m M dR t x y X1 Y1 X2 Y2 U12 U13 U23 K1 K2 K3 E')
w, W, r, R, m, M, dR, t, x, y, X1, Y1, X2, Y2, U12, U13, U23, K1, K2, K3, E= symbols('w W r R m M dR t x y X1 Y1 X2 Y2 U12 U13 U23 K1 K2 K3 E')
w = Function('w')
W=Function('W')
w, W = symbols('w, W')
pi
W=2*pi/sqrt(2*pi*R**3/M)
w=2*pi/sqrt(2*pi*r**3/m)
W
w
W.series(R,0,2)
Wnew=W.subs(R,R+dR)
Wnew
Wnew.series(dR,0,2)
x=r*cos(w*t)
y=r*sin(w*t)
X1=-R*cos(W*t)
Y1=-R*sin(W*t)
X2=R*cos(W*t)
Y2=R*sin(W*t)
r13, r23=symbols('r13,r23')
r13=sqrt((x-X1)**2+(y-Y1)**2)
r23=sqrt((x-X2)**2+(y-Y2)**2)
r13
r23
r12 = symbol('r12')
r12 = symbols('r12')
r12 = 2*R
U12 = -M*M/r12
U12
U13=-M*m/r13
U13
U23=-M*m/r23
U23
vcirc, m1, m2, rcirc=symbols('vcirc,m1,m2,rcirc')
vcirc=m1*m2/(m1+m2)/rcirc
vcirc
v, V1, V2 = symbols('v, V1, V2')
v=vcirc.subs(m1,m).subs(m2,M).subs(rcirc,r)
v
V1=vcirc.subs(m1,M).subs(m2,M).subs(rcirc,R)
V1
V2=V1
V2
V = symbols('V')
V=V1
V
K1=1/2*M*V**2
K1
K2 = 1/2*M*V**2
K2
K3 = 1/2*m*v**2
K3
Econs = symbols('Econs')
Econs = U12+U13+U23+K1+K2+K3-E
Econs
Eperturbed=Econs.subs(R, R+dR)
Eperturbed
Efirstorder=Eperturbed.series(dR,0,3)
Efirstorder=Eperturbed.series(dR,0,2)
Efirstorder
Efirstorder.removeO
Efirstorder.removeO()
Efirstorder.series(dR,0,1).removeo()
Efirstorder.series(dR,0,1).removeO()
EdR=Efirstorder.removeO()-Efirstorder.series(dR,0,1).removeO()
EdR
EdR/dR
EdR=EdR/dR
EdR
factor(EdR)
EdR.replace(sqrt(2)*sqrt(pi)*sqrt(M)/R**(3/2)-sqrt(2)*sqrt(pi)*sqrt(m)/r**(3/2),w0)
w0=symbol('w0')
w0=symbols('w0')
EdR.replace(sqrt(2)*sqrt(pi)*sqrt(M)/R**(3/2)-sqrt(2)*sqrt(pi)*sqrt(m)/r**(3/2),w0)
EdR
EdR.replace(sqrt(2)*sqrt(pi)*sqrt(M)*t/R**(3/2)-sqrt(2)*sqrt(pi)*sqrt(m)*t/r**(3/2),w0*t)
EdR.replace(sqrt(2)*sqrt(pi)*sqrt(M)*t/R**(3/2),W*t)
EdR.subs(sqrt(2)*sqrt(pi)*sqrt(M)/R**(3/2)-sqrt(2)*sqrt(pi)*sqrt(m)/r**(3/2),w0)
EdR.subs(sqrt(2)*sqrt(pi)*sqrt(M)/R**(3/2)-sqrt(2)*sqrt(pi)*sqrt(m)/r**(3/2),w0)
EdR.subs(sqrt(2)*sqrt(M)/R**(3/2)-sqrt(2)*sqrt(m)/r**(3/2),w0)
EdR.subs(sqrt(2)*sqrt(pi)*sqrt(M)/R**(3/2),W)
EdR=Efirstorder.removeO()-Efirstorder.series(dR,0,1).removeO()
EdR=EdR/dR
EdR.subs(sqrt(2)*sqrt(M)/R**(3/2)-sqrt(2)*sqrt(m)/r**(3/2),w0)
EdRnew=EdR.subs(sqrt(2)*sqrt(M)/R**(3/2)-sqrt(2)*sqrt(m)/r**(3/2),w0)
EdRnew
EdRnew=EdR.subs(sqrt(2*pi*M/R**3),W)
EdRnew
EdRbyr=EdR.series(R/r,0,2)
EdRbyr
limit(EdR,r,oo)
numEdR=EdR.subs(M,100).subs(m,1).subs(R,10).subs(r,1000)
numEdR
simplify(numEdR)
solve(numEdR,t)
solveset(numEdR,t)
Eperturbation
Eperturb
