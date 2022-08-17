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

#Droplets sedimentation velocity
sed_velo = np.array([])
for diam in drop_dist[:,0]:
    sed_velo = np.append(sed_velo, 0) #droplet_descr.sed_velocity(diam))
#print(sed_velo)
#Droplets initial velocity
init_velo = droplet_descr.init_velocity()
#print("Droplets initial velocity = ",init_velo, "m/s")


# Plotting point using scatter method
X = dd.x[:, 1]
t = dd.t
#X= drop_dist[:, 0]
#Y1= drop_dist[:, 1]
#Y2= drop_dist[:, 2]
#N = drop_dist[:, 3]

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(t, X)
plt.show()

#plt.scatter(X,Y2)
#plt.show()
