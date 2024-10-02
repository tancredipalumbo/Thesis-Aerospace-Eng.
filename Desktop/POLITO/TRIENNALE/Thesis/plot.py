import matplotlib.pyplot as plt
from staging2 import deltaVtot_plot
from staging2 import lagrange_list
from staging2 import deltaV1_plot
from staging2 import deltaV2_plot
from staging2 import deltaV3_plot

plt.plot(lagrange_list, deltaVtot_plot, label='ΔV totale', linestyle='-', color='orange')
plt.plot(lagrange_list, deltaV1_plot, label='ΔV stadio 1', linestyle='-', color='blue')
plt.plot(lagrange_list, deltaV2_plot, label='ΔV stadio 2', linestyle='-', color='red')
plt.plot(lagrange_list, deltaV3_plot, label='ΔV stadio 3', linestyle='-', color='pink')

plt.title('Ottimizzazione di Lagrange per RP1-LOX/LH2-LOX/LCH4-LOX')
plt.xlabel('Moltiplicatore di Lagrange')
plt.ylabel('ΔV in Km/s')
plt.legend(loc='best')


plt.show()