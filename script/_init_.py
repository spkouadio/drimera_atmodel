# -*- coding: utf-8 -*-
"""
Created as part of my PhD, on Sun Jun 19 12:04:32 2022

@author: KOUADIO, S.-P.
"""
import math

import const as cst
import droplet_descr
import matplotlib.pyplot as plt
import numpy as np
import droplet_dispersal as dd
import params
import conc_calculus as cc
from mpl_toolkits.mplot3d import Axes3D

app_rate = params.application_rate #l/ha
field_surf = params.field_surface #ha
chem_mass = params.chem_mass #(g/m2)
field_surface = params.field_surface #ha

#Droplets distribution by diameter
drop_dist = droplet_descr.drop_distrib()
"""
plt.plot(drop_dist[:, 0], drop_dist[:, 2])
plt.xlabel('diameter (µm)')
plt.ylabel('cumulated fraction')
plt.title('Droplet distribution')
plt.show()
"""

#Droplets trajectory
n_diam = len(drop_dist[:,0])
'''
for i in range (n_diam):
    plt.plot(dd.t_t, dd.x[i,:])
plt.xlabel('time (s)')
plt.ylabel('position (m)')
plt.title('Droplet trajectory')
plt.show()
'''
#Droplets concentration (quantity distribution)
t = 3600
pos_max = round(max(dd.x[:, t]))
#dt = .01
pos = 6
vol_unit = 1
field = 100 #int(field_surface*10000)
treat_field = int(field*0.5)
conc = np.zeros((field))
field_conc = np.zeros((field))
pos_x = dd.x[:, :]
'''
field_conc = np.zeros((it_field, n_diam))
field_conc[0,:] = drop_dist[:, 1]

dropfield_pos = np.zeros((it_field, n_diam))
dropfield_pos[0,:] = drop_dist[:, 1]


for i in range (it_field-1):
    for k in range(n_diam):
        dropfield_pos[i+1,k] = dropfield_pos[i,k] + drop_dist[k, 1]

plt.plot(field_conc[it_field-1, :])
plt.show()
'''

for i in range(n_diam):
    for x_pos in range (pos_max):
        if round(dd.x[i, t]) == x_pos:
           conc[x_pos] = conc[x_pos] + drop_dist[i, 1]

#Iteration
it = 0
field_conc[:] = conc[:]
while (it < treat_field):
    for i in range(treat_field-1):
        field_conc[i+1+it] = field_conc[i+1+it] + conc[i]
    it += 1

drift_field = field_conc[treat_field:]

conc_treat = 0
for i in [0, treat_field]:
    conc_treat += field_conc[i]

conc_drift = 0
for i in [treat_field+1, field-1]:
    conc_drift += field_conc[i]

#Result
#print(f'Le taux de derive est : = {(conc_drift/(params.chem_mass*treat_field))*100} %')
#print(f'Le taux de pulvérisation est : = {(conc_treat/(params.chem_mass*treat_field))*100} %')
#print(conc[:]*treat_field)

"""
drift_pos = [5,10,20,30,50] #m
for x in drift_pos:
    print(f'Droplet concentration at x = {x} m from treat field is {drift_field[x-1]*math.pow(10,6)} µg')
"""

# Plot concentration profile for a specific time
# Plot concentration profile by diameter
concent = np.zeros((101, 101))
for k in range(n_diam):
    i = round(dd.x[k, -1])
    j = dd.j
    u_air = dd.u_air
    alpha_buoy = dd.C_d(drop_dist[k, 0], dd.u_air[i, i], 0.0)
    c_0 = drop_dist[k, 1] #*math.pow(10,6) µg/l
    #concent = cc.conc_cal(u_air, alpha_buoy, c_0, i, j)
    concent = np.add(concent, cc.conc_cal(u_air, alpha_buoy, c_0, i, j))

plt.imshow(concent, cmap='hot', origin='lower', extent=[0, 100, 0, 100])
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
#plt.title(f'Time = {t:.2f}')
plt.title(f'Concentration in g/l at time = 100')
plt.show()

x = 80
print(f'Droplet concentration at x = {x} m from treat field is {round(concent[dd.j, x-1]*math.pow(10,6),3)} µg')
'''
plt.plot(dd.x[:, t], drop_dist[:, 0])
plt.xlabel('position (m)')
plt.ylabel('diameter (µm)')
plt.title(f'Droplet concentration at t = {t*dt} s')
plt.show()

#Droplets sedimentation
n_diam = len(drop_dist[:,0])

for t in range (len(dd.t_t)):
    plt.scatter(dd.x[100, t], dd.z[100, t])
plt.xlabel('position (m)')
plt.ylabel('altitude (m)')
plt.title('Droplet altitude per position')
plt.show() '''

'''
# Creating 3D figure
fig = plt.figure(figsize=(8, 8))
ax = plt.axes(projection='3d')

ax.plot3D(dd.z[:, t], dd.x[:, t], drop_dist[:, 1])
ax.set_xlabel('z')
ax.set_ylabel('x')
ax.set_zlabel('m')

plt.show()
'''



