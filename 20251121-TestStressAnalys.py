import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


# -----------------------------
# 1. Input data (you can change)
# -----------------------------
L = 1.0          # Beam length [m]
P = 1000.0       # End load [N] (downward)
E = 210e9        # Young's modulus [Pa] (e.g., steel)
b = 0.02         # Rectangular cross-section width [m]
h = 0.04         # Rectangular cross-section height [m]

# Second moment of area for a rectangle about the neutral axis (b*h^3 / 12)
I = b * h**3 / 12.0

print(f"I = {I:.3e} m^4")

# -----------------------------
# 2. Discretize beam along x
# -----------------------------
n_points = 200
x = np.linspace(0, L, n_points)

# -----------------------------
# 3. Internal forces & moments
# -----------------------------
# Shear force (constant along beam for a tip load)
V = -P * np.ones_like(x)     # [N]

# Bending moment: M(x) = -P*(L - x)
M = -P * (L - x)             # [N·m]

# -----------------------------
# 4. Deflection (Euler–Bernoulli solution)
# y(x) = P x^2 (x - 3L) / (6 E I)
# sign convention: downward deflection is negative
# -----------------------------
y = P * x**2 * (x - 3*L) / (6 * E * I)  # [m]

# Tip deflection (should match analytical PL^3 / (3EI) in magnitude)
y_tip = y[-1]
print(f"Tip deflection = {y_tip:.3e} m (negative = downward)")

# -----------------------------
# 5. Bending stress at outer fiber
# sigma(x) = M(x) * c / I
# c = h/2 (distance from neutral axis to outer surface)
# -----------------------------
c = h / 2.0
sigma = M * c / I  # [Pa]
print(f"Max bending stress at the fixed end = {sigma[0]/1e6:.2f} MPa")

# -----------------------------
# 6. Plots
# -----------------------------

# Deflection plot
plt.figure()
plt.plot(x, y)
plt.xlabel("x [m]")
plt.ylabel("Deflection y(x) [m]")
plt.title("Cantilever Beam Deflection (end load)")
plt.grid(True)

# Bending moment diagram
plt.figure()
plt.plot(x, M)
plt.xlabel("x [m]")
plt.ylabel("Bending moment M(x) [N·m]")
plt.title("Cantilever Bending Moment Diagram")
plt.grid(True)

plt.show()
plt.savefig("deflection.png")
plt.savefig("moment.png")
