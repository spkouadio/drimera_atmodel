r'''
Air_flow module are based on the Eulerian approach solving the Navier-Stokes equations.
Velocity field is initialized with a constant free stream velocity u_inf and then solves the Euler equations
using a finite difference method to calculate the velocity field at each point on the grid.
'''


import numpy as np

class air_flow(object):
    def __init__(self, gamma, p_inf, rho_inf, u_inf):
        self.gamma = gamma # air specific heat ratio
        self.p_inf = p_inf # free stream pressure
        self.rho_inf = rho_inf # free stream density
        self.u_inf = u_inf # free stream velocity

        # Define parameters
        nx = 101  # number of grid points
        ny = 101
        nt = 100  # number of time steps
        dx = 0.1  # grid spacing
        dy = 0.1
        CFL = 0.1  # CFL number

        # Initialize arrays
        self.u = np.zeros((nx, ny))  # x-velocity
        self.v = np.zeros((nx, ny))  # y-velocity
        p = np.ones((nx, ny)) * self.p_inf  # pressure
        rho = np.ones((nx, ny)) * self.rho_inf  # density

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
        for n in range(nt):
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