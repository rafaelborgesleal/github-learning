import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------
# Beam and load information
# ---------------------------------------------------
L = 1.0          # Beam length [m]
F = 1000.0       # Load magnitude [N]
a = 0.7 * L      # Load position from the fixed end [m]
b = L - a        # Remaining length

# Discretize
x = np.linspace(0, L, 300)

# ---------------------------------------------------
# Shear force diagram V(x)
# ---------------------------------------------------
V = np.zeros_like(x)
mask = x <= a
V[mask] = -F       # constant up to load point
V[~mask] = 0       # zero after load point (already zero, but explicit)

# ---------------------------------------------------
# Bending moment M(x)
# M(x) = -F * (a - x) for x <= a
# M(x) = 0           for x > a
# ---------------------------------------------------
M = np.zeros_like(x)
M[mask] = -F * (a - x[mask])

# ---------------------------------------------------
# 1) LOAD DIAGRAM
# ---------------------------------------------------
plt.figure(figsize=(8, 2))
plt.plot(x, np.zeros_like(x), 'k-', linewidth=3)
plt.arrow(a, 0.0, 0, -0.3,
          head_width=0.03,
          head_length=0.05,
          length_includes_head=True,
          color='red')
plt.text(a, -0.33, f"F = {F:.1f} N", ha='center', color='red')

plt.title("Load Diagram – Cantilever with Point Load at x = a")
plt.xlabel("Beam Length [m]")
plt.yticks([])
plt.ylim(-0.5, 0.5)
plt.savefig("load_point.png", dpi=300, bbox_inches='tight')
plt.close()

# ---------------------------------------------------
# 2) SHEAR FORCE DIAGRAM
# ---------------------------------------------------
plt.figure(figsize=(8, 2))
plt.plot(x, V, color='green')
plt.axhline(0, color='black', linewidth=0.8)
plt.title("Shear Force Diagram V(x)")
plt.xlabel("Beam Length [m]")
plt.ylabel("V(x) [N]")
plt.grid(True)
plt.savefig("shear_point.png", dpi=300, bbox_inches='tight')
plt.close()

# ---------------------------------------------------
# 3) BENDING MOMENT DIAGRAM
# ---------------------------------------------------
plt.figure(figsize=(8, 2))
plt.plot(x, M, color='brown')
plt.axhline(0, color='black', linewidth=0.8)
plt.title("Bending Moment Diagram M(x)")
plt.xlabel("Beam Length [m]")
plt.ylabel("M(x) [N·m]")
plt.grid(True)
plt.savefig("moment_point.png", dpi=300, bbox_inches='tight')
plt.close()

print("Saved: load_point.png, shear_point.png, moment_point.png")
