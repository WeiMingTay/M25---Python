# Mahte 2.5 Epic Bearbeitung
"""
Aufgabenstellung

Öffnet eure Python-IDE. Erstellt eine Sammlung von 5 Mathe-Tools (Artefakt: tools.py), die mathematische Probleme lösen.

1. Der Mengen-Rechner: Implementiert eine Funktion, die zwei Listen (z.B. Zutaten) als Sets vergleicht und ausgibt, was fehlt (Differenz) und was da ist (Schnitt).
2. Der Dubletten-Killer: Schreibt ein Skript, das eine Liste von Messwerten bereinigt (Sets) und die Anzahl der gelöschten Duplikate meldet.
3. Der Binär-Übersetzer: Baut einen Konverter, der eine Dezimalzahl einliest und die Binär- und Hex-Darstellung formatiert ausgibt.
4. Der ASCII-Decoder: Entwickelt eine Schleife, die einen Namen in seine ASCII-Codes zerlegt (ord()) und untereinander ausgibt.
5. Der Wörterbuch-Bot: Nutzt ein dict, um Fachbegriffe (Key) in Erklärungen (Value) zu übersetzen. Fragt den User nach einem Begriff.
"""
print("\033[42m-\033[0m" * 8**2)
# 1. Der Mengen-Rechner: Implementiert eine Funktion, die zwei Listen 
# (z.B. Zutaten) als Sets vergleicht und ausgibt, was fehlt (Differenz) 
# und was da ist (Schnitt).

print("\033[91m 1. Der Mengen-Rechner \033[0m")

zutaten1 = ["Tofu", "Tempeh", "Pilze", "Knoblauch", "Sternanis", "Sojasoße", "Nelken", "Austernsoße"]
zutaten2 = ["Zimt", "Pfefferkörner", "Sojasoße", "Zucker", "Sternanis", "Nelken" ]

def mengen_rechner(liste_a, liste_b):
    print(f"Was fehlt:\n{set(liste_a) - set(liste_b)}")
    print(f"Was verbindet:\n{set(liste_a) & set(liste_b)}")

print("\033[4mZutaten 1 als Basis\033[0m")
mengen_rechner(zutaten1, zutaten2)

print("\033[4mZutaten 2 als Basis\033[0m")
mengen_rechner(zutaten2, zutaten1)

print("\033[46m-\033[0m" * 8**2)

# 2. Der Dubletten-Killer: Schreibt ein Skript, das eine Liste von 
# Messwerten bereinigt (Sets) und die Anzahl der gelöschten Duplikate meldet.

print("\033[91m 2. Der Dubletten-Killer\033[0m")

messwerte_liste = [23,45,68,45,65,98,23,45,78,44]

# print(messwerte_liste)

def bereinigung(liste):
    liste_set = set(liste)
    differenz = len(liste) - len(liste_set)
    
    print("Messwerte: ", liste_set)
    print(f"Es wurden {differenz} Duplikate gelöscht.")
    
    # Durch das return kann man die bereinigte Liste und die Differenz noch verwenden
    return list(liste_set), differenz

bereinigte_liste, gelöscht = bereinigung(messwerte_liste)

print("\033[46m-\033[0m" * 8**2)

# 3. Der Binär-Übersetzer: Baut einen Konverter, der eine Dezimalzahl einliest 
# und die Binär- und Hex-Darstellung formatiert ausgibt.

print("\033[91m 3. Der Binär-Übersetzer \033[0m")

# Input sind erst immer Strings und müssen hier in ein Integer umgewandelt werden
#dezimal_zahl = int(input("Bitte Dezimalzahl zum Umrechnen in Binär und Hexadezimal eingeben: "))
dezimal_zahl = 44

def dez_zu_bin_hex(zahl):
    # slice, damit der jeweilige Präfix nicht angezeigt wird. ggf überlegen, ob man das erst nach dem return macht
    binaer = bin(zahl)[2:]
    hexa = hex(zahl)[2:].upper()
    
    return binaer, hexa

binaer_zahl, hexa_zahl = dez_zu_bin_hex(dezimal_zahl)
print(f"Dezimalzahl: {dezimal_zahl}\nBinär: {binaer_zahl}\nHexaDezimal: {hexa_zahl}")

print("-" * 8)
# Lösung über f-Strings
print(f"Binär: {dezimal_zahl:_b}\nHexadezimal: {dezimal_zahl:X}".replace("_", " "))

