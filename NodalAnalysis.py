import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inline

# IPR Dataset (Source: Petrowiki)
# The following data represents the relationship between
# flowing bottom-hole pressure and production rate.

Q_IPR= [0,1999,3094,3902,4512,4963,5275,5458,5519]
Pwf_IPR= [4000,3500,3000,2500,2000,1500,1000,500,14.7]

# The IPR data is arranged in a DataFrame for analysis.
DF_IPR= pd.DataFrame({'Pwf':Pwf_IPR, 'q':Q_IPR})

DF_IPR

# Preparing the production rate and flowing pressure data
# for plotting the IPR curve.

x_IPR= Q_IPR
y_IPR= Pwf_IPR

# Plotting the IPR curve to visualize well inflow performance.

plt.plot(x_IPR,y_IPR)
plt.xlabel('Q_IPR(bbl/d)')
plt.ylabel('Pwf_IPR(psi)')
plt.title('IPR Curve')
plt.figure(figsize=(10,6))
plt.style.use('classic')

# TPR Dataset (Source: Petrowiki)
# TPR data is considered for three different tubing sizes:
# 1.90 inch, 2.375 inch and 2.875 inch.

Q_TPR= np.arange(1000,6500,500)
P_T190=[1334,1400,1487,1592,1712,1843,1984,2132,2287,2446,2689]
P_T2375=[1298,1320,1351,1390,1435,1487,1545,1609,1677,1749,1824]
P_T2875=[1286,1294,1305,1319,1336,1356,1378,1403,1431,1461,1493]

# Organizing the TPR data into a DataFrame for comparison.

DF_TPR= pd.DataFrame({'Q':Q_TPR, 'P190':P_T190, 'P2375':P_T2375, 'P2875':P_T2875})

DF_TPR

# Production-rate data used for plotting the TPR curves.

x_TPR= Q_TPR

# Combining the IPR and TPR curves to perform nodal analysis.
# The curves are compared for different tubing sizes.

plt.plot(Q_IPR,Pwf_IPR,label='IPR',linewidth='2.5')
plt.plot(Q_TPR,P_T190,label='TPR at 1.90in tubing',linewidth='2.5')
plt.plot(Q_TPR,P_T2375,label='TPR at 2.375in tubing',linewidth='2.5')
plt.plot(Q_TPR,P_T2875,label='TPR at 2.875in tubing',linewidth='2.5')

# Adding labels, title and legend to the final nodal analysis plot.

plt.xlabel('Q(MMscf/d)')
plt.ylabel('Flowing BHP(psi)')
plt.title('Nodal Analysis')
plt.legend(loc='best')
plt.style.use('classic')
