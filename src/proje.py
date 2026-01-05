#Kullanıcıya istediğimiz giriş bilgilerini gösteriyoruz.
print("Lütfen giriş değerlerinize 1 ve 0 giriniz!")


#Kullanıcı doğru verileri girene kadar girdi alma işlemini tekrarlıyoruz
while (True):
    #Birinci giriş bilgisini alıyoruz.
    birinci_giris = int(input("Birinci girdinizi giriniz: "))
    #İkinci giriş bilgisini alıyoruz.
    ikinci_giris = int(input("İkinci girdinizi giriniz: "))
    
    #Girilen girdilerin doğru girilip girilmediğini kontrol ediyoruz.
    #Doğru girildiğinde while döngüsünden çıkıyoruz
    if ((birinci_giris == 1 or birinci_giris == 0) and (ikinci_giris == 1 or ikinci_giris == 0)):
        break
    #Kullanıc istediğimiz girdi bilgilerini girmezse hata mesajı yazdırıp tekrardan girdi alıyoruz
    else:
        print("Lütfen giriş değerlerinize 1 ve 0 giriniz!")
        print("\n")
        
#Kullanıcıya kullanabileceği mantık kapıları ile ilgili bilgi veriyoruz.
print("AND Kapısı : 1, OR Kapısı: 2, NOT Kapısı: 3, XOR Kapısı: 4")

#Doğru kapı bilgisi girilene kadar çalışacak bir while döngüsü açıyoruz
while(True):
    kapi_bilgisi = int(input("Hangi kapıda işlem yapmak istiyorsunuz: "))
    
    #Kapı bilgisi 1 gelirse iki girdiyi and işlemine alıyoruz
    if (kapi_bilgisi == 1):
        print(f"{birinci_giris} AND {ikinci_giris} = {birinci_giris and ikinci_giris}")
        break
    #Kapı bilgisi 2 gelirse iki girdiyi or işlemine alıyoruz
    elif (kapi_bilgisi == 2):
        print(f"{birinci_giris} OR {ikinci_giris} = {birinci_giris or ikinci_giris}")
        break
    #Kapı bilgisi 3 gelirse iki girdiyi ayrı ayrı not işlemine alıyoruz. Not işleminden true veya false değeri döneceği için tam sayıya çeviriyoruz
    elif (kapi_bilgisi == 3):
        print(f"NOT {birinci_giris} = {int(not birinci_giris)}")
        print(f"NOT {ikinci_giris} = {int(not ikinci_giris)}")
        break
    #Kapı bilgisi 4 gelirse iki girdiyi xor işlemine alıyoruz. Xor işleminden true veya false değeri döneceği için tam sayıya çeviriyoruz.
    elif (kapi_bilgisi == 4):
        print(f"{birinci_giris} XOR {ikinci_giris} = {int(birinci_giris != ikinci_giris)}")
        break
    #Geçerli kapı bilgisi girilmezse hata mesajı dönderip tekrar kapı bilgisi alıyoruz
    else:
        print("Geçersiz kapı bilgisi girdiniz!")
        print("\n")

print("-"*50) #50 kere eksi koymamızı sağlıyor
print("\n")

print("A XOR (B and C) Doğruluk Tablosu")

#Doğruluk tablosu için iç içe for döngüsüne ihtiyacımız var. Her bir değişken için bir döngü olmalı
#Değişkenler 0 ile 1 arası değer alacağı için range(0,2) yazıyoruz
for A in range(0,2):
    for B in range(0,2):
        for C in range(0,2):
            #A XOR (B AND C) işlemini sonuc değişkenine atıyoruz
            sonuc = int(A != (B and C))
            #f string yardımıyla çıkan sonucu ve a, b, c içerisindeki değerleri ekrana yazdırıyoruz.
            print(f"A:{A}, B:{B}, C:{C} -> A XOR (B AND C): {sonuc}")
            
