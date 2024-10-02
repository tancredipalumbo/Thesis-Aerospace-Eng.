import math
from staging2 import c_stages
from staging2 import structRatio_stages
from staging2 import nStadi
from staging2 import deltaV_tot
from staging2 import payloadFraction_tot
def mf_i(deltaV_j, c_j, mi_j):
    return mi_j*math.e**(-deltaV_j/c_j)
def mp_i(mi_j, mf_j):
    return mi_j-mf_j
def ms_i(struct, mp):
    return ((struct*mp)/(1-struct))

m0 = 2500000
m_i = 2500000
mf_stages = []
mp_stages = []
ms_stages = []
mi_stages = []
mu_stages = []
frac_1 = []
frac_2 = []
frac_3 = []
frac_4 = []
frac_5 = []


for i in range(nStadi):
    mf_j = mf_i(deltaV_tot[i], c_stages[i], m_i)
    mf_stages.append(mf_j)
    mp_j = mp_i(m_i, mf_j)
    mp_stages.append(mp_j)
    ms_j = ms_i(structRatio_stages[i], mp_j)
    ms_stages.append(ms_j)
    mi_stages.append(m_i)
    mu_j = payloadFraction_tot[i] * m_i
    mu_stages.append(mu_j)
    m_i = mu_j

for i in range(nStadi):
    frac_1.append(mi_stages[i]/m0)
    frac_2.append(mf_stages[i]/m0)
    frac_3.append(mp_stages[i]/m0)
    frac_4.append(ms_stages[i]/m0)
    frac_5.append(mu_stages[i]/m0)

print('Massa strutturale totale su massa iniziale a pieno carico:', sum(frac_4))
print('Frazioni di propellente:', frac_3)
print('Rapporto masse iniziali:', frac_1)
print('Rapporto masse finali:', frac_2)







