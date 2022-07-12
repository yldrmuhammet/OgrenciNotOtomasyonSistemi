#Kütüphaneler..

import pandas as pd
import csv

# Kullanılan indexler..

x = 0
indeksler           = []
isimlistesi         = []
soyisimlistesi      = []
okulnumaralistesi   = []
puanlistesi         = []
gecmelistesi        = []
harflistesi         = []

while True:
    isim    = input("Öğrenci İsmini Giriniz: ")
    soyisim = input("Öğrenci Soyismini Giriniz: ")
    numara  = int(input("Öğrenci Okul Numarasını Giriniz: "))
    puan    = int(input("Öğrenci Notunu Giriniz: "))
    x       = x+1

    #Notlandırma sistemi..

    def fnotlandirma():
        if (puan >= 90):
         print("AA ile geçtiniz ")
         harflistesi.append('AA')
         gecmelistesi.append('Geçti')

        elif (puan >= 85):
         print("BA ile geçtiniz ")
         harflistesi.append('BA')
         gecmelistesi.append('Geçti')

        elif (puan >= 75):
         print("BB ile geçtiniz ")
         harflistesi.append('BB')
         gecmelistesi.append('Geçti')

        elif (puan >= 65):
         print("CB ile geçtiniz ")
         harflistesi.append('CB')
         gecmelistesi.append('Geçti')

        elif (puan >= 55):
         print("CC ile geçtiniz ")
         harflistesi.append('CC')
         gecmelistesi.append('Geçti')

        elif (puan >= 50):
         print("DC ile geçtiniz ")
         harflistesi.append('CB')
         gecmelistesi.append('Geçti')  

        elif (puan >= 45):
         print("DD ile geçtiniz ")
         harflistesi.append('DD')
         gecmelistesi.append('Geçti')  

        else:
         print("FF ile kaldiniz")
         harflistesi.append('FF')
         gecmelistesi.append('Kaldi')
    
    fnotlandirma()

    isimlistesi.append(isim)
    soyisimlistesi.append(soyisim)
    okulnumaralistesi.append(numara)
    harflistesi.append(puan)

    indeksler.append(x)
    
    karar = input("Devam etmek istiyor musunuz ? (Y/N)")

# Eklemeye devam halinde?..

    if karar == 'Y':
        print("Teşekkürler. İşleminize devam ediliyor..")
        continue
    elif karar == 'N':
        ogrdata = {
                        'Öğrenci İsmi'    : isimlistesi,
                        'Öğrenci Soyismi' : soyisimlistesi,
                        'Okul Numarası'   : okulnumaralistesi,
                        'Öğrenci Puanı'   : puanlistesi,
                        'Harf Notu'       : harflistesi,
                        'Geçme Durumu'    : gecmelistesi
                         }
#Excel Dönüşümü..
        ogrdata = pd.DataFrame(data=ogrdata,index=indeksler)
        ogrdata.to_excel('./proje1pythonistas.xlsx')
        
    break