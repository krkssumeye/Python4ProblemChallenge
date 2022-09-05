#KELİME KARIŞTIRMA
def harfKaristir(str1, str2):
    for i in str2 :
        if i not in str1:
            return False
    return True
print(harfKaristir("merkez kütüphanesi", "ezkerm üphaneksiüt"))
print(harfKaristir("merkez kütüphanesi", "ezkfferm üphaneksiüt"))

#SIKLIK BULMA
# string harflerine eriş
# bulduğun harfin bir sonraki indexine bak hatta sonraki indexlerdeki harfleri kontrol et
# bir string içinde birleştir
def siklikBulma ( string):
    i=0
    final_string = ""
    while i< len(string):
        c = string[i]
        j = i+1
        compressed = [1,c]

        while j< len (string):
            if string[j] == c:
                compressed[0] += 1
            else:
                break
            j +=1
        final_string += "".join(map(str,compressed))
        i = j

    return final_string

print(siklikBulma("aassdkkdd"))


#KAYIP BASAMAK
def kayipBasamak(string):
    #x i bul replace et 0-9 sayılarıyla
    #eval() metodu kullan string karşılaşştırma

    for i in range (10):
        c=string.replace("x",str(i))
        x=string.index("=")
        if eval(c[:x]) == eval(c[x+1:]):
            #eval("1x0 / 3") == eval("50") yani buradaki x i silip yerine 5 yazar
            return str(i)
print(kayipBasamak("5 + x = 9")) #4
print(kayipBasamak("1x + 7 = 17")) #0
print(kayipBasamak("1x * 11 = 132")) #2

#eval fonk stringle mat işlemi yapamadığımız zaman
if eval("55") == eval("50+5"):
    print("yes")
else:
    print("no")