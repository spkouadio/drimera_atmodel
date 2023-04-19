r'''
Module for calculate droplets concentration in environment.
It takes as input, the droplet caracteristics generated by droplet_dispersal module and simulates the dispersion
of droplets in air using the Euler-Lagrange approach and the Finite Difference Method.
Pesticides concentration is then determinated.
'''


import numpy as np
import matplotlib.pyplot as plt

# Define parameters
nx = 101  # number of grid points
ny = 101
nt = 100  # number of time steps
dx = 0.1  # grid spacing
dy = 0.1
dt = 0.01  # time step
u = 1  # fluid velocity
D = 0.1  # diffusion coefficient
alpha = 0.5  # weighting factor for particle velocity

# Initialize arrays
c = np.zeros((nx, ny))  # concentration of particles
u_p = np.zeros((nx, ny))  # particle velocity in x-direction
v_p = np.zeros((nx, ny))  # particle velocity in y-direction

# Set initial condition
c[50, 50] = 1


# Define finite difference operator
def laplacian(c):
    lap = np.zeros_like(c)
    lap[1:-1, 1:-1] = (c[2:, 1:-1] - 2 * c[1:-1, 1:-1] + c[:-2, 1:-1]) / dx ** 2 \
                      + (c[1:-1, 2:] - 2 * c[1:-1, 1:-1] + c[1:-1, :-2]) / dy ** 2
    return lap


# Time loop
for n in range(nt):
    # Update particle velocity based on fluid velocity
    u_p = alpha * u + (1 - alpha) * u_p
    v_p = alpha * 0 + (1 - alpha) * v_p

    # Calculate particle diffusion
    c += dt * D * laplacian(c)

    # Calculate advection of particles
    c[1:-1, 1:-1] -= dt * u_p[1:-1, 1:-1] * (c[2:, 1:-1] - c[:-2, 1:-1]) / (2 * dx) \
                     + dt * v_p[1:-1, 1:-1] * (c[1:-1, 2:] - c[1:-1, :-2]) / (2 * dy)

    # Enforce boundary conditions
    c[:, 0] = 0
    c[:, -1] = 0
    c[0, :] = 0
    c[-1, :] = 0

    # Plot concentration profile
    if n % 10 == 0:
        plt.imshow(c, cmap='hot', origin='lower', extent=[0, 10, 0, 10])
        plt.colorbar()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Time = {n * dt:.2f}')
        plt.show()
