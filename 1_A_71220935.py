print ('======= Program Manipulasi String =======')
print ('Pilihan menu:' )
print ('1. Hitung kata')
print ('2. Ubah kata')

def Hitung_Kata(kata, hitung):
     hasil_1 = kata.count(hitung)
     return print

def Ubah_Kata(kata, ubah, ganti):
      hasil = kata.replace(ubah, ganti)
      return hasil
  

angka = int((input ('Pilihan anda: ')))
kata = input ('Masukkan sebuah kalimat/kata: ')
if angka == 1:
    hitung = input('Masukkan kata yang ingin dihitung: ')
    Hitung_Kata = Hitung_Kata(kata, hitung)
    print ('Terdapat sebanyak', Hitung_Kata, 'kata', hitung, 'di dalam kalimat')
    Hitung_Kata

elif angka == 2:
    ubah = input ('Masukkan kata yang ingin diubah: ')
    ganti = input ('Masukkan kata pengganti: ')
    Ubah_Kata = Ubah_Kata(kata, ubah, ganti)
    print ('String berhasil menjadi: ', Ubah_Kata)
    Ubah_Kata

else:
    print ('Pilihan yang anda input tidak terdaftar')


