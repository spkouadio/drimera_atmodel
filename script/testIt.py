import math
import random

import numpy as np
import scipy.special as sc

def windSpeedProfil(meanSpeed, timestep):
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

    for i in rand_u_step:
        x = math.pow((-1 * math.pow(c, k) * math.log(1 - i)), 1 / k)
        windSpeed_table = np.append(windSpeed_table, np.array([[x]]), axis=0)  # (m/s)

    return windSpeed_table

print(windSpeedProfil(5,80))

print(math.log(2))

