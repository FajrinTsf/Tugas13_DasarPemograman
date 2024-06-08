print("Nama   : Muhammad Fajrin Tsinan F")
print("NIM    : 20230040086")
print("Kelas  : TI23C\n")

# 1. Konversi nilai ke Integer


def konversi_integer(teks):
    try:
        nilai_integer = int(teks)
        print(f"nilai integer adalah {nilai_integer}")
    except ValueError:
        print("kesalahan : integer tidak valid")


konversi_integer("123")
konversi_integer("ABC")


# 2. Akses list indeks
def akses_elemen(dafar_list, indeks):
    try:
        hasil = dafar_list[indeks]
        print(f"elemen di indeks {indeks} adalah {hasil}")
    except IndexError:
        print("kesalahan : indeks di luar jangkauan")


list_saya = [1, 2, 3]
akses_elemen(list_saya, 1)
akses_elemen(list_saya, 5)
