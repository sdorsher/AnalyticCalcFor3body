# coding: utf-8
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
