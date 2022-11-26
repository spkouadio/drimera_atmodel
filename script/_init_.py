# -*- coding: utf-8 -*-
"""
Created as part of my PhD, on Sun Jun 19 12:04:32 2022

@author: KOUADIO, S.-P.
"""
import const as cst
import droplet_descr
import matplotlib.pyplot as plt
import numpy as np
import droplet_dispersal as dd
import params
from mpl_toolkits.mplot3d import Axes3D

app_rate = params.application_rate #l/ha
field_surf = params.field_surface #ha
chem_mass = params.chem_mass #(g/m2)
field_surface = params.field_surface #ha

#Droplets distribution by diameter
drop_dist = droplet_descr.drop_distrib()

plt.plot(drop_dist[:, 0], drop_dist[:, 2])
plt.xlabel('diameter (µm)')
plt.ylabel('cumulated fraction')
plt.title('Droplet distribution')
plt.show()


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
t = 1500
dt = .01
pos = 6
quantity = 0
vol_unit = 1
it_field = field_surface*10000

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
for i in range (n_diam):
    if round(dd.x[i, t]) == pos :
        quantity = quantity + drop_dist[i,1]
conc = quantity / vol_unit

print(f'Droplet concentration at x = {pos} m is {conc} mg')

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

