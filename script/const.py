r'''
Constants package
'''
import math
import numpy as np
import random
import scipy.special as sc

class constants(object):
    # Initial chemical list
    def chemical(self):
        chem_list = np.array((['Banko 720 SC', 'Chlorothalonil', 720, 0.00], ['Sico 250 EC', 'Difenoconazol', 250, 1.37],
                              ['Syllit 400 SC', 'Dodin', 400, 0.00], ['Opal 7.5 EC', 'Epoxiconazol', 75, 1.38],
                              ['Volley 88 OL', 'Fenpropimorph', 750, 0.93], ['Ivory 80 WP', 'Mancozeb', 800, 0.00],
                              ['Tilt 250 EC', 'Propiconazol', 250, 1.09], ['Cabrio EG', 'Pyraclostrobin', 000, 0.00],
                              ['Siganex 600 SC', 'Pyrimethanil', 600, 0.00], ['Impulse 075 EC', 'Spiroxamin', 800, 0.00],
                              ['Thiram 75 WP', 'Thiram', 750, 0.00], ['Folicur 250 EW-Junior', 'Tebuconazol', 250, 1.25],
                              ['Trical 250 EC', 'Triadimefon', 250, 0.00], ['Calixine 75 EC', 'Tridemorph', 750, 0.00],
                              ['Téga 075 EC', 'Trifloxystrobin', 75, 1.36], ['Callis 400 OL', 'Thiophanate-methyl', 400, 1.45],
                              ['Bankit 25 SC', 'Azoxystrobin', 250, 1.34]))
        return chem_list

    # Initial carrier
    def carrier(self):
        supp_list = np.array((['Water', 1, 'water at 25°C'], ['Oil', 0.9, 'natural oil at 25°C']))
        return supp_list

    # Initial diameter by Herbicide spray drift, NDSU Extension (µm)
    def dropletClass(self):
        diam_list = np.array((['Fog', 50], ['Very fine', 20], ['Fine', 100], ['Medium', 240],
                              ['Coarse', 400], ['Fine rain', 1000]))
        return diam_list

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
    def rho_mix(self, pest_density, pest_volume, supp_density, supp_volume):
        rho_mix = float(((pest_density * pest_volume) + (supp_density * supp_volume)) / (pest_volume + supp_volume))
        return rho_mix

    # Chemical density in g/l
    def rho_chem(self, chem):
        chem_list = self.chemical
        d_chem = float(chem_list[np.where(chem_list[:, 1] == chem), 3])

        return d_chem

    # Droplet size caracteristic
    def drop_size(self, droplet):
        droplet_class = np.array((['Fog', 5], ['Very fine', 20], ['Fine', 100], ['Medium', 240], ['Coarse', 400],
                                  ['Fine rain', 1000]))
        d_droplet = float(droplet_class[np.where(droplet_class[:, 0] == droplet), 1])
        return d_droplet

    # Support caracteristic
    def supp_dens(self, supp):
        supp_list = self.carrier
        d_supp = float(supp_list[np.where(supp_list[:, 0] == supp), 1])
        return d_supp

    def windSpeedProfil(self, meanSpeed, timestep):
        '''
        WInd speed profil obtain with Weibull distribution
        :param meanSpeed: mean speed enter by user
        :param timestep: timestep of simulation enter by user
        :return: a wind speed profil table
        '''
        sigma = 0.25 * meanSpeed
        # calculate the k index
        k = math.pow(sigma / meanSpeed, -1.086)
        # calculate the c index
        gamma_f = math.exp(sc.gammaln(1 + (1 / k)))
        c = (meanSpeed / gamma_f)
        u_step = 1 / timestep
        # randomly create u[0, 1] uniform values
        rand_u_step = random.sample([i for i in np.arange(0, 1, u_step)], timestep)
        windSpeed_table = np.empty((0, 1), float)
        # wind speed generation
        for i in rand_u_step:
            x = math.pow((-1 * math.pow(c, k) * math.log(1 - i)), 1 / k)
            windSpeed_table = np.append(windSpeed_table, np.array([[x]]), axis=0)  # (m/s)
        return windSpeed_table

    # Wind rose initial value
    def roseValue(self):
        rose_val = np.array((['N', 0.5], ['NE', 0.1], ['E', 0.06], ['SE', 0.06], ['S', 0.06],
                                  ['SW', 0.06], ['W', 0.06], ['NW', 0.1]))
        return rose_val
