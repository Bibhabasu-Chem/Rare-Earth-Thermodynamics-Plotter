import matplotlib.pyplot as plt
import numpy as np

# Data extracted from MSc Dissertation (Table 2)
metals = ['La', 'Ce', 'Pr', 'Eu', 'Yb']
sound_velocities = [1462.48, 618.5, 923.29, 1205.61, 1164.47]
compressibilities = [9.68, 39.77, 23.00, 14.92, 13.14]

fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot Sound Velocity
color = 'tab:blue'
ax1.set_xlabel('Rare Earth Liquid Metals', fontsize=12)
ax1.set_ylabel('Sound Velocity (m/s)', color=color, fontsize=12)
ax1.plot(metals, sound_velocities, marker='o', color=color, linewidth=2, label='Sound Velocity')
ax1.tick_params(axis='y', labelcolor=color)

# Create a second y-axis for Compressibility
ax2 = ax1.twinx()  
color = 'tab:red'
ax2.set_ylabel('Isothermal Compressibility (10^-11 m^2/N)', color=color, fontsize=12)
ax2.plot(metals, compressibilities, marker='s', color=color, linestyle='--', linewidth=2, label='Compressibility')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Acoustic & Thermodynamic Trends in Rare Earth Melts', fontsize=14)
fig.tight_layout()
plt.grid(True, alpha=0.3)
plt.show()
