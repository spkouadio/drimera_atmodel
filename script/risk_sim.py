import random
import numpy as np
import matplotlib.pyplot as plt

def bootstrap_sample(data, sample_size):
  """
  Samples data with replacement to create a bootstrap sample.

  Args:
      data: A list of initial values.
      sample_size: The number of values to sample.

  Returns:
      A list containing the bootstrap sample.
  """
  return random.choices(data, k=sample_size)

def monte_carlo_simulation(initial_values, num_simulations, simulation_function):
  """
  Performs Monte Carlo simulation using bootstrapped initial values.

  Args:
      initial_values: A list of initial values.
      num_simulations: The number of simulations to run.
      simulation_function: A function that takes a single value and returns the simulated outcome.

  Returns:
      A list containing the simulated outcomes.
  """
  bootstrap_samples = [bootstrap_sample(initial_values, len(initial_values)) for _ in range(num_simulations)]
  simulated_outcomes = [simulation_function(sample) for sample in bootstrap_samples]
  return simulated_outcomes

def plot_cdf(data, display_value=None):
  """
  Plots the cumulative density function (CDF) of the data with optional highlighting and display of a specific value.

  Args:
      data: A list of data points.
      title: The title for the plot (default: "Health Risk CDF").
      highlight_value: The y-axis value to highlight (optional).
      display_value: The x-axis value to display with its corresponding y-value (optional).
  """
  sorted_data = np.sort(data)
  y_vals = np.arange(len(sorted_data)) / (len(sorted_data) - 1)
  plt.plot(sorted_data, y_vals)
  plt.xlabel("Dose value (µg/l)")
  plt.ylabel("Cumulative Probability")
  #plt.title(title)
  #plt.grid(True)

  # Display specific value if provided
  if display_value is not None:
      try:
          idx = np.searchsorted(sorted_data, display_value)
          if 0 <= idx < len(sorted_data):
              x = sorted_data[idx]
              y = y_vals[idx]
              plt.text(x*1.2, y*0.8, f"X={round(x,3)}, Y={round(y,3)}", fontsize=9)
              plt.plot([x, x], [0, y], color='gray', linewidth=1.5, linestyle="--")
              plt.plot([0, x], [y, y], color='gray', linewidth=1.5, linestyle="--")
              plt.scatter([x, ], [y, ], 10, color='gray')
      except ValueError:
          print(f"Error: X-value {display_value} not found in data.")

  plt.show()

def your_simulation_function(sample):
  """
  **Replace this function with your actual health risk simulation logic.**

  This function should take a single value (representing a bootstrapped sample)
  and return the simulated health risk score.

  For example, it could perform calculations based on the sample values
  and return a health risk score.
  """
  # Replace with your specific simulation logic
  # This example simply returns the average of the sample
  return np.mean(sample)

if __name__ == "__main__":
  # Replace these with your actual initial health risk values
  initial_values = [0, 8.33333E-10, 8.20267E-09]
  num_simulations = 10000

  # Perform Monte Carlo simulation with bootstrapping
  simulated_outcomes = monte_carlo_simulation(initial_values, num_simulations, your_simulation_function)

  # Specify the x-axis value to display (optional)
  VTR = 1.20  # Replace with VTR

  # Plot the CDF with highlighting and display
  plot_cdf(simulated_outcomes, display_value=VTR)