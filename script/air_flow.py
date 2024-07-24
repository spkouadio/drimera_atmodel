r'''
Air_flow module are based on Weibull Law coupled with the Wind Rose.
A Mean Speed is used to determinate Weibull's k and c parameters and then, calculate wind speeds.
Based on probabilities at each direction on the Wind Rose, a velocity field is randomly generate on the grid.
'''
import math
import numpy as np
import scipy.special as sc

class air_flow(object):
    def __init__(self, meanSpeed, timestep):

        sigma = 0.25 * meanSpeed
        # calculate the k index
        k = math.pow(sigma / meanSpeed, -1.086)
        # calculate the c index
        gamma_f = math.exp(sc.gammaln(1 + (1 / k)))
        c = (meanSpeed / gamma_f)
        grid_size = 201

        # Generate wind rose data (dummy data for example)
        wind_directions = np.arange(0, 360, 45)  # Angles in degrees
        wind_probabilities = [0.5, 0.1, 0.06, 0.06, 0.06, 0.06, 0.06, 0.1]  # Corresponding probabilities at each direction

        # Generate Weibull wind speeds based on probabilities
        num_samples = 100
        wind_speeds = np.random.weibull(k, num_samples) * c

        # Initialize velocity field
        self.velocity_field_x = np.zeros((grid_size, grid_size))
        self.velocity_field_y = np.zeros((grid_size, grid_size))
        self.velocity_value = np.zeros((grid_size, grid_size))

        # Populate velocity field based on wind rose and Weibull distribution
        for i in range(grid_size):
            for j in range(grid_size):
                # Randomly sample wind direction and speed
                idx = np.random.choice(len(wind_directions), p=wind_probabilities)
                wind_direction = wind_directions[idx]
                wind_speed = np.random.choice(wind_speeds)

                # Convert wind vector to cartesian coordinates
                wind_vector_x = np.cos(np.deg2rad(wind_direction)) * wind_speed
                wind_vector_y = np.sin(np.deg2rad(wind_direction)) * wind_speed

                # Assign wind velocity to the grid cell
                self.velocity_field_x[i, j] = wind_vector_x
                self.velocity_field_y[i, j] = wind_vector_y
                self.velocity_value[i, j] = wind_speed
