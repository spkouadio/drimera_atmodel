import numpy as np
from front import params

# Define parameters
nx = 101  # number of grid points
ny = 101
nt = 100  # number of time steps
dx = 0.1  # grid spacing
dy = 0.1
gamma = 1.4  # specific heat ratio
CFL = 0.1  # CFL number
p_inf = 10.1325  # free stream pressure
rho_inf = params.air_density #1.225  # free stream density
u_inf = 5  # free stream velocity

# Initialize arrays
u = np.zeros((nx, ny))  # x-velocity
v = np.zeros((nx, ny))  # y-velocity
p = np.ones((nx, ny)) * p_inf  # pressure
rho = np.ones((nx, ny)) * rho_inf  # density

# Set initial condition
u[:, :] = u_inf
p[:, :] = p_inf
rho[:, :] = rho_inf


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
    dt = CFL * min(dx / np.max(np.abs(u)), dy / np.max(np.abs(v)))

    # Calculate pressure from density and velocity
    p = (gamma - 1) * (rho * (u ** 2 + v ** 2) / 2 - p_inf)

    # Calculate density from pressure and velocity
    rho = p / ((gamma - 1) * (u ** 2 + v ** 2) / 2 + p_inf)

    # Calculate x-velocity
    u -= dt * ddt(p, u, v) / rho

    # Calculate y-velocity
    v -= dt * ddt(p, u, v) / rho

# Plot velocity field
#X, Y = np.meshgrid(np.linspace(0, dx * (nx - 1), nx), np.linspace(0, dy * (ny - 1), ny))
#plt.streamplot(X, Y, u, v)
#plt.show()
