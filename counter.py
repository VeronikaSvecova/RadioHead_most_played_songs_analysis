from collections import Counter
def nacti_soubor(nazev_souboru: str) -> list:
    vysledek = []
    with open(nazev_souboru, encoding="utf8") as f:
        for radek in f:
            vysledek.append(radek.strip())
    return vysledek


data = nacti_soubor("radiohead.csv")

citac = Counter()

for zaznam in data[1:]:
    sloupce = zaznam.split(",", maxsplit=3)
    if sloupce[1] != "Rádio Beat":
        continue

    titulek = sloupce[3]
    titulek_zvlast = titulek.split(" - ", maxsplit=1)
    interpret = titulek_zvlast[0]
    if interpret == "Radio BEAT":
        continue

    citac[interpret] += 1

for item in citac.most_common(10):
    print(item)