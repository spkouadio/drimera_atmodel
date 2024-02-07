import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
rho_air = 1.225  # Density of air
mu_air = 1.8e-5  # Dynamic viscosity of air
rho_droplet = 1000.0  # Density of droplet
D_droplet = 1e-6  # Diameter of droplet
v_initial = 1.0  # Initial velocity of droplet
deposition_rate = 0.1  # Deposition rate

# Simulation parameters
L = 10  # Length of each dimension (cube)
N = 50  # Number of grid points along each dimension
dt = 0.01  # Time step
total_time = 5.0  # Total simulation time

# Initialize velocity field (assuming uniform airflow)
u = np.zeros((N, N, N)) + v_initial
v = np.zeros((N, N, N))
w = np.zeros((N, N, N))

# Initialize pressure field
p = np.zeros((N, N, N))

# Initialize droplet concentration field
C = np.zeros((N, N, N))
C[N // 2, N // 2, N // 2] = 1.0  # Initial concentration at center

# Initialize coordinates
x = np.linspace(0, L, N)
y = np.linspace(0, L, N)
z = np.linspace(0, L, N)

# Initialize figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Euler's method
for t in np.arange(0, total_time, dt):
    # Update velocity field (no pressure gradient term for simplicity)
    u += dt * (-u * np.gradient(u, axis=0) / rho_air + mu_air * np.gradient(np.gradient(u, axis=0), axis=0) / rho_air)
    v += dt * (-v * np.gradient(v, axis=1) / rho_air + mu_air * np.gradient(np.gradient(v, axis=1), axis=1) / rho_air)
    w += dt * (-w * np.gradient(w, axis=2) / rho_air + mu_air * np.gradient(np.gradient(w, axis=2), axis=2) / rho_air)

    # Update pressure field (simplified Poisson equation)
    p += dt * rho_air * (np.gradient(u, axis=0) + np.gradient(v, axis=1) + np.gradient(w, axis=2))

    # Compute droplet advection
    dC_dx, dC_dy, dC_dz = np.gradient(C, x, y, z)
    adv_x = -u * dC_dx
    adv_y = -v * dC_dy
    adv_z = -w * dC_dz

    # Update droplet concentration using Euler's method
    C += (adv_x + adv_y + adv_z) * dt

    # Apply deposition
    C -= deposition_rate * C * dt

    # Plot 3D surface
    ax.clear()
    X, Y, Z = np.meshgrid(x, y, z)
    ax.plot_surface(X, Y, Z, facecolors=plt.cm.jet(C / C.max()), rstride=1, cstride=1, alpha=0.5)
    ax.set_title(f'Time: {t:.2f}')
    plt.pause(0.01)

plt.show()

'''
# Define parameters
grid_size = 50
k = 2.0  # Weibull shape parameter
c = 8.0  # Weibull scale parameter

# Generate wind rose data (dummy data for example)
wind_directions = np.arange(0, 360, 45)  # Angles in degrees
wind_probabilities = [0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.1, 0.1]  # Corresponding probabilities at each direction

# Generate Weibull wind speeds based on probabilities
num_samples = 1000
wind_speeds = np.random.weibull(k, num_samples) * c

# Initialize velocity field
velocity_field_x = np.zeros((grid_size, grid_size))
velocity_field_y = np.zeros((grid_size, grid_size))

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
        velocity_field_x[i, j] = wind_vector_x
        velocity_field_y[i, j] = wind_vector_y

# Plot velocity field as an imshow plot
plt.figure(figsize=(10, 6))
plt.quiver(velocity_field_x, velocity_field_y, scale=20)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Airflow Velocity Field')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
'''