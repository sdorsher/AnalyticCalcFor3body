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
