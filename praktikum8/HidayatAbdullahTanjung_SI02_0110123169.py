def say(nama, alamat, gender, umur, hoby):
    print("saya adalah",nama)
    print("tempat tinggal di", alamat)
    print("jenis kelamin saya", gender)
    print("usia saya",umur)
    print("hoby saya", hoby)

say("hidayat","depok","laki-laki","18","main bola")
print("------------------------")

def cek_kelulusan(nilai):
    if nilai < 60:
        print("Gagal")
    elif 61 <= nilai <= 70:
        print("Baik")
    elif 71 <= nilai <= 80:
        print("Sangat Baik")
    elif 81 <= nilai <= 100:
        print("Istimewa")
    
    else:
        print("Tidak Lulus")
cek_kelulusan(90)
print("------------------------")

def ganjil(angka):
    for i in range(1, angka + 1, 2):
        print(i)
ganjil(100)
print("------------------------")

