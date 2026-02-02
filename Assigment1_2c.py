import numpy as np  
import matplotlib.pyplot as plt
# Parameters for the normal distribution N(µ, σ)
mu = 1e-7
sigma = 9e-8

# Number of samples to draw from the normal distribution
num_samples = 10000

# Randomly sample from N(µ, σ) and reject negative values
photon_probabilities = []
for _ in range(num_samples):
    sample = np.random.normal(mu, sigma)
    if sample > 0:  # Only accept positive probabilities
        photon_probabilities.append(sample)

# Now we calculate the posterior probability for each sampled probability using Bayes' formula
false_positive_rate = 0.10
true_positive_rate = 0.85
prior_prob_neg = 1 - np.array(photon_probabilities)

posterior_probabilities = [
    (true_positive_rate * prob) / ((true_positive_rate * prob) + (false_positive_rate * (1 - prob)))
    for prob in photon_probabilities
]

# Plot the histogram of the resulting probabilities
plt.figure(figsize=(8,6))
plt.hist(posterior_probabilities, bins=30, density=True, alpha=0.75, color='purple')
plt.title('Distribution of Probabilities of Package Reception')
plt.xlabel('Probability')
plt.ylabel('Density')
plt.grid(True)
plt.show()
