### Droplet description package ###

import const as cst
import math

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
        *:return: sedimentation velocity of différente droplet
    '''
    rho_vol = cst.rho_mix_vol(chem_dilrate, chem_density, supp_density)
    rho_a = cst.rho_a(humidity, temp)
    g = cst.g()
    Cd = cst.Cd()
    Vs = math.sqrt((4*g*(rho_vol)*drop_diam)/(3*Cd*rho_a))
    return Vs

#
def drop_distrib(mixt_volume):
    r'''Droplet distribution based on the Stochastic Rosin-Rammler Diameter Distribution Method
        *:param mixt_volume:
        *:return:
    '''
    return
