import math
import numpy as np
import params
import const as cst
import droplet_descr

import matplotlib.pyplot as plt

rho_mix = params.rho_mix
rho_a = params.air_density
drop_dist = droplet_descr.drop_distrib()
alt_spray = params.alt_spray
init_velocity = droplet_descr.init_velocity()
g = cst.g()
Cd = cst.Cd()

nx = 41
dx = 2 / (nx - 1)
nt = 150    #nt is the number of timesteps
dt = .025  #dt is the amount of time each timestep covers (delta t)
c = 1

n_diam = len(drop_dist[:,0])
v = np.zeros((nt,n_diam))
x = np.zeros((nt,n_diam))
z = np.zeros((nt,n_diam)) # for altitude
t = np.zeros(nt)
v[0,:] = init_velocity # initialization of droplet velocity
z[0,:] = alt_spray # altitude of spray initialization

# Droplet velocity and position by diameter
for n in range(nt - 1):
    for i in range(n_diam):
        vel = dt*(g*(rho_mix-rho_a)/rho_mix-(rho_a*math.pi*math.pow(drop_dist[i,0],2)*Cd*math.pow(v[n,i],2))/
                       (8*(rho_mix*math.pi*math.pow(drop_dist[i,0],3)/6))) + v[n,0]
        if vel >= 0 :
            v[n+1, i] = vel # droplet velocity
            z[n+1, i] = alt_spray
        else :
            alt = z[n, i] - droplet_descr.sed_velocity(drop_dist[i,0])*dt # droplet altitude
            if alt >= 0 : z[n+1, i] = alt

        x[n + 1, i] = x[n, i] + v[n+1, i]*dt # droplet position

# Timestep
for n in range(nt):
    t[n] = n*dt

plt.scatter(z[:,0],x[:,0])
plt.show()
