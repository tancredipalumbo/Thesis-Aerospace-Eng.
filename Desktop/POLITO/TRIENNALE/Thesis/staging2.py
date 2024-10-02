import math
from functools import reduce

#check=moltiplicatore di lagrange
def payloadFraction_opt(structuralRatio, c, check):
    return ((check*structuralRatio)/((1-structuralRatio)*(c-check)))

def deltaV_opt(structuralRatio, c, payload_fraction):
    return -(c*math.log(payload_fraction*(1-structuralRatio)+structuralRatio))

nStadi = int(input('Inserire il numero di stadi: '))
deltaV_req = float(input('Inserire la deltaV totale richiesta in Km/s: '))

lagrange = 1
deltaV_tot = []
payloadFraction_tot = []
c_stages = []
structRatio_stages = []
deltaVtot_plot = []
deltaV1_plot = []
deltaV2_plot = []
deltaV3_plot = []
lagrange_list = []

for i in range(nStadi):
    print('Stadio numero:', i + 1)
    c_j = float(input('Inserire la velocità efficace in Km/s: '))
    struct_ratio_j = float(input('Inserire lo structural ratio: '))
    c_stages.append(c_j)
    structRatio_stages.append(struct_ratio_j)

while not sum(deltaV_tot) == deltaV_req:
    for i in range(nStadi):
        payloadFraction_j = payloadFraction_opt(structRatio_stages[i], c_stages[i], round(lagrange, 5))
        deltaV_j = deltaV_opt(structRatio_stages[i], c_stages[i], payloadFraction_j)
        deltaV_tot.append(deltaV_j)
        payloadFraction_tot.append(payloadFraction_j)

    deltaV1_plot.append(deltaV_tot[0])
    deltaV2_plot.append(deltaV_tot[1])
    deltaV3_plot.append(deltaV_tot[2])
    lagrange_list.append(lagrange)
    deltaVtot_plot.append(sum(deltaV_tot))

    if round(sum(deltaV_tot), 4) > deltaV_req:
        lagrange = round(lagrange, 5)+0.00001
        deltaV_tot = []
        payloadFraction_tot = []

    elif round(sum(deltaV_tot), 4) < deltaV_req:
        lagrange = round(lagrange, 5)-0.00001
        deltaV_tot = []
        payloadFraction_tot = []

    elif round(sum(deltaV_tot), 4) == deltaV_req:
        for i in range(len(deltaV_tot)):
            print('Il deltaV ottimale per lo stadio', i+1, 'è', deltaV_tot[i], 'Km/s')
        payloadFraction_multiplied=reduce(lambda a, b: a * b, payloadFraction_tot)
        print('Lagrange:', lagrange)
        print('Le payload fraction per i singoli stadi saranno', payloadFraction_tot)
        print('Lambda tot:', payloadFraction_multiplied)
        break



                                     




