r'''
Droplet description module
'''

#import const as cst
import math
import numpy as np
#import params

class droplet_descr(object):
    def __init__(self, mean_diam, output_vol, rho_mix, vol_mix):
        # Chemical properties
        self.output_vol = output_vol  # (l/m) params.chem_mass
        self.rho_mix = rho_mix  # (g/l) params.rho_mix #Density of mixture
        self.vol_mix = vol_mix  # (l) params.vol_mix #Volume of mixture
        self.d_50 = mean_diam

    def init_velocity(self):
        r'''
        Droplets initial emission velocity is based on Bernoulli equation with some simplification hypothesis
        :return: initial velocity of droplets
        '''
        P = 10
        nu_e = 1
        V_0 = math.sqrt((2 * nu_e * P) / self.rho_mix)
        return V_0

    def drop_distrib(self):
        r'''
        Droplet distribution based on the log-normal distribution function
        :param mixt_volume: volume of the mixture that will be sprayed
        :return: drop_table that contains per line, the diameter of the droplet, with its volume fraction and the number of
        droplets of this diameter within, and the cumulative volume fraction
        '''
        n0 = 0.567
        sigma_g = 1.3
        #d_50 = 254.74  # micrometer µm
        d_inf = (1 - 0.8430) * self.d_50
        d_sup = (1 + 0.9623) * self.d_50
        f_cumul = 0
        drop_table = np.empty((0, 4), float)
        for d in np.arange(d_inf, d_sup, sigma_g):
            f = (n0 / (math.sqrt(2 * math.pi) * d * math.log10(sigma_g))) \
                * math.exp(-math.pow(math.log10(d / self.d_50), 2) / (2 * math.pow(math.log10(sigma_g), 2)))
            f_cumul = f_cumul + f
            n = f / (math.pow(d, 3) * (math.pi / 6))
            #drop_table = np.append(drop_table, np.array([[d, f * self.vol_mix, f_cumul, n]]), axis=0) # (l)
            drop_table = np.append(drop_table, np.array([[d, f * self.output_vol, f_cumul, n]]), axis=0) # (l)
        #test = sum(drop_table)
        #test2 = self.chem_mass
        #print(test, test2)
        return drop_table