# Python Program to Calculate Resonance in RLC Circuit
# Resonant Frequency: fr = 1 / (2 * pi * sqrt(L * C))

import math

print("========================================")
print("       RLC CIRCUIT RESONANCE")
print("========================================")

# Input values
L = float(input("Enter inductance L (mH): "))
C = float(input("Enter capacitance C (uF): "))
R = float(input("Enter resistance R (ohm): "))

# Convert units
L = L / 1000       # mH to H
C = C / 1000000    # uF to F

# Calculate resonant frequency
fr = 1 / (2 * math.pi * math.sqrt(L * C))

# Calculate angular resonant frequency
omega_r = 2 * math.pi * fr

# Calculate quality factor for series RLC
Q = omega_r * L / R

# Calculate bandwidth
bandwidth = fr / Q

# Display results
print("\n------------- RESULTS ----------------")
print(f"Inductance              : {L:.6f} H")
print(f"Capacitance             : {C:.9f} F")
print(f"Resistance              : {R:.2f} ohm")
print(f"Resonant Frequency      : {fr:.2f} Hz")
print(f"Angular Frequency       : {omega_r:.2f} rad/s")
print(f"Quality Factor (Q)      : {Q:.2f}")
print(f"Bandwidth               : {bandwidth:.2f} Hz")
print("--------------------------------------")
