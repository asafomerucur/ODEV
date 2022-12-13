
#1
Liste1 = ['a', 'e', 'i', 'o', 'i', 'u']
count = Liste1.count('i')
print('i harflerinin sayısı:', count)
count = Liste1.count('p')
print('p harflerinin sayısı:', count)

#2
liste2,liste3,liste4,liste5= ['a','b','c','d']
print(liste2)
print(liste3)
print(liste4)
print(liste5)

#3
list6 = ["Elma", "Armut" , "Kabak"]
list7 = [1, 2, 3]
list8 = list6 + list7
print(list8)

#4
liste9 = [34,1,56,334,23,2,3,19]
liste9.sort()
print('Küçükten Büyüğe Doğru',liste9)
liste9.reverse()
print('Büyükten Küçüğe Doğru',liste9)

#5
liste10= ["Merhaba", "Türkiye", "Nasılsın", "Tebrikler"]
print(liste10[-1])
print(liste10[-3])
print(liste10[-4])

#6
liste11 = [1, 2, 3, 4, 5, 6, 7]

print(liste11[1:3])
print(liste11[:3])
print(liste11[3:])
print(liste11)

#7
isimler = ['ali','veli','ayşe']
soyisimler = ['türk','izci','erel']
ad_soy1 = isimler[0] +' '+ soyisimler[0]
ad_soy2 = isimler[1] +' '+ soyisimler[1]
ad_soy3 = isimler[2] +' '+ soyisimler[2]
print(ad_soy1)
print(ad_soy2)
print(ad_soy3)

#8
liste12 = ['bir','iki','dört']
liste12[2]='üç'
liste12.insert(3,'dört')
liste12.insert(4,'beş')
print(liste12)
['bir', 'iki', 'üç', 'dört', 'beş']

#9
liste13=["birinci veri","ikinci veri","üçüncü veri ","dördüncü veri","beşinci veri"]
#İlk veri
print(liste13[0])
#Son veri
print(liste13[4])

