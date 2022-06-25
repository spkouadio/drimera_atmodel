import math
import numpy as np
import params
import const as cst
import droplet_descr


rho_mix = params.rho_mix
rho_a = params.air_density
drop_dist = droplet_descr.drop_distrib()
g = cst.g()
Cd = cst.Cd()

nx = 41
dx = 2 / (nx - 1)
nt = 20    #nt is the number of timesteps we want to calculate
dt = .025  #dt is the amount of time each timestep covers (delta t)
c = 1

u = np.ones(nx)      #as before, we initialize u with every value equal to 1.
u[int(.5 / dx) : int(1 / dx + 1)] = 2  #then set u = 2 between 0.5 and 1 as per our I.C.s

un = np.ones(nx) #initialize our placeholder array un, to hold the time-stepped solution

for n in range(nt):  # loop for values of n from 0 to nt, so it will run nt times
    un = u.copy()  ##copy the existing values of u into un
    for i in range(1, nx):  ## you can try commenting this line and...
        # for i in range(nx): ## ... uncommenting this line and see what happens!
        #u[i] = un[i] - c * dt / dx * (un[i] - un[i - 1])
        un[i] = dt*(un[i-1] + g*(rho_mix-rho_a)/rho_mix-(rho_a*math.pi*math.pow(drop_dist[0,0],2)*Cd*math.pow(un[i],2))/
                   (8*(rho_mix*math.pi*math.pow(drop_dist[0,0],3)/6)))

print(u)
print(un)