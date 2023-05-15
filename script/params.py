r'''
Parameter lists for imput
'''
import math
import const as cst

class parameter(object):
    def __init__(self, activeMatCarac, supportCarac, dropletSize, activMatConc, carrierVol, boomHeight, appRate,
                 residualConc, windSpeed, temperature, humidity, timeStep):

        self.chem = activeMatCarac
        self.supportCarac = supportCarac
        self.dropletSize = dropletSize

        self.active_mat_conc = activMatConc
        self.supp_volume = carrierVol
        self.boomHeight = boomHeight
        self.application_rate = appRate
        self.resConcentration = residualConc
        self.air_velocity = windSpeed
        self.temp = temperature
        self.humidity = humidity
        self.time_nt = timeStep

    def pars(self):
        # Operational parameters
        #alt_spray = 5  # altitude of spray (m)
        #aeronef_velocity = 15  # m/s

        # Atmosphere properties
        #humidity = 0.5  # 50%
        #temp = 30  # °C
        #alt = 10  # m
        #resConcentration = 5  # µg/l
        #air_velocity = 4  # m/s

        air_pressure = 10.1325  # mCE
        air_sp_ratio = 1.4  # air specific heat ratio

        air_density = cst.rho_a(self.humidity, self.temp)
        air_dviscosity = cst.mu_a(self.temp)
        air_kviscosity = cst.mu_a(self.temp) / air_density

        # Times step dispersion
        time_nt = 180

        # Chemical properties
        #chem = 'thiophanate-methyl'
        chem_density = cst.rho_chem(self.chem)

        #active_mat_conc = 400
        #active_mat_conc_unit = 'g/l'
        # Application properties
        #application_rate = 2
        #app_rate_unit = 'l/ha'

        chem_mass = self.active_mat_conc * self.application_rate * math.pow(10, -4)  ##chemical mass (g/m2)
        chem_dilrate = 0  ##chemical dilution rate (0%)

        # Support properties
        supp_volume = 1  # liters
        supp_density = 1  # Water density

        # Field properties
        field_surface = 0.025  # ha

        if chem_dilrate != 0:
            chem_mass = chem_dilrate * self.supp_volume * (1000 * chem_density)

        ## Mixture properties
        rho_mix = cst.rho_mix(chem_mass, chem_dilrate, chem_density, self.supp_volume, supp_density)  # Density of mixture
        # Volume of mixture
        vol_mix = supp_volume + (chem_mass / (1000 * chem_density))
"""        
# Operational parameters
alt_spray = 5 #altitude of spray (m)
aeronef_velocity = 15 #m/s

# Atmosphere properties
humidity = 0.5 #50%
temp = 30 #°C
alt = 10 #m
resConcentration = 5 #µg/l
air_velocity = 4 #m/s
air_pressure = 10.1325 #mCE
air_sp_ratio = 1.4 #air specific heat ratio

air_density = cst.rho_a(humidity, temp)
air_dviscosity = cst.mu_a(temp)
air_kviscosity = cst.mu_a(temp) / air_density

#Times step dispersion
time_nt = 180

# Chemical properties
chem = 'thiophanate-methyl'
chem_density = cst.rho_chem(chem)

active_mat_conc = 400
active_mat_conc_unit = 'g/l'
# Application properties
application_rate = 2
app_rate_unit = 'l/ha'

chem_mass = active_mat_conc*application_rate*math.pow(10,-4) ##chemical mass (g/m2)
chem_dilrate = 0 ##chemical dilution rate (0%)

# Support properties
supp_volume = 1 #liters
supp_density = 1 #Water density

# Field properties
field_surface = 0.025 #ha

if chem_dilrate != 0 :
    chem_mass = chem_dilrate*supp_volume*(1000*chem_density)

## Mixture properties
rho_mix = cst.rho_mix(chem_mass, chem_dilrate, chem_density, supp_volume, supp_density) #Density of mixture
#Volume of mixture
vol_mix = supp_volume+(chem_mass/(1000*chem_density))

"""