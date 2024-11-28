import random
sifre_karakterleri = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while True:
    try:
        hane = int(input("Kaç haneli şifre oluşturacaksın? "))
        
        if hane <= 0:
            print("Hata: Şifre uzunluğu pozitif bir sayı olmalıdır. Tekrar deneyin.")
        else:
            
            sifre = ""
            for i in range(hane):
                sifre += random.choice(sifre_karakterleri)
            print("Şifren:", sifre)
            break  
    except ValueError:
        print("Hata: Geçerli bir sayı girmediniz. Lütfen bir tam sayı girin.")
