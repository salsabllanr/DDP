import getpass

def error():
     print("===========================================")
     print("                 ANDA SALAH                ")
     print("===========================================")

def rumus():
    while True:
            print('='*54)    
            print('|               Rumus Segitiga Pythagoras             |')
            print('='*54)
            print(' 1. Sisi Tegak ')
            print(' 2. Alas')
            print(' 3. Sisi Miring')
            print(' 4. Keluar')
            print('='*54) 
            operasi = input('pilih operasi (1/2/3/4): ')
            print('='*54)
            if operasi == '1':
                 sisi_miring = eval(input('sisi miring: '))
                 sisi_alas = eval(input('sisi alas: '))
                 hasil = sisi_miring **2 - sisi_alas **2
                 print('hasil operasi dari sisi tegak', hasil)
                 rumus()
                #  lagi=input('adalagi?') 
                 break   
            elif operasi == '2' :
                 sisi_miring = eval(input('sisi miring: '))
                 sisi_tegak = eval(input('sisi tegak: '))
                 hasil = sisi_miring **2 - sisi_tegak **2
                 print('hasil operasi dari sisi alas', hasil)
                 rumus()
                #  lagi=input('adalagi?') 
                 break
            elif operasi == '3' :
                 sisi_tegak = eval(input('sisi tegak: '))
                 sisi_alas = eval(input('sisi alas: '))
                 hasil = sisi_tegak **2 + sisi_alas **2
                 print('hasil operasi dari sisi miring', hasil)
                 rumus()
                #  lagi=input('adalagi?') 
                 break
            elif operasi == '4' :
                 exit()
            else:
                 error()

print('='*54)
print('|            SELAMAT DATANG DI KALKULATOR            |')
print('|                SEGITIGA PYTHAGORAS                 |')
print('-'*54)
print('|            SILAHKAH LOGIN TERLEBIH DAHULU          |')
print('='*54)

username1 = 'Salsabilla'
nim1 = 23
kelas1 = 'A'
password1 = '2323'
salah = 0

while True :
    username = str(input('masukkan username : '))
    nim = int(input('masukkan nim : '))
    kelas = str(input('masukkan kelas : '))
    password = getpass.getpass('masukkan pasword : ')

    if username == username1 and nim == nim1 and kelas == kelas1 and password == password1 :
        print('='*54)
        print('|                 ANDA BERHASIL LOGIN                 |')
        print('-'*54)
        print('|            SILAHKAN MELANJUTKAN PENGGUNAAN          |')
        print('='*54) 
        rumus() 
        break

    else :
        salah += 1
        print("|         -----------------------------------------------------        |")
        print("|             sepertinya ada yang salah | silahkan ulangi              |")
        print("|         -----------------------------------------------------        |")
        if salah == 3 : 
            print("========================================================================")
            print("|                    SORRY SEPERTINYA ANDA BUKAN SALSA                 |")
            print("========================================================================")  
            exit()



