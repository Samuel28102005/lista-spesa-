lista = []

def riempi_lista(lista):
    prodotto = input("inserire prodotto:")
    lista.append(prodotto)

riempi_lista(lista)
riempi_lista(lista)
riempi_lista(lista)


def Stampa_lista(lista):
    print("lista della spesa")
    for i in range(len(lista)):
        print(f"{i + 1}. {lista[i]}")


def rimuovi_lista(lista):
    prodotto = input ("inserisci il prodotto da rimuovere dalla lista:")
    lista.pop(lista.index(prodotto))

rimuovi_lista(lista)
Stampa_lista(lista)


