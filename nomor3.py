#Penggunaan if
soal = input("kamu udah selesai tugas dari Pak Hadi?")

if soal == "belum":
    print("ayo kita belajar bareng")

#penggunaan if dan else
print("Penggunaan if dan else : ")
nilai = 90

if(nilai > 70):
    print("Selamat Anda Lulus")
else:
    print("Maaf Anda Tidak Lulus")

#Penggunaan if, elif, else
print("Penggunaan if, elif, else : ")
gaji = 5000000

if gaji >= 10000000:
    print("Sangat banyak")

elif gaji >= 5000000:
    print("Sudah pas")

elif gaji >= 2000000:
    print("Masih kurang")

elif gaji >= 500000:
    print("Kurang Sekali")

else:
    print("Kondisi Salah")