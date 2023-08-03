r'''
Parameter lists for imput
'''
import math
from script.const import constants #import const as cst

class inputs_par(object):
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

        self.cst = constants() #constants new instance

        self.air_pressure = 10.1325  # mCE
        self.air_sp_ratio = 1.4  # air specific heat ratio

        self.air_density = self.cst.rho_a(self.humidity, self.temp)
        self.air_dviscosity = self.cst.mu_a(self.temp)
        self.air_kviscosity = self.cst.mu_a(self.temp) / self.air_density
        # Times step dispersion
        #self.time_nt = self.time_nt  # 180

        # Chemical properties
        # chem = 'thiophanate-methyl'
        self.chem_density = self.cst.rho_chem(self.chem)

        self.chem_mass = self.active_mat_conc * self.application_rate * math.pow(10, -4)  ##chemical mass (g/m2)
        self.chem_dilrate = 0  ##chemical dilution rate (0%)

        # Support properties
        #supp_volume = self.supp_volume  # liters
        self.supp_density = self.cst.supp_dens(self.supportCarac)  # Water density

        # Field properties
        field_surface = 0.025  # ha

        if self.chem_dilrate != 0:
            self.chem_mass = self.chem_dilrate * self.supp_volume * (1000 * self.chem_density)

        ## Mixture properties
        self.rho_mix = self.cst.rho_mix(self.chem_mass, self.chem_dilrate, self.chem_density, self.supp_volume,
                              self.supp_density)  # Density of mixture
        # Volume of mixture
        self.vol_mix = self.supp_volume + (self.chem_mass / (1000 * self.chem_density))