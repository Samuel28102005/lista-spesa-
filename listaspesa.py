lista = []

def riempi_lista(lista):
    prodotto = input("inserire prodotto:")
    lista.append(prodotto)



def Stampa_lista(lista):
    print("lista della spesa")
    for i in range(len(lista)):
        print(f"{i + 1}. {lista[i]}")


def rimuovi_lista(lista):
    prodotto = input ("inserisci il prodotto da rimuovere dalla lista:")
    lista.pop(lista.index(prodotto))


def conta_elementi(lista):
    return print(len(lista))


def svuota_lista(lista):
    lista.clear()


while True:
    scelta = input("quale funzione vuoi eseguire? (riempi, rimuovi, stampa, svuota lista, conta elementi, esci):\n 1. riempi\n 2. Rimuovi\n 3. Stampa\n 4. Svuota Lista\n 5. Conta Elementi\n 6. Esci\n")
    if scelta == "1":
        riempi_lista(lista)
    if scelta == "2":
        rimuovi_lista(lista)
    if scelta == "3":
        Stampa_lista(lista)
    if scelta == "4":
        svuota_lista(lista)
    if scelta == "5":
        conta_elementi(lista)
    if scelta == "6":
        break

