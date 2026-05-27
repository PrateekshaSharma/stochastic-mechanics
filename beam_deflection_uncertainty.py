# Uncertainty Propagation in Beam Deflection

This project propagates input uncertainty through the mid-span deflection formula for a simply supported beam under a central point load.

The deflection formula is:

δ = P * L³ / (48 * E * I)


Load P and elastic modulus E are treated as random variables with known means and standard deviations. Monte Carlo simulation is used to compute the full distribution of deflection outcomes.

## Parameters

 P — Point load ; Random ; Normal(50 kN, 7.5 kN) 
 E — Elastic modulus | Random | Normal(200 GPa, 10 GPa) 
L — Span; Fixed ; 5.0 m 
I — Moment of inertia ; Fixed ; 2.5 × 10⁻⁴ m⁴ 

## Results

Deterministic deflection : 2.6042 mm
Mean deflection          : 2.6108 mm
Standard deviation       : 0.4131 mm
95th percentile          : 3.2982 mm
99th percentile          : 3.6025 mm

## Output

![Beam Deflection Uncertainty](beam_deflection_uncertainty.png)




