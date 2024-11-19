import random
import calendar
import matplotlib.pyplot as plt
import numpy as np

total_populatie = 19064409

distrib_judete = {
    "Bihor": 555774, "Bistrita-Nasaud": 297088, "Cluj": 694149, "Maramures": 452092, "Satu Mare": 330566,
    "Salaj": 210548, "Alba": 326027, "Brasov": 557549, "Covasna": 199627, "Harghita": 292237, "Mures": 519830,
    "Sibiu": 393776, "Bacau": 595611, "Botosani": 388905, "Iasi": 77861, "Neamt": 447667, "Suceava": 644718,
    "Vaslui": 369237, "Braila": 274490, "Buzau": 397801, "Constanta": 658611, "Galati": 492692, "Tulcea": 189453,
    "Vrancea": 331887, "Arges": 564677, "Calarasi": 279072, "Dambovita": 476591, "Giurgiu": 258176, "Ialomita": 249388,
    "Prahova": 688860, "Teleorman": 315104, "Ilfov": 583547, "Bucuresti": 1719958, "Dolj": 598637, "Gorj": 310479,
    "Mehedinti": 230392, "Olt": 376468, "Valcea": 340430, "Arad": 410805, "Caras-Severin": 243799, "Hunedoara": 354805,
    "Timis": 664270
}

distrib_sex = {
    "Masculin": 9274651 / total_populatie,
    "Feminin": 9789758 / total_populatie
}

distrib_varsta = {
    "0-4 ani": 917110 / total_populatie,
    "5-9 ani": 1059599 / total_populatie,
    "10-14 ani": 1070618 / total_populatie,
    "15-19 ani": 1098247 / total_populatie,
    "20-24 ani": 979201 / total_populatie,
    "25-29 ani":966854 / total_populatie,
    "30-34 ani": 1114372 / total_populatie,
    "40-44 ani": 1336903 / total_populatie,
    "45-49 ani": 1510178 / total_populatie,
    "50-54 ani": 1468702 / total_populatie,
    "55-59 ani": 1308353 / total_populatie,
    "60-64 ani": 1080102 / total_populatie,
    "65-69 ani": 1260835 / total_populatie,
    "70-74 ani": 1060956 / total_populatie,
    "75-79 ani": 663388 / total_populatie,
    "80-84 ani": 446486 / total_populatie,
    "85 ani si peste": 390302 / total_populatie
}

prenume_barbatesc = ["Ion", "Andrei", "Cristian", "Mihai", "Gabriel", "Stefan", "Vlad", "Paul", "Florin", "Cosmin", "Lucian", "Marian", "Radu", "Daniel", "Alexandru", "Doru"]
prenume_feminin = ["Maria", "Elena", "Ana", "Ioana", "Alexandra", "Laura", "Diana", "Irina", "Anca", "Lucia", "Gabriela", "Carmen", "Mihaela", "Loredana", "Oana", "Roxana"]
nume_familie = ["Popescu", "Ionescu", "Georgescu", "Dumitrescu", "Radu", "Matei", "Marin", "Vasile", "Popa", "Sima", "Ilie", "Păun", "Constantin", "Mihăilescu", "Stan", "Bălan", "Tudor", "Lungu", "Munteanu", "Stoica"]

judete_coduri = {
    "Alba": "01", "Arad": "02", "Arges": "03", "Bacau": "04", "Bihor": "05",
    "Bistrita-Nasaud": "06", "Botosani": "07", "Brasov": "08", "Braila": "09",
    "Buzau": "10", "Caras-Severin": "11", "Cluj": "12", "Constanta": "13",
    "Covasna": "14", "Dambovita": "15", "Dolj": "16", "Galati": "17", "Gorj": "18",
    "Harghita": "19", "Hunedoara": "20", "Ialomita": "21", "Iasi": "22", "Ilfov": "23",
    "Maramures": "24", "Mehedinti": "25", "Mures": "26", "Neamt": "27", "Olt": "28",
    "Prahova": "29", "Satu Mare": "30", "Salaj": "31", "Sibiu": "32", "Suceava": "33",
    "Teleorman": "34", "Timis": "35", "Tulcea": "36", "Vaslui": "37", "Valcea": "38",
    "Vrancea": "39", "Bucuresti": "40", "Bucuresti - Sector 1": "41", "Bucuresti - Sector 2": "42",
    "Bucuresti - Sector 3": "43", "Bucuresti - Sector 4": "44", "Bucuresti - Sector 5": "45",
    "Bucuresti - Sector 6": "46", "Bucuresti - Sector 7 (desfiintat)": "47",
    "Bucuresti - Sector 8 (desfiintat)": "48", "Calarasi": "51", "Giurgiu": "52"
}

