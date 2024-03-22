lista=[]
def beolvasas():
    with open ("adatok.txt","r",encoding="UTF-8") as fm:
        for sor in fm:
            lista.append(int(sor.strip()))
    return lista

def megszamolas(l):
    db=0
    for szam in l:
        if szam %2 == 0:
            print("A szám osztható 2-vel")
     
def kiir(a_b, p_sz):
    print(f"A listában levő számok {a_b}")
    print(f"A listában lévő páros számok: {p_sz}")

adat_betoltes=beolvasas()
paros_szam=megszamolas(lista)       
kiir(adat_betoltes, paros_szam)