print("\033[46m-\033[0m" * 8**2)

# Der ASCII-Decoder: Entwickelt eine Schleife, die einen Namen in seine 
# ASCII-Codes zerlegt (ord()) und untereinander ausgibt.

print("\033[91m 4. Der ASCII-Decoder \033[0m")

name = "Wei Ming"
# name = input("Bitte Namen eingeben: ")

for buchstabe in name:
    ascii_wert = ord(buchstabe)
    print(f"Zeichen: '{buchstabe}’ | ASCII: {ascii_wert}")

print("\033[46m-\033[0m" * 8**2)

# Der Wörterbuch-Bot: Nutzt ein dict, um Fachbegriffe (Key) in 
# Erklärungen (Value) zu übersetzen. Fragt den User nach einem Begriff.

print("\033[91m 5. Der Wörterbuch-Bot \033[0m")

def wörterbuch():
    fruechte_lexikon = {
    "Durian": "Sie wird für ihre cremige Konsistenz und ihr komplexes, herzhaft-süßes Aroma geschätzt.",
    "Mangostan": "Diese Frucht bietet ein perfekt ausbalanciertes Verhältnis zwischen Süße und feiner Säure.",
    "Rambutan": "Hinter der weichen, behaarten Schale steckt ein sehr erfrischendes und saftiges Fruchtfleisch.",
    "Erdbeere": "Die kleinen gelben Nüsschen auf der roten Haut machen sie botanisch einzigartig.",
    "Apfel": "Er ist ein vielseitiger Energielieferant, der in fast jedem Klima der Welt gedeiht.",
    "Mango": "Das goldgelbe Fruchtfleisch ist besonders reich an Vitaminen und tropischer Süße.",
    "Drachenfrucht": "Die Kaktusfrucht fasziniert durch ihr punktiertes Inneres und ihre außergewöhnliche Optik.",
    "Ananas": "Ihre charakteristische Struktur und die intensive Süße machen sie zu einer kulinarischen Ikone.",
    "Heidelbeere": "Die intensive Färbung stammt von Pflanzenstoffen, die als besonders wertvoll gelten.",
    "Granatapfel": "Seine zahlreichen Kerne sind für ihre knackige Textur und den herben Saft bekannt."
    }
    
    # frucht = input("Bitte Obstnamen eingeben: ").capitalize()
    frucht= "Durian"
    
    if frucht in fruechte_lexikon:
        print(f"Name der Frucht: {frucht.capitalize()}\nWas macht diese aus: {fruechte_lexikon[frucht]}")
    else:
        print(f"Sorry, '{frucht.capitalize()}' leider nicht gefunden")

wörterbuch()

print("\033[42m-\033[0m" * 8**2)

# Echte MatheTools

# Addition
print("\033[92m 1. Summe \033[0m")

def summe(a, b):
    return a+b
"""
zahl1 = int(input("Bitte erste Zahl eingeben: "))
zahl2 = int(input("Bitte zweite Zahl eingeben: "))

ergebnis_summe = summe(zahl1, zahl2)

print(f"Summe aus {zahl1} und {zahl2} ist {ergebnis_summe}.")
"""

print("\033[46m-\033[0m" * 8**2)

# Multiplikation
print("\033[92m 2. Multiplikation \033[0m")

def multiplikation(a, b):
    return a * b
"""
zahl3 = int(input("Bitte erste Zahl eingeben: "))
zahl4 = int(input("Bitte zweite Zahl eingeben: "))

ergebnis_produkt = multiplikation(zahl3, zahl4)

print(f"Produkt aus {zahl3} und {zahl4} ist {ergebnis_produkt}.")
"""
print("\033[46m-\033[0m" * 8**2)

# Subtraktion

print("\033[92m 3. Subraktion \033[0m")

def subtraktion(a, b):
    return a - b

print("\033[46m-\033[0m" * 8**2)

# Division

print("\033[92m 4. Division \033[0m")

# Der Quotient ist ein float
def division(a, b):
    return a / b

print("\033[46m-\033[0m" * 8**2)

# Quadrat

print("\033[92m 5. Quadrat \033[0m")

def zum_quadrat(a):
    return a ** 2

print("\033[46m-\033[0m" * 8**2)

print("\033[92m 6. Wurzel ziehen \033[0m")

# Wurzel

def wurzel(a):
    return a ** 0.5

#print("\033[46m-\033[0m" * 8**2)
print("\033[42m-\033[0m" * 8**2)