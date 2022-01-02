# coding: utf-8
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
