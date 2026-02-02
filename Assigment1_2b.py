import numpy as np
import matplotlib.pyplot as plt

# Define the possible energies for each photon
photon_energies = [10, 20, 30, 40]

# Variables for 100 photons
num_packages_100 = 100
total_energies_100 = []

# Variables for 2000 photon packages
num_packages_2000 = 2000
total_energies_2000 = []

#Calculations for 100 photons packages
for _ in range(num_packages_100):
    package_energy = np.sum(np.random.choice(photon_energies, size=num_packages_100))
    total_energies_100.append(package_energy)


# Calculations for 2000 photons
for _ in range(num_packages_2000):
    # Randomly choose 2000 photon energies and sum them up
    package_energy = np.sum(np.random.choice(photon_energies, size=num_packages_2000))
    total_energies_2000.append(package_energy)

# Plot the histogram for 100 packages
plt.figure(figsize=(8,6))
plt.hist(total_energies_100, bins=20, density=True, alpha=0.75, color='green')
plt.title('Distribution of Total Energies of 100 Photon Packages')
plt.xlabel('Total Energy (eV)')
plt.ylabel('Probability Density')
plt.grid(True)
plt.show()

# Plot for 2000 packages (already simulated)
plt.figure(figsize=(8,6))
plt.hist(total_energies_2000, bins=30, density=True, alpha=0.75, color='blue')
plt.title('Distribution of Total Energies of 2000 Photon Packages')
plt.xlabel('Total Energy (eV)')
plt.ylabel('Probability Density')
plt.grid(True)
plt.show()

