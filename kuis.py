
def tampilkan_pertanyaan():
    print("=== KUIS PENGETAHUAN UMUM ===")
    print("1. Apa ibu kota Indonesia?")
    print("A. Jakarta")
    print("B. Bandung")
    print("C. Surabaya")
    print("D. Malang")

    jawaban = input("Masukkan jawaban (A/B/C/D): ").upper()

    if jawaban == "A":
        print("Benar! Jakarta adalah ibu kota Indonesia.")
    else:
        print("Jawaban belum tepat.")


if __name__ == "__main__":
    tampilkan_pertanyaan()
