#Tugas1
kendaraan = ["motor", "yamaha", "150cc", "hitam", "roda 2"]

kendaraan.append("12.000.000")
kendaraan.append("kopling")

kendaraan.insert(kendaraan.index("yamaha") + 1, "rx king")

print(kendaraan)


#Tugas2
operasi = input("Menghitung luas bangun datar")
match operasi:
    case "1":
        sisi= int (input("masukan nilai sisi:"))
        luas= sisi*sisi
        print(luas)
    case "2":
        jari_jari= int (input("masukan nilai jari jari:"))
        luas= 3.14*jari_jari*jari_jari
        print(luas)
    case "3":
        alas= int (input("masukan nilai alas:"))
        tinggi= int(input("masukan nilai tinggi:"))
        luas= 0.5*alas*tinggi
        print(luas)  
    case _:
        print("salah pilih")    