#!/usr/bin/env python
# coding: utf-8

# In[ ]:


kaydedilmiş_kullanıcı= "globalaı"
kaydedilmiş_parola="2021"
while True:
  kullanıcı_adı= input("kullanıcı adınızı giriniz: ")
  parola= input("parolanızı giriniz: ")
  if (kullanıcı_adı==kaydedilmiş_kullanıcı) and (parola==kaydedilmiş_parola):
    print("Bligleriniz kontrol edildi, hoşgeldiniz...")
    break
  elif (kullanıcı_adı!=kaydedilmiş_kullanıcı) and (parola==kaydedilmiş_parola):
    print("kullanıcı adı yanlıs!")
  elif (kullanıcı_adı==kaydedilmiş_kullanıcı) and (parola!=kaydedilmiş_parola):
    print("Şifremi unuttum?")
    cevap=input("yes/no")
    if cevap=="yes":
      yeni_parola=input("yeni parola: ")
      kaydedilmiş_parola=yeni_parola
      print("parolanız değiştirildi.")
  else:
    print("tekrar dene")


# In[ ]:




