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



while True:
    scelta = input("quale funzione vuoi eseguire? (aggiungi, rimuovi, stampa, esci):\n 1. Aggiungi\n 2. Rimuovi\n 3. Stampa\n 4. Esci")
    if scelta == "1":
        Aggiungi_lista(lista)
    if scelta == "2":
        Rimuovi_prodotto(lista)
    if scelta == "3":
        Stampa_lista(lista)
    if scelta == "4":
        break