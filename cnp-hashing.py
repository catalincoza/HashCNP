import random
import calendar
import matplotlib.pyplot as plt
import numpy as np


def genereaza_cifra_control(cnp_fara_control):
    constanta = "279146358279"
    suma = sum(int(cnp_fara_control[i]) * int(constanta[i]) for i in range(12))
    cifra_control = suma % 11
    return cifra_control if cifra_control < 10 else 1


def genereaza_cnp():
    # S (Sex și secol)
    S = random.choice([1, 2, 5, 6])  # 1 și 2 pentru 1900-1999, 5 și 6 pentru 2000-2099

    # AA (Anul nașterii)
    if S in [1, 2]:
        anul = random.randint(1900, 1999)
    else:
        anul = random.randint(2000, 2024)
    AA = str(anul % 100).zfill(2)

    # LL (Luna nașterii)
    luna = random.randint(1, 12)
    LL = str(luna).zfill(2)

    # ZZ (Ziua nașterii)
    zi_maxima = calendar.monthrange(anul, luna)[1]
    ziua = random.randint(1, zi_maxima)
    ZZ = str(ziua).zfill(2)

    # JJ (Codul județului)
    while True:
        judet = random.randint(1, 52)
        if judet not in [49, 50]:
            JJ = str(judet).zfill(2)
            break

    # NNN (Număr secvențial)
    NNN = str(random.randint(1, 999)).zfill(3)

    # Concatenăm primele 12 cifre pentru a calcula cifra de control
    cnp_fara_control = f"{S}{AA}{LL}{ZZ}{JJ}{NNN}"
    C = genereaza_cifra_control(cnp_fara_control)

    # CNP-ul final
    cnp = f"{cnp_fara_control}{C}"
    return cnp

def hash_cnp_fnv(cnp, numar_sloturi=1000):
    # Inițializăm valorile FNV
    hash_value = 2166136261
    fnv_prime = 16777619

    # Aplicăm FNV-1a pe fiecare caracter din CNP
    for char in cnp:
        hash_value ^= int(char)
        hash_value *= fnv_prime

    # Obținem hash-ul final folosind modul
    hash_index = hash_value % numar_sloturi
    return hash_index

# Simulăm generarea și hashing-ul unui set de CNP-uri
numar_cnpuri = 1000000
numar_sloturi = 1000
cnp_list = [genereaza_cnp() for _ in range(numar_cnpuri)]
distributie_hash = {i: [] for i in range(numar_sloturi)}

for cnp in cnp_list:
    hash_index = hash_cnp_fnv(cnp, numar_sloturi)
    distributie_hash[hash_index].append(cnp)

# Extragem datele pentru graf
sloturi = list(distributie_hash.keys())
valori = [len(distributie_hash[i]) for i in range(numar_sloturi)]

# Crearea graficului de bare pentru distribuție
plt.figure(figsize=(12, 6))
plt.bar(sloturi, valori, color='blue')
plt.xlabel('Sloturi Hash')
plt.ylabel('Număr de CNP-uri per Slot')
plt.title('Distribuția CNP-urilor în Sloturile Hash')
plt.show()

# Selectăm aleatoriu 1000 de CNP-uri pentru căutare
cnp_aleatoare = random.sample(cnp_list, 1000)

numar_iteratii = []

for cnp in cnp_aleatoare:
    hash_index = hash_cnp_fnv(cnp, numar_sloturi)
    slot = distributie_hash[hash_index]

    # Căutăm CNP-ul în slotul hash și contorizăm iterațiile
    for idx, cnp_in_slot in enumerate(slot):
        if cnp_in_slot == cnp:
            numar_iteratii.append(idx + 1)  # Adăugăm numărul de verificări pentru a găsi CNP-ul
            break

# Calculăm statisticile
media_iteratii = np.mean(numar_iteratii)
min_iteratii = np.min(numar_iteratii)
max_iteratii = np.max(numar_iteratii)

print(f"Media numărului de iterații: {media_iteratii}")
print(f"Numărul minim de iterații: {min_iteratii}")
print(f"Numărul maxim de iterații: {max_iteratii}")