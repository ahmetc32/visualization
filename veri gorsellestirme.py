# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 13:36:09 2022

@author: Ahmet
"""
"""
# sözlük {"anahtar":"değer}
bos={}   # boş sözlük oluşturma
print(bos)

bos2=dict()   # bos sözlük oluşturma
print(bos2)

renkler={"Kırmızı":"Red","Siyah":"Black","Beyaz":"White"}
print(renkler)

print(renkler.items())

print(renkler.keys())

print(renkler.values())

print(renkler["Siyah"])   # tek bir anahtara ait veriyi çekme

print(dir(renkler))

print(renkler.get("Siyah"))  # tek bir anahtara ait veriyi çekme

renkler.pop("Siyah")        # sözlükten belirli anahtara sahip elemanı silme
print(renkler)

renkler["Mavi"]="Blue"    # sözlüğe ekleme
print(renkler)

sayilar={1:["Bir","One"],2:["İki","Two"]}
print(sayilar)

anahtar=sayilar.keys()
for i in anahtar:
      print(i)

deger=sayilar.values()
for i in deger:
      print(i)

genel=sayilar.items()
for i in genel:
      print(i)

sayilar.popitem()   # son anahtar:değer çiftini siler
print(sayilar)

print(renkler)
renkler.__delitem__("Kırmızı")
print(renkler)

# Bir sözlüğün anahtar ve değer bilgisinin otomatik girilmesi
sozluk=dict()
for i in range(1,11):
  sozluk[i]=(i**2)

print(sozluk)

print(renkler)

renkler["Mavi"]="Dark Blue"

print(renkler)


#Sözlüğün dışardan girilmesi
s1=dict()
for i in range(3):
  a=input("Anahtar Giriniz: ")
  b=input("Yaş Giriniz")
  s1[str(a)]=b

print(s1)
"""
##### düzenli ifadeler (regular expression)
import re
"""
print(dir(re))

help(re.sub)   # sub metodunun kullanımı hakkında bilgi verir

ifade = "Saatim geri kalmış" 

duzenli=re.compile(r"a+")       # örüntüyü (patterni) belirle  'a', 'aa', 'aaa..'  + aynı harfin devamı demek
cikar=duzenli.findall(ifade)            # findall bulunan örüntüleri liste şeklinde döndürür
print(cikar)
"""
Liste = ['TATLI', 'TEL', 'TATIL', 'TOKA', 'ATA', 'TAS', 'TESBIH', 'TASIT', 'TAKI']
"""
for i in Liste:
      print(i)
      """
"""
for eleman in Liste:
      ara = re.search("^TA+[A-Z]*",eleman)         # düzenli ifade içerisinde " TA ile başlayan sonrasında ne geliyorsa " ara   (search ifadenin tamamını tarar)
      if ara:
            print(ara.group())  

for eleman in Liste:
  bul = re.match('[A-Z]+L$',eleman)                         # sonu L ile biten elemanları bulur  (match ifadenin başına bakar, uymazsa yok der)
  if bul:
    print(eleman)

"""
"""
for eleman in Liste:
  if re.match('[A-Z]E+[A-Z]',eleman):                       # önceki ve sonraki harfleri ne olursa olsun içerisinde E harfi olanları listele
    print(eleman)


for eleman in Liste:
  if re.match('TE*[A-Z]',eleman):                       # TE ile başlayan ya da E'den bir önceki yani T ile başlayanları getir
    print(eleman)


# . tek karakter yerini tutar
liste=["YASA","YARA","YAS","YASTIK"]
for eleman in liste:
  if re.match('YA.A',eleman):
    print(eleman)


Liste=["MAALESEF", "SAAT", "SAT","AAA"]
for eleman in Liste:
  if re.match('[A-Z]A{2}[A-Z]', eleman):
    print(eleman)
"""
"""
unvan="Dr. Cuneyt Bayilmis"
oku=re.match('.*\\.',unvan)               # . ilk karakter ne olursa olsun, * devamı nasıl olursa olsun, \\. nokta ile bitsin.
print(oku.group())

unvanli=["Dr. Ceren", "Muh. Cuneyt", "Prof Kerem" ]
for eleman in unvanli:
  if re.match('.*\\.',eleman):
    print(eleman)

metin="Bay, Muh. Cuneyt"
cikar=re.sub(".*,.([^.]*)\\..*","\\1",metin)
print(cikar)



metin="Python ile veri analizi"
oruntu="analizi"
yeni="bilimi"
print(re.sub(oruntu, yeni, metin))     # sub oruntunun bulunarak yeni ifade ile değiştirilmesini sağlar

metin="Fakülte, Bilgisayar Müh."
# regex ile istemediğim karakterleri silme
temizle = re.sub('[!.,]','',metin)
print(temizle)

"""
"""
# hata yönetimi
try:
      s1=int(input("payı gir: "))
      s2=int(input("paydayı gir: "))
      bol=s1/s2
      print("hata")
      print(bol)
except ZeroDivisionError:
      print("payda sıfır girilmiş")
except ValueError:
      print("değer girmelisin")
finally:
      print("sonlandı")


try:
      s1=int(input("payı gir: "))
      s2=int(input("paydayı gir: "))
      bol=s1/s2
except Exception as hata:                          # kullanıcıya python a ait hata mesajlarını göstermek için 'as' yapısı kullanılır
  print("Hata Sınıfı", type (hata))
  print("Hata Mesajı", hata)
"""
# görselleştirme
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
"""
x=[1,2,3,4,5]
y=[2,4,6,8,10]
fig=plt.figure()
plt.plot(x,y,color="red")
plt.xlabel("zaman")
plt.title("maliyet-zaman grafiği",fontsize=25)
plt.ylabel("maliyet")
"""

"""
fig=plt.figure()
x=np.linspace(0,10,100)
y=2*np.sin(x)
fig,ax=plt.subplots(2,1)
ax[0].plot(x,y, label='sinus') 

x1=[1,2,3,4,5]
y1=[2,4,6,8,10]
#plt.subplots(1,2)
ax[1].plot(x1,y1,color="red",label="lineer")

plt.legend(loc="upper left")   

"""

"""
x= np.arange(1,6)   # x=[1, 2, 3, 4, 5]
y= np.random.randint(20, size=5)     # y= [2,4,9,16,25]
y2=[1,1,6,8,10]
plt.bar(x,y,label="Mevcut",color='b')        # çubuk grafik
plt.bar(x,y2,label="Yeni",color='r')
plt.legend()
plt.xticks(x,['a','b','c','d','e']);     # x değerlerini farklı isimlendir

"""
"""
# Scatter Plots
x1= [2, 4, 6, 8]
y1=x1

x2=[1,3,5,7,9]
y2= [4,1,9,2,6]
plt.scatter(x1,y1,marker='s', color='r')
plt.scatter(x2,y2,marker='^', color='m')
plt.show()
"""

# Pasta Grafik
etiket='A','B','C','D'
pay=[55,25,15,5]    
renk=['r','g','b','m']
plt.pie(pay,labels=etiket, colors=renk,startangle=90,explode=(0,0.1,0,0),autopct='%1.2f%%');