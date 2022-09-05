#ARRAY ROTASYONU
#Listedeki ilk elemanı index olarak kabul et o indexten ileriye git
# input = [2,3,5,7]
#output = [5,7,2,3]
def rotateArray(array):
    #array iinilk elemanını bul
    #bu değer bizim eski başlangıç değeri
    #output array in ilk elemanını bul
    #arrayin ilk elemanı eski başlangıç indexi kabul et
    #while döngüsü ile counter ata

    eski_baslangic = array[0] #input index 0 daki değer
    yeni_baslangic = [str(array[eski_baslangic])]

    count = eski_baslangic + 1
    length = len(array)

    while count%length != eski_baslangic:
        yeni_baslangic.append(str(array[count%length]))
        count += 1
    return "".join(yeni_baslangic)
print(rotateArray([8,5,7,9,6,4,4,8,6,1,3,6,3])) #output 6136385796448


#ARRAY ÇİFTLERi
#Verilen listede simetrisi var mı diye bakıyoruz
#inpıt = [5,6,7,1,6,5,1,7] birbirlerinin simetrisi varsa output = "ok"
# eğer yoksa simetrisi olmayan değeri yazdırıypruz
# stringe çevir "5,6","6,5"
# reverse pair olmayanları depolayın
# eğer depo boş ise "ok" return et
# eğer depo doluysa return depo
def arrayCouple(array):

    new= ""

    for k in range(len(array)):
        new += str(array[k]) + " "
        if k%2 == 1:
            new += ","

    new = new.split(",")

    depo = []
    for i in new:
        if i[::-1] not in new:
            for l in i.split():
                depo.append(l)

        elif i== i[::-1] and new.count(i)<2:
            for l in i.split():
                depo.append(l)
    if depo == []:
        return "Hepsi birbirinin simetriği"

    return ",".join(depo)

print(arrayCouple([5,6,6,5,7])) #output Hepsi birbirinin simetriği

#yanlış çalışıyor kontrol et