r'''
Droplet description module
'''

import const as cst
import math
import numpy as np
import params

# Atmosphere properties
humidity = params.humidity
temp = params.temp
air_density = params.air_density

# Chemical properties
chem = params.chem
chem_density = params.chem_density
chem_mass = params.chem_mass
chem_dilrate = params.chem_dilrate

# Support properties
supp_volume = params.supp_volume
supp_density = params.supp_density

# Mixture properties
rho_mix = params.rho_mix #Density of mixture
vol_mix = params.vol_mix #Volume of mixture


def init_velocity():
    r'''
    Droplets initial emission velocity is based on Bernoulli equation with some simplification hypothesis
    :return: initial velocity of droplets
    '''
    P = 10
    nu_e = 1
    V_0 = math.sqrt((2*nu_e*P)/rho_mix)
    return V_0


def drop_distrib():
    r'''
    Droplet distribution based on the log-normal distribution function
    :param mixt_volume: volume of the mixture that will be sprayed
    :return: drop_table that contains per line, the diameter of the droplet, with its volume fraction and the number of
    droplets of this diameter within, and the cumulative volume fraction
    '''
    n0 = 0.567
    sigma_g = 1.3
    d_50 = 254.74 # micrometer µm
    d_inf = 40
    d_sup = 500
    f_cumul = 0
    drop_table = np.empty((0, 4), float)
    for d in np.arange(d_inf, d_sup, sigma_g):
        f = (n0/(math.sqrt(2*math.pi)*d*math.log10(sigma_g)))\
            *math.exp(-math.pow(math.log10(d/d_50),2)/(2*math.pow(math.log10(sigma_g),2)))
        f_cumul = f_cumul + f
        n = f/(math.pow(d,3)*(math.pi/6))
        #drop_table = np.append(drop_table, np.array([[d, f*vol_mix, f_cumul, n]]), axis=0)
        drop_table = np.append(drop_table, np.array([[d, 1000*f*chem_mass, f_cumul, n]]), axis=0)
    return drop_table