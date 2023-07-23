r'''
Constants package
'''
import math
import numpy as np

class constants(object):
    # Gravity
    def g(self):
        return 9.18

    # Air density
    def rho_a(self, humid, temp):
        P = 101325  # air pressure (Pa)
        Rs = 287.06  # water vapor specifique constant
        rho = float(
            (1 / (Rs * (temp + 273.15))) * (P - 230.617 * humid * np.exp((17.5043 * temp) / (241.2 + temp))))
        return rho

    # Specific humidity
    def humid_spe(self, humid_rel, p_atmos, p_satur):
        h = 0.6217 * (humid_rel * p_satur) / (p_atmos - 0.3783 * humid_rel * p_satur)
        return h

    # Atmosperical pressure (Pa)
    def p_atm(self, alt):
        p_at = 101325 * math.pow(1 - 0.0000225577 * alt, 5.2554876)
        return p_at

    # Saturation water vapor pressure (Pa)
    def p_sat(self, temp):
        p_s = math.pow(10, 2.7862 + ((7.5526 * temp) / (239.21 + temp)))
        return p_s

    # Air dynamic viscosity
    def mu_a(self, temp):
        S = 110.4  # Kelvin
        b = 1.458 * math.pow(10, -6)
        mu = (b * math.pow(temp, 3 / 2)) / (temp + 273.15 + S)  # Sutherland Equation
        return mu

    # Mixture density
    def rho_mix_mass(self, chem_mass, chem_density, supp_volume, supp_density):
        rho_mix = float(
            (chem_mass + supp_density * supp_volume) / ((chem_mass / (1000 * chem_density)) + supp_volume))
        return rho_mix

    def rho_mix_vol(self, chem_dilrate, chem_density, supp_density):
        rho_mix = float(((chem_dilrate * chem_density) + supp_density) / (1 + chem_dilrate))
        return rho_mix

    def rho_mix(self, chem_mass, chem_dilrate, chem_density, supp_volume, supp_density):
        if chem_dilrate == '' or chem_dilrate == 0:
            return self.rho_mix_mass(chem_mass, chem_density, supp_volume, supp_density)
        else:
            return self.rho_mix_vol(chem_dilrate, chem_density, supp_density)

    # Chemical density in g/ml
    def rho_chem(self, chem):
        # chem_density = np.array((['Thiophanate-methyl', 1.45], ['Difenoconazole', 1.37], ['Epoxiconazole', 1.38],
        # ['Propiconazole', 1.09], ['Tebuconazole', 1.25], ['Fenpropimorph', 0.93],
        # ['Azoxystrobin', 1.34], ['Trifloxystrobin', 1.36]))
        chem_density = np.array((['Chlorothalonil', 0.00], ['Difenoconazol', 1.37], ['Dodin', 0.00],
                                 ['Epoxiconazol', 1.38], ['Fenpropimorph', 0.93], ['Mancozeb', 0.00],
                                 ['Propiconazol', 1.09], ['Pyraclostrobin', 0.00], ['Pyrimethanil', 0.00],
                                 ['Spiroxamin', 0.00], ['Thiram', 00], ['Tebuconazol', 1.25], ['Triadimefon', 0.00],
                                 ['Tridemorph', 0.00], ['Trifloxystrobin', 1.36]))
        d_chem = float(chem_density[np.where(chem_density[:, 0] == chem), 1])

        return d_chem

    # Droplet size caracteristic
    def drop_size(self, droplet):
        droplet_class = np.array((['Fog', 5], ['Very fine', 20], ['Fine', 100], ['Medium', 240], ['Coarse', 400],
                                  ['Fine rain', 1000]))
        d_droplet = float(droplet_class[np.where(droplet_class[:, 0] == droplet), 1])
        return d_droplet

    # Support caracteristic
    def supp_dens(self, supp):
        supp_density = np.array((['Water', 1], ['Oil', 0.9]))
        d_supp = float(supp_density[np.where(supp_density[:, 0] == supp), 1])
        return d_supp



