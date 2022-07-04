r'''
Parameter lists for imput
'''

import const as cst


# Operational parameters
alt_spray = 5 #altitude of spray (m)

# Atmosphere properties
humidity = 0.5 #50%
temp = 30 #°C
air_density = cst.rho_a(humidity, temp)

# Chemical properties
chem = 'thiophanate-methyl'
chem_density = cst.rho_chem(chem)
chem_mass = 0.5 ##chemical mass (grams)
chem_dilrate = 0 ##chemical dilution rate (0%)

# Support properties
supp_volume = 50 #liters
supp_density = 1 #Water density

## Mixture properties
rho_mix = cst.rho_mix(chem_mass, chem_dilrate, chem_density, supp_volume, supp_density) #Density of mixture
#Volume of mixture
if chem_mass != 0 :
    vol_mix = supp_volume+(chem_mass/(1000*chem_density))
else:
    vol_mix = supp_volume*(1+chem_dilrate)