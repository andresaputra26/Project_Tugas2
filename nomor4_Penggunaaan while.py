#penggunaan while angka
p = int(input("Masukkan banyak pengulangan: "))
i = 1
while i <= p:
   print(i)
   i+=1

#penggunaan while karakter
print("Macam-macam merek hp : ")
merekhp = ["Samsung", "Xiaomi", "Iphone", "Realme", "Oppo", "Vivo"]
while merekhp:
  print(merekhp.pop())