
"""Program PRVACI:
    1) nacte data z studenti.txt jako tabulku seznamu - kazdy radek = vnoreny seznam.
    2) pridame sloupec udavajici vek
    3) pridame sloupec s pohlavim
    4) pridame sloupec email (=5pismen prijmeni + 3pismena jmena @hybrid.eu

"""


def nejaka_fce():                           # dílčí fce
    vstup = open('studenti.txt',"r" , encoding='utf-8')
    radky = [radek.split("\t") for radek in vstup]
    vstup.close()
    jmena = [radek[1] for radek in radky]
    print(radky)
    


def main():                                # hlavní fce.  (v C a Java se používá jako hlavní fce. V Pythonu ne, ale je to dobrý zvyk. +lze zavolat z importovaného modulu)
    nejaka_fce()

if __name__ == "__main__":                 # zde odpálím můj script     (abych ho mohl i importovat, ne jen spouštět přímo)
    main()