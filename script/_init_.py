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
from mpl_toolkits.mplot3d import Axes3D


#Droplets distribution by diameter
drop_dist = droplet_descr.drop_distrib()

plt.plot(drop_dist[:, 0], drop_dist[:, 2])
plt.xlabel('diameter')
plt.ylabel('cumulated fraction')
plt.title('Droplet distribution')
plt.show()

#Droplets trajectory
n_diam = len(drop_dist[:,0])

for i in range (n_diam):
    plt.plot(dd.t_t, dd.x[i,:])
plt.xlabel('time')
plt.ylabel('position')
plt.title('Droplet trajectory')
plt.show()

#Droplets concentration (quantity distribution)
t = 1500
dt = .01

plt.plot(dd.x[:, t], drop_dist[:, 1])
plt.xlabel('position')
plt.ylabel('masse (mg)')
plt.title(f'Droplet concentration at t = {t*dt} s')
plt.show()

#Droplets sedimentation
n_diam = len(drop_dist[:,0])

for t in range (len(dd.t_t)):
    plt.scatter(dd.x[100, t], dd.z[100, t])
plt.xlabel('position')
plt.ylabel('altitude')
plt.title('Droplet altitude per position')
plt.show()

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

