r'''
Air_flow module are based on the Eulerian approach solving the Navier-Stokes equations.
Velocity field is initialized with a constant free stream velocity u_inf and then solves the Euler equations
using a finite difference method to calculate the velocity field at each point on the grid.
'''
import math
import numpy as np
import random
import scipy.special as sc

class air_flow(object):
    def __init__(self, meanSpeed, timestep):

        sigma = 0.25 * meanSpeed
        # calculate the k index
        k = math.pow(sigma / meanSpeed, -1.086)
        # calculate the c index
        gamma_f = math.exp(sc.gammaln(1 + (1 / k)))
        c = (meanSpeed / gamma_f)
        u_step = 1 / timestep
        # randomly create u[0, 1] uniform values
        #rand_u_step = random.sample([i for i in np.arange(0, 1, u_step)], timestep)
        #wind_speeds = np.empty((0, 1), float)

        # wind speed generation
        #wind_speeds = []
        #for i in np.arange(0, 1, u_step):
        #    wind_speeds.append(math.pow((-1 * math.pow(c, k) * math.log(1 - i)), 1 / k)) # (m/s)
        # Define parameters
        grid_size = 201
        #k = 2.0  # Weibull shape parameter
        #c = 8.0  # Weibull scale parameter

        # Generate wind rose data (dummy data for example)
        wind_directions = np.arange(0, 360, 45)  # Angles in degrees
        wind_probabilities = [0.5, 0.1, 0.06, 0.06, 0.06, 0.06, 0.06, 0.1]  # Corresponding probabilities at each direction
        #[0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.1, 0.1]

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
'''
import numpy as np

class air_flow(object):
    def __init__(self, timestep, gamma, p_inf, rho_inf, u_inf):
        self.gamma = gamma # air specific heat ratio
        self.p_inf = p_inf # free stream pressure
        self.rho_inf = rho_inf # free stream density
        self.u_inf = u_inf # free stream velocity

        # Define parameters
        self.nx = 101  # number of grid points
        self.ny = 101
        self.nt = timestep  # number of time steps
        dx = 0.1  # grid spacing
        dy = 0.1
        CFL = 0.1  # CFL number

        # Initialize arrays
        self.u = np.zeros((self.nx, self.ny))  # x-velocity
        self.v = np.zeros((self.nx, self.ny))  # y-velocity
        p = np.ones((self.nx, self.ny)) * self.p_inf  # pressure
        rho = np.ones((self.nx, self.ny)) * self.rho_inf  # density

        # Set initial condition
        self.u[:, :] = self.u_inf
        p[:, :] = self.p_inf
        rho[:, :] = self.rho_inf

        # Define finite difference operator
        def ddt(f, u, v):
            dfdt = np.zeros_like(f)
            dfdx = np.zeros_like(f)
            dfdy = np.zeros_like(f)

            dfdx[1:-1, 1:-1] = (f[2:, 1:-1] - f[:-2, 1:-1]) / (2 * dx)
            dfdy[1:-1, 1:-1] = (f[1:-1, 2:] - f[1:-1, :-2]) / (2 * dy)

            dfdt[1:-1, 1:-1] = - u[1:-1, 1:-1] * dfdx[1:-1, 1:-1] \
                               - v[1:-1, 1:-1] * dfdy[1:-1, 1:-1]

            return dfdt

        # Time loop
        for n in range(self.nt):
            # Calculate time step
            dt = CFL * min(dx / np.max(np.abs(self.u)), dy / np.max(np.abs(self.v)))

            # Calculate pressure from density and velocity
            p = (self.gamma - 1) * (rho * (self.u ** 2 + self.v ** 2) / 2 - self.p_inf)

            # Calculate density from pressure and velocity
            rho = p / ((self.gamma - 1) * (self.u ** 2 + self.v ** 2) / 2 + self.p_inf)

            # Calculate x-velocity
            self.u -= dt * ddt(p, self.u, self.v) / rho

            # Calculate y-velocity
            self.v -= dt * ddt(p, self.u, self.v) / rho
'''