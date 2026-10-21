
def tambah(a, b):
    return a + b


def kurang(a, b):
    return a - b


def kali(a, b):
    return a * b


def bagi(a, b):
    if b == 0:
        return "Tidak bisa membagi dengan nol"
    return a / b


if __name__ == "__main__":
    print("Hasil tambah:", tambah(10, 5))
    print("Hasil kurang:", kurang(10, 5))
    print("Hasil kali:", kali(10, 5))
    print("Hasil bagi:", bagi(10, 5))
