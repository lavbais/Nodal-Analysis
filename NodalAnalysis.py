import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# NODAL ANALYSIS
# ============================================================
# This project evaluates well performance using:
# 1. Inflow Performance Relationship (IPR)
# 2. Tubing Performance Relationship (TPR)
# 3. Comparison of different tubing sizes
# ============================================================


# ------------------------------------------------------------
# 1. IPR DATASET
# ------------------------------------------------------------
# Source: PetroWiki

Q_IPR = [0, 1999, 3094, 3902, 4512, 4963, 5275, 5458, 5519]

Pwf_IPR = [4000, 3500, 3000, 2500, 2000, 1500, 1000, 500, 14.7]

DF_IPR = pd.DataFrame({
    'Pwf (psi)': Pwf_IPR,
    'Flow Rate (bbl/d)': Q_IPR
})

print("\nIPR Dataset:")
print(DF_IPR)


# ------------------------------------------------------------
# 2. IPR CURVE
# ------------------------------------------------------------

x_IPR = Q_IPR
y_IPR = Pwf_IPR

plt.figure(figsize=(10, 6))

plt.plot(
    x_IPR,
    y_IPR,
    linewidth=2.5,
    label='IPR'
)

plt.xlabel('Production Rate (bbl/d)')
plt.ylabel('Flowing Bottom-Hole Pressure (psi)')
plt.title('Inflow Performance Relationship (IPR)')
plt.grid(True)
plt.legend()
plt.show()


# ------------------------------------------------------------
# 3. TPR DATASET
# ------------------------------------------------------------
# Source: PetroWiki

Q_TPR = np.arange(1000, 6500, 500)

P_T190 = [
    1334, 1400, 1487, 1592, 1712,
    1843, 1984, 2132, 2287, 2446, 2689
]

P_T2375 = [
    1298, 1320, 1351, 1390, 1435,
    1487, 1545, 1609, 1677, 1749, 1824
]

P_T2875 = [
    1286, 1294, 1305, 1319, 1336,
    1356, 1378, 1403, 1431, 1461, 1493
]

DF_TPR = pd.DataFrame({
    'Flow Rate': Q_TPR,
    'TPR - 1.90 in': P_T190,
    'TPR - 2.375 in': P_T2375,
    'TPR - 2.875 in': P_T2875
})

print("\nTPR Dataset:")
print(DF_TPR)


# ------------------------------------------------------------
# 4. NODAL ANALYSIS
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

# IPR curve
plt.plot(
    Q_IPR,
    Pwf_IPR,
    label='IPR',
    linewidth=2.5
)

# TPR curves for different tubing sizes
plt.plot(
    Q_TPR,
    P_T190,
    label='TPR at 1.90 in tubing',
    linewidth=2.5
)

plt.plot(
    Q_TPR,
    P_T2375,
    label='TPR at 2.375 in tubing',
    linewidth=2.5
)

plt.plot(
    Q_TPR,
    P_T2875,
    label='TPR at 2.875 in tubing',
    linewidth=2.5
)

plt.xlabel('Production Rate')
plt.ylabel('Flowing Bottom-Hole Pressure (psi)')
plt.title('Nodal Analysis')

plt.legend(loc='best')
plt.grid(True)

plt.show()
