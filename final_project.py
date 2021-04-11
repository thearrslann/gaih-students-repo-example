#!/usr/bin/env python
# coding: utf-8

# In[23]:


import time
print("""**********************************************************
 Sınava hoşgeldiniz! 
 Lütfen büyük küçük harf duyarlılığına dikkat edin!
**********************************************************""")
isim = input("isminiz:  ")
soyisim = input("soyisminiz:  ")
no = int(input("okul numaranız:  "))
dogru_cevaplar=[]

soru_1 = input("Kgtü üniversitesi hangi şehirdedir? ")
soru_2 = input("En iyi Türk introductionto python eğitimi veren eğitimci kimdir? ")
soru_3 = input("dönüşüm kitabının yazarı kimdir? ")
soru_4 = input("google aı hub Yöneticisi kimdir? ")
soru_5 = input("T.B.M.M açılımı nedir?  ")
soru_6 = int(input("google aı hub hangi yılda kurulmuştur? "))
soru_7 = int(input("aı hub'ın pyhtona giriş derleri toplam kaç saat sürmüştür? "))
soru_8 = input("istiklal marşının yazarı kimdir? ")
soru_9 = int(input("1 saat kaç dakikadır? "))
soru_10 = input("Print('hello'*3)'un çıktısı nedir' ")


if soru_1== "Konya":
    dogru_cevaplar.append(soru_1)


if soru_2== "Ömer Cengiz":
    dogru_cevaplar.append(soru_2)


if soru_3== "Franz Kafka":
    dogru_cevaplar.append(soru_3)


if soru_4== "Fuat Beşer":
    dogru_cevaplar.append(soru_4)
   

if soru_5== "Türkiye Büyük Millet Meclisi":
    dogru_cevaplar.append(soru_5)
  
if soru_6== 2020:
    dogru_cevaplar.append(soru_6)
    
if soru_7== 10:
    dogru_cevaplar.append(soru_7)
    
if soru_8== "Mehmet Akif ERSOY":
    dogru_cevaplar.append(soru_8)
    
if soru_9== 60:
    dogru_cevaplar.append(soru_9)
    
if soru_10=="'hellohellohello'":
    dogru_cevaplar.append(soru_10)

puan = len(dogru_cevaplar)*10
print("sonucunuz hazırlanıyor...")
def basarı_durumu():
    if len(dogru_cevaplar)>5:
        print(f"{no} numaralı {isim} {soyisim}, {len(dogru_cevaplar)} tane soruyu doğru bilerek {puan} puan aldın ve sınavı başarıyla tamamladın...")
    else :
        print(f"{no} numaralı {isim} {soyisim}, {len(dogru_cevaplar)} tane doğru soru bilerek {puan} puan ile başarısız oldun...")
time.sleep(1.3)
basarı_durumu()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