def genereaza_nume(sex):
    if sex == "Masculin":
        prenume_ales = random.choice(prenume_barbatesc)
    else:
        prenume_ales = random.choice(prenume_feminin)
    nume_ales = random.choice(nume_familie)
    return f"{prenume_ales} {nume_ales}"

def genereaza_cifra_control(cnp_fara_control):
    constanta = "279146358279"
    suma = sum(int(cnp_fara_control[i]) * int(constanta[i]) for i in range(12))
    cifra_control = suma % 11
    return cifra_control if cifra_control < 10 else 1


def genereaza_cnp():
    sex = random.choices(
        population=list(distrib_sex.keys()),
        weights=list(distrib_sex.values())
    )[0]

    varsta = random.choices(
        population=list(distrib_varsta.keys()),
        weights=list(distrib_varsta.values())
    )[0]

    anul_curent = 2024
    if "peste" in varsta:
        anul = random.randint(1900, anul_curent - 85)
    else:
        ani = [int(s) for s in varsta.replace("ani", "").replace(" ", "").split("-") if s.isdigit()]
        if len(ani) == 2:
            anul = random.randint(anul_curent - ani[1], anul_curent - ani[0])
        else:
            raise ValueError(f"Format necunoscut pentru grupa de vârstă: {varsta}")

    if anul < 2000:
        S = 1 if sex == "Masculin" else 2
    else:
        S = 5 if sex == "Masculin" else 6

    judet = random.choices(
        population=list(distrib_judete.keys()),
        weights=list(distrib_judete.values())
    )[0]

    if judet == "Bucuresti":
        JJ = str(random.randint(40, 48))  # Coduri pentru București și sectoarele sale
    else:
        JJ = judete_coduri.get(judet, None)
        if JJ is None:
            raise ValueError(f"Cod județ necunoscut pentru județul {judet}")

    LL = str(random.randint(1, 12)).zfill(2)
    zi_maxima = calendar.monthrange(anul, int(LL))[1]
    ZZ = str(random.randint(1, zi_maxima)).zfill(2)

    NNN = str(random.randint(1, 999)).zfill(3)

    cnp_fara_control = f"{S}{str(anul % 100).zfill(2)}{LL}{ZZ}{JJ}{NNN}"
    constanta = "279146358279"
    suma = sum(int(cnp_fara_control[i]) * int(constanta[i]) for i in range(12))
    cifra_control = suma % 11
    cifra_control = cifra_control if cifra_control < 10 else 1

    # CNP final
    cnp = f"{cnp_fara_control}{cifra_control}"

    nume = genereaza_nume(sex)

    return {"cnp": cnp, "nume": nume}


def hash_cnp_fnv(cnp, numar_sloturi=1000):
    hash_value = 2166136261
    fnv_prime = 16777619

    for char in cnp:
        hash_value ^= int(char)
        hash_value *= fnv_prime

    hash_index = hash_value % numar_sloturi
    return hash_index

numar_cnpuri = 1000000
numar_sloturi = 1000
cnp_list = [genereaza_cnp() for _ in range(numar_cnpuri)]
distributie_hash = {i: [] for i in range(numar_sloturi)}

for cnp_obj in cnp_list:
    hash_index = hash_cnp_fnv(cnp_obj["cnp"], numar_sloturi)
    distributie_hash[hash_index].append(cnp_obj)

valori = [len(distributie_hash[i]) for i in range(numar_sloturi)]

plt.figure(figsize=(12, 6))
plt.bar(range(numar_sloturi), valori, color='blue')
plt.xlabel('Sloturi Hash')
plt.ylabel('Număr de CNP-uri per Slot')
plt.title('Distribuția CNP-urilor în Sloturile Hash')
plt.show()

cnp_aleatoare = random.sample(cnp_list, 1000)

numar_iteratii = []

for cnp_obj in cnp_aleatoare:
    hash_index = hash_cnp_fnv(cnp_obj["cnp"], numar_sloturi)
    slot = distributie_hash[hash_index]

    for idx, cnp_in_slot in enumerate(slot):
        if cnp_in_slot["cnp"] == cnp_obj["cnp"]:
            numar_iteratii.append(idx + 1)
            break

media_iteratii = np.mean(numar_iteratii)
min_iteratii = np.min(numar_iteratii)
max_iteratii = np.max(numar_iteratii)

print(f"Media numărului de iterații: {media_iteratii}")
print(f"Numărul minim de iterații: {min_iteratii}")
print(f"Numărul maxim de iterații: {max_iteratii}")
