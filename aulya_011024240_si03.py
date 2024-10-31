# SOAL NO 1
#1. buat variabel variable list dengan value (namakendaraan)
# Jeniskendaraan, cckendaraan, warna kendaraan, roda 
# kendaraan

kendaraan = ['Honda Beat','sepeda motor', 120, 'hitam', 2]
print('kendaraan saya')
print(kendaraan)
print("========")

#tambahkan dari list tersebut di belakang dengan value : [harga kendaraan, tipe kendaraan]
kendaraan.append(15000000)
kendaraan.append("metic")
print(kendaraan)
print("========")

# tambahkan setelah jenis kendaraan dengan value [merk kendaraan]
kendaraan.insert(2, "Honda")
print(kendaraan)
print("===========")

#SOAL NO 2
#Buat program phyto dengan match case untuk menghitung luas bangun datar:
#jika pilih 1 , maka menghitung luas persegi
#jika pilih 2 , maka menghitung luas lingkaran
#jika pilih 3 , maka menghitung luas segitiga
#kalau pilihannya tidak ada maka ada keterangan : salah pilih 

print("ini adalah program sederhana untuk menghitung luas bangun datar")
print ("Pilih Menu angka 1-3 : \n1. Persegi\n2. Lingkaran\n3. Segitiga")
pilihMenu = int(input("Silahkan pilih menu dengan mengetikkan angka 1-3 ="))

match pilihMenu :
    case 1 : 
        print("ini adalah menu untuk menghitung luas persegi")
        sisi = int(input("Silahkan masukkan nilai yang mau di hitung"))
        hitung = sisi * sisi
        print (f"luas persegi adalah : {hitung}")
    case 2 :
        print("ini adalah menu untuk menghitung luas Lingkaran")
        π = 22/7
        r = int(input("Silahkan masukkan nilai r"))
        hitung = π * r * r
        print (f"luas lingkaran adalah : {hitung}")
    case 3 :
        print("ini adalah menu untuk menghitung luas Segitiga")
        a = int(input("Silahkan masukkan nilai a:"))
        t = int(input("Silahkan masukkan nilai t:"))
        hitung = a * t / 2
        print (f"luas Segitiga adalah : {hitung}")
    case _ :
        print("Pilihan tidak valid, silahkan pilih antar 1-3")
    







