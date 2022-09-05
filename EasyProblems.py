import math
#1: FAKTÖRİYEL
def factorial (num):
    f = 1
    for i in range (1,num+1):
        f= f*i
    return f
print("5! = ", factorial(5))
print("120! = ", factorial(120))
print("90! = ", factorial(90))

#2: KELİMENİN TERSİ
def reverse (str):
# str [start:stop:step]
    return str[::-1]
print("merhaba:", reverse("merhaba"))

#3: SAAT ÇEVİRME
def convertTime(num1):
    #saati bul 128/60= 2. saat
    saat = int(math.floor(num1/60))
    #dakikayı bul 128%60 kalan dakikakdır
    dakika =  num1%60
    #string (saati + : + dakika)
    return str(saat)+ ":"+str(dakika)
print("128 = ", convertTime(128))
print("345 = ", convertTime(345))

#4: Büyük Harf
def buyukHarf(str1):
    kelimeler = str1.split(" ")
    for i in range (0,len(kelimeler)):
        kelimeler[i]= kelimeler[i][0].upper() + kelimeler[i][1:]
        return " ".join(kelimeler)
print(buyukHarf ("kod yazmak çok zevkli"))

deneme_str= "kod yazmak çok zevkli"
print(deneme_str.title()) #ikinci seçenek
