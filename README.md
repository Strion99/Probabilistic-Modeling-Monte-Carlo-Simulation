# Probabilistic-Modeling-Monte-Carlo-Simulation
Developed a statistical model using Bayesian Inference to calculate posterior probabilities and error rates (False/True Positives).  Executed Monte Carlo simulations (10,000 samples) to analyze probability densities and visualize Central Limit Theorem convergence.

Probabilities (Theoretical)

- Solve the following problems:
a. In a population of n couples, where each couple has exactly 2 kids. What is the
probability that all couples have 1 daughter and 1 son? (assume binary equi
probable genders)
b. You flip a fair (50-50 chance of each side) coin n times. What is the probability
that all n times you get Heads?
c. In a box, there are beads of 3 colours: red, green, and blue at percentages 30%,
50% and 20%. Half of the red, 2/3 of the blue, and 2/3 of the green beads are
hollow. Which is the probability of drawing a hollow bead by picking a random
bead from the box?

- Bayesian Theorem (Programming)

Include in your submission the python files that implement this exercise and show the
plots in your report. Do not forget to put labels on the axes.
a. A photon package emitted by a star has a probability of 1e-7 to pass through the
Earth’s atmosphere and reach a detector placed on the ground.
The detector has the following properties:
i) A false positive rate (= probability of incorrectly reporting the detection of
a photon package, when no photon package was actually received) of 10%.
ii) A true positive rate (= probability of correctly reporting the detection of a
photon package, when a photon package was actually received) of 85%.
Which is the probability that − if the detector reported a detection − a photon
package was actually received?
b. Assume that the photon package is composed of 100 photons. Each photon has an
equal probability [i.e. 25%] to carry an energy of either 10, 20, 30, or 40 electron
volts. That means that each package has photon energies roughly distributed
according to a uniform distribution in energy.
Which distribution the total energy of a package (i.e. the sum of the energies of
the photons composing a package) follows? Plot it. Does it look like a familiar
distribution? Why?
c. We will now assume that the photon package doesn’t simply have a defined prob
ability of 1e-7 to reach the ground. Instead, due to stochastic emission from the
star and interaction with the atmosphere, the probability density function for this
event is described by a normal distribution N (µ,σ) centered at µ = 1e-7, and
with σ = 9e-8.
The resulting probability that − if the detector reported a detection − a photon
package was actually received will now be a distribution (instead of a single value).
Plot such distribution. Does it make sense?
