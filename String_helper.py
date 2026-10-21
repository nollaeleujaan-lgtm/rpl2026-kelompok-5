
def huruf_besar(teks):
    return teks.upper()


def huruf_kecil(teks):
    return teks.lower()


def balik_teks(teks):
    return teks[::-1]


if __name__ == "__main__":
    kalimat = "Belajar Python"

    print("Teks asli:", kalimat)
    print("Huruf besar:", huruf_besar(kalimat))
    print("Huruf kecil:", huruf_kecil(kalimat))
    print("Teks terbalik:", balik_teks(kalimat))
