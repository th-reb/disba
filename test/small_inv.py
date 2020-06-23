import numpy as np
import matplotlib.pyplot as plt

from disba import PhaseDispersion, GroupDispersion

# Velocity model
# thickness, Vp, Vs, density
# km, km/s, km/s, g/cm3
velocity_model = np.array([
                    [0.5, 1.0, 0.5, 1.8],
                    [0.3, 2.0, 1.0, 1.8],
                    [10.0, 1.0, 0.5, 1.8],
                ])

pd = PhaseDispersion(*velocity_model.T, algorithm="fast-delta", dc=0.001)
gd = GroupDispersion(*velocity_model.T, algorithm="fast-delta", dc=0.001)

# Periods must be sorted starting with low periods
f = np.linspace(0.1, 10.0, 100)

# Compute the 20 first Rayleigh- and Love- waves modal dispersion curves
# Fundamental mode corresponds to mode 0
group_modes = [gd(f, mode=i, wave="rayleigh", x_axis="frequency") for i in range(20)]
phase_modes =  [pd(f, mode=i, wave="rayleigh", x_axis="frequency") for i in range(20)]

relevant = group_modes[0]
relevant_phase = phase_modes[0]
print(relevant.velocity.shape, relevant.x.shape)
plt.plot(relevant.x, relevant.velocity)
plt.plot(relevant_phase.x, relevant_phase.velocity)

###Ca marche pas car fonction de dispersion:  c=f(t) et pas f(w)
diff = np.gradient(relevant_phase.velocity, np.abs(f[1] - f[0]) )
group_diff = relevant_phase.velocity  + f * diff
plt.plot(relevant_phase.x, group_diff)

plt.show()
