# By Muhammad Rheza Pahleevi
# Teknik Informatika
def makanan():
    global total_makan, jumlah_porsi, nama_makanan

def minuman():
    global total_minum, jumlah_gelas, nama_minuman

print("|========================================|")
print("|         KASIR WARUNG SEDERHANA         |")
print("|========================================|")
print("|         : Pilih Menu Makanan :         |")
print("|========================================|")
print("|1. Nasi Campur                Rp.13000,-|")
print("|2. Nasi Pecel                 Rp.10000,-|")
print("|3. Nasi Ayam Goreng           Rp.13000,-|")
print("|4. Nasi Ayam Geprek           Rp.15000,-|")
print("|5. Mie Goreng                 Rp.9000,- |")
print("|========================================|")

menu_makanan = int(input("Pilih Menu (1/2/3/4/5) : "))
jumlah_porsi = int(input("Berapa Porsi : "))

if menu_makanan == 1:
    total_makan = jumlah_porsi * 13000
    print("Nasi Campur", jumlah_porsi,"Porsi : Rp.",total_makan)
    nama_makanan = ("Nasi Campur")
elif menu_makanan == 2:
    total_makan = jumlah_porsi * 10000
    print("Nasi Pecel", jumlah_porsi,"Porsi : Rp.",total_makan)
    nama_makanan = ("Nasi Pecel")
elif menu_makanan == 3:
    total_makan = jumlah_porsi * 13000
    print("Nasi Ayam Goreng", jumlah_porsi,"Porsi : Rp.",total_makan)
    nama_makanan = ("Nasi Ayam Goreng")
elif menu_makanan == 4:
    total_makan = jumlah_porsi * 15000
    print("Nasi Ayam Geprek", jumlah_porsi,"Porsi : Rp.",total_makan)
    nama_makanan = ("Nasi Ayam Geprek")
elif menu_makanan == 5:
    total_makan = jumlah_porsi * 9000
    print("Mie Goreng", jumlah_porsi,"Porsi : Rp.",total_makan)
    nama_makanan = ("Mie Goreng")
else:
    print("Pilihan Tidak Tersedia")

print("|========================================|")
print("|         : Pilih Menu Minuman :         |")
print("|========================================|")
print("|1. Es Teh                      Rp.5000,-|")
print("|2. Teh Anget                   Rp.4000,-|")
print("|3. Es Jeruk                    Rp.6000,-|")
print("|4. Es Susu                     Rp.7000,-|")
print("|5. Teh Tawar                   Rp.3000,-|")
print("|========================================|")

menu_minuman = int(input("Pilih Menu (1/2/3/4/5) : "))
jumlah_gelas = int(input("Berapa Gelas : "))

if menu_minuman == 1:
    total_minum = jumlah_gelas * 5000
    print("Es Teh", jumlah_gelas,"Gelas : Rp.",total_minum)
    nama_minuman = ("Es Teh")
elif menu_minuman == 2:
    total_minum = jumlah_gelas * 4000
    print("Teh Anget", jumlah_gelas,"Gelas : Rp.",total_minum)
    nama_minuman = ("Teh Anget")
elif menu_minuman == 3:
    total_minum = jumlah_gelas * 6000
    print("Es Jeruk", jumlah_gelas,"Gelas : Rp.",total_minum)
    nama_minuman = ("Es Jeruk")
elif menu_minuman == 4:
    total_minum = jumlah_gelas * 7000
    print("Es Susu", jumlah_gelas,"Gelas : Rp.",total_minum)
    nama_minuman = ("Es Susu")
elif menu_minuman == 5:
    total_minum = jumlah_gelas * 3000
    print("Teh Tawar", jumlah_gelas,"Gelas : Rp.",total_minum)
    nama_minuman = ("Teh Tawar")
else:
    print("Pilihan Tidak Tersedia")

makanan()
minuman()
jumlah_semuanya = total_makan + total_minum

print()
print("|========================================|")
print("|            Daftar Pembelian            |")
print("|========================================|")
print("|Makanan :",nama_makanan,"\t")
print("|Porsi   :",jumlah_porsi,"\t\t\t")
print("|Minuman :",nama_minuman,"\t")
print("|Gelas   :",jumlah_gelas,"\t\t\t")
print("|========================================|")
print("|               Total Biaya              |")
print("|========================================|")
print("| Total  : Rp.",jumlah_semuanya,",-")
print("|========================================|")
print()

