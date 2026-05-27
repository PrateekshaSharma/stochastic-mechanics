# Uncertainty Propagation in Beam Deflection

## Overview

This project looks at what happens to beam deflection when the inputs are not fixed but uncertain. Instead of plugging in single values for load and elastic modulus, I treat them as random variables and run a Monte Carlo simulation to see the full range of possible deflection outcomes.

The formula used is the standard mid-span deflection for a simply supported beam under a central point load:

δ = P × L³ / (48 × E × I)

## Inputs

Load P is modeled as Normal with mean 50 kN and standard deviation 7.5 kN.
Elastic modulus E is modeled as Normal with mean 200 GPa and standard deviation 10 GPa.
Span L is fixed at 5.0 m and moment of inertia I is fixed at 2.5 × 10⁻⁴ m⁴.

## Results

Deterministic deflection : 2.6042 mm
Mean deflection from simulation : 2.6108 mm
Standard deviation : 0.4131 mm
95th percentile : 3.2982 mm
99th percentile : 3.6025 mm

