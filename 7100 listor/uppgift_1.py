import random
from collections import Counter

resultat = [random.randint(1, 6) for i in range(10)]
resultat.sort()
summa = sum(resultat)
medelvärde = summa / len(resultat)
minsta = min(resultat)
högsta = max(resultat)
räkna_sexor = resultat.count(6)
counter = Counter(resultat)
vanligast = counter.most_common(1)[0][0]

print("Resultat:", resultat)
print("Summan:", summa)
print("Medelvärde:", medelvärde)
print("Minsta:", minsta)
print("Högsta:", högsta)
print("Antal sexor:", räkna_sexor)
print("Vanligast:", vanligast)

