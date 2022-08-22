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


plt.scatter(drop_dist[:, 1],  dd.z[:, t])
plt.xlabel('masse (mg)')
plt.ylabel('altitude')
plt.title(f'Droplet concentration at t = {t*dt} s')
plt.show()


#Droplets sedimentation
n_diam = len(drop_dist[:,0])

for i in range (n_diam):
    plt.plot(dd.t_t, dd.z[i,:])
plt.xlabel('time')
plt.ylabel('altitude')
plt.title('Droplet altitude')
plt.show()

'''
from mpl_toolkits import mplot3d
dist = np.zeros((len(dd.x[:, t]),2))
for i in range (n_diam):
    dist[i,0] = dd.x[i, t]
    dist[i,1] = dd.z[i, t]

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(dd.x[:, t], dd.z[:, t], dist[:,:], rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('surface')
ax.set_xlabel('t')
ax.set_ylabel('x')
ax.set_zlabel('z')
plt.show()
'''

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(dd.x[:, t], dd.z[:, t], drop_dist[:,1]) # plot the point (2,3,4) on the figure
plt.show()
'''
#Droplets sedimentation velocity
sed_velo = np.array([])
for diam in drop_dist[:,0]:
    sed_velo = np.append(sed_velo, 0) #droplet_descr.sed_velocity(diam))
#print(sed_velo)
#Droplets initial velocity
init_velo = droplet_descr.init_velocity()
#print("Droplets initial velocity = ",init_velo, "m/s")

# Plotting point using scatter method
#diam = drop_dist[10,0]
#while diam == dd.x[:, :, :]


x_max = round(x[- 1])
conc = np.zeros((x_max,x_max))
#Quantity distribution
for pos_i in range(x_max):
    for pos_j in range(x_max):
        conc[pos_i,pos_j] = 
 
 
fig = plt.figure(figsize=(6, 3.2))

ax = fig.add_subplot(111)
ax.set_title('colorMap')
plt.imshow(X)
ax.set_aspect('equal')

cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
cax.get_xaxis().set_visible(False)
cax.get_yaxis().set_visible(False)
cax.patch.set_alpha(0)
cax.set_frame_on(False)
plt.colorbar(orientation='vertical')
plt.show()
'''

