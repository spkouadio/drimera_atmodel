### Droplet description package ###

import const as cst
import math
import numpy as np
import matplotlib.pyplot as plt

humidity = 0.5 #50%
temp = 30 #°C

chem = 'thiophanate-methyl'
chem_density = cst.rho_l(chem)
chem_mass = 0.5 #grams
chem_dilrate = 0.1 #dilution of 10%

supp_volume = 50 #liters
supp_density = 1 #Water density


def sed_velocity(drop_diam):
    r'''The sedimentation velocity of the droplet is obtained at equilibrium (dV/dt=0),
    under conditions close to the ground where the wind movement is horizontal
        *:param drop_diam: droplet diameter depend of weigth fraction
        *:return: sedimentation velocity of differente droplet
    '''
    rho_vol = cst.rho_mix_vol(chem_dilrate, chem_density, supp_density)
    rho_a = cst.rho_a(humidity, temp)
    g = cst.g()
    Cd = cst.Cd()
    Vs = math.sqrt((4*g*(rho_vol)*drop_diam)/(3*Cd*rho_a))
    return Vs

#
def drop_distrib(mixt_volume):
    r'''
    Droplet distribution based on the log-normal distribution function
    :param mixt_volume:
    :return:
    '''
    n0 = 0.567
    sigma_g = 1.3
    d_50 = 254.74
    d_inf = 40
    d_sup = 500
    f_cumul = 0
    drop_table = np.empty((0, 3), float)
    for d in np.arange(d_inf, d_sup, sigma_g):
        f = (n0/(math.sqrt(2*math.pi)*d*math.log10(sigma_g)))\
            *math.exp(-math.pow(math.log10(d/d_50),2)/(2*math.pow(math.log10(sigma_g),2)))
        f_cumul = f_cumul + f
        drop_table = np.append(drop_table, np.array([[d, f, f_cumul]]), axis=0)
    return drop_table

# Plotting point using scatter method
X= drop_distrib(0)[:, 0]
Y1= drop_distrib(0)[:, 1]
Y2= drop_distrib(0)[:, 2]
plt.scatter(X,Y1 )
plt.show()
