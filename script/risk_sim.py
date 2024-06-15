import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Define parameters and their probability distributions
num_simulations = 10000

# Exposure parameters
mean_exposure = 3.66154E-09 # Mean exposure level
std_dev_exposure = 4.07523E-17 # Standard deviation of exposure level

# Health impact parameters
mean_health_impact = 0.100 # Mean health impact per unit exposure
std_dev_health_impact = 0.05*mean_health_impact # Standard deviation of health impact

# Perform Monte Carlo simulation
exposure_samples = np.random.normal(mean_exposure, std_dev_exposure, num_simulations)
health_impact_samples = np.random.normal(mean_health_impact, std_dev_health_impact, num_simulations)

# Calculate risk
risk = exposure_samples / health_impact_samples

# Create histogram with seaborn for both exposure and health impact
fig, ax = plt.subplots(figsize=(10, 6))
"""ax2 = ax.twinx()
sns.histplot(risk, bins=50, ax=ax, kde=True)
sns.histplot(risk, bins=50, ax=ax2, stat="probability")

ax.set_xlabel('Risk distribution')
ax2.set_ylabel('Probability')
ax.set_ylabel('Frequency')
plt.tight_layout()"""

sns.histplot(risk, bins=200, ax=ax, stat='probability', element='step', color='gray')
ax.set_xlabel('Risk distribution')
plt.show()


