r'''
Parameter lists for imput
'''
import math
from script.const import constants #import const as cst

class inputs_par(object):
    def __init__(self, activeMatConcent, pesticideDensity, pestVol, carrierDens, carrierVol, dropletSize, boomHeight, appRate,
                 residualConc, windSpeed, temperature, humidity, timeStep):

        #self.chem = activeMatCarac
        #self.supportCarac = supportCarac
        self.dropletSize = dropletSize

        self.chem_concent = activeMatConcent
        self.pesticide_density = pesticideDensity
        self.carrier_density = carrierDens
        self.pesticide_volume = pestVol
        self.carrier_volume = carrierVol
        self.boomHeight = boomHeight
        self.application_rate = appRate
        self.resConcentration = residualConc #Pas encore utliser !!!
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

        # Field properties
        #field_surface = 0.025  # ha

        # Mixture properties
        ## Density of mixture
        self.rho_mix = self.cst.rho_mix(self.pesticide_density, self.pesticide_volume, self.carrier_density, self.carrier_volume)
        ## Volume of mixture
        self.vol_mix = self.carrier_volume + self.pesticide_volume

        # Chemical properties
        ##chemical mass (g/m2)
        self.chem_mass = ((self.chem_concent * self.pesticide_volume)/self.vol_mix) * self.application_rate * math.pow(10, -4)