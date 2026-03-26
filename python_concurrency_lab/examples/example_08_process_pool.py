from multiprocessing import Pool

def podnies_do_kwadratu(x):
    return x * x


if __name__ == "__main__":
    dane = list(range(10))

    with Pool(processes=4) as pool:
        wyniki = pool.map(podnies_do_kwadratu, dane)

    print(f"Dane wejściowe: {dane}")
    print(f"Wyniki: {wyniki}")
