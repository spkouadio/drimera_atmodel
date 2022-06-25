r'''
Constants package
'''

import numpy as np

#Gravity
def g():
    return 9.18

#Buyoency coefficient
def Cd():
    return 0.447

#Air density
def rho_a(humid, temp):
    P = 101325 #air pressure (Pa)
    Rs = 287.06 #water vapor specifique constant
    rho = float((1/(Rs*(temp+273.15)))*(P-230.617*humid*np.exp((17.5043*temp)/(241.2+temp))))
    return rho

#Mixture density
def rho_mix_mass(chem_mass, chem_density, supp_volume, supp_density):
    rho_mix = float((chem_mass + supp_density*supp_volume)/((chem_mass/(1000*chem_density)) + supp_volume))
    return rho_mix

def rho_mix_vol(chem_dilrate, chem_density, supp_density):
    rho_mix = float(((chem_dilrate*chem_density) + supp_density)/(1 + chem_dilrate))
    return rho_mix

def rho_mix(chem_mass, chem_dilrate, chem_density, supp_volume, supp_density):
    if chem_dilrate == '' or chem_dilrate == 0 :
        return rho_mix_mass(chem_mass, chem_density, supp_volume, supp_density)
    else :
        return rho_mix_vol(chem_dilrate, chem_density, supp_density)


#Chemical density in g/ml
def rho_chem(chem):
    chem_density = np.array((['thiophanate-methyl', 1.45], ['difenoconazole', 1.37], ['epoxiconazole', 1.38],
                             ['propiconazole', 1.09], ['tebuconazole', 1.25], ['fenpropimorph', 0.93],
                             ['azoxystrobin', 1.34], ['trifloxystrobin', 1.36]))
    d_chem = float(chem_density[np.where(chem_density[:, 0] == chem), 1])

    return d_chem