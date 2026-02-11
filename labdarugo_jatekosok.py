"""
Olvasd be a labdarugok.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány játékos szerepel a fájlban?
2. Melyik játékos szerezte a legkevesebb gólt?
3. Melyik játékos szerzett a legtöbb gólt?
4. Ki játszott a legtöbb mérkőzést?
5. Átlagosan hány gólt szerzett egy játékos?

***EXTRA - nehezebb feladat*** (nem kötelező, de érdemes megpróbálni):
6. Melyik csapat szerzett a legtöbb gólt? (feltételezve, hogy egy játékos csak egy csapatban játszott)


A megoldott feladatokat a kiirt_adatok nevű mappában hozd létre statisztika.txt néven!
"""

labdarugok = []
with open('beolvasando_adatok/labdarugok.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        labdarugo = {'neve': adatok[0], 'csapat': adatok[1], 'golszam': int(adatok[2]), 'merkozesek szama': int(adatok[3]) }
        labdarugok.append(labdarugo)
print(f'{labdarugok=}')

print(f"A beolvasott fájlban összesen {len(labdarugok)} játékos szerepel.")

print(f"A legkevesebb gólt szerző játékos: {min(labdarugok, key=lambda x: x ["golszam"])}")

print(f"A legtöbb gólt szerző játékos: {max(labdarugok, key=lambda x: x ["golszam"])}")

print(f"A legtöbb mérkőzést játszó játékos:  {max(labdarugok, key=lambda x: x ["merkozesek szama"])}")

osszes_gol = 0
for j in labdarugok:
    osszes_gol += j['golszam']
atlag_gol = osszes_gol / len(labdarugok)
print(f"Az átlagos gólszám: {atlag_gol}")
csapat_golok = {}
for j in labdarugok:
    csapat = j['csapat']
    csapat_golok[csapat] = csapat_golok.get(csapat, 0) + j['golszam']

legtobb_gol_csapat = max(csapat_golok, key=csapat_golok.get)

print(f"A legtöbb gólt szerző csapat: {legtobb_gol_csapat}")
