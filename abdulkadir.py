# Soru 1

#Boyu ve kilosu verilen bir kişinin vücut kitle indeksini ölçen program
# kilo=float(input("Lütfen kilonuzu giriniz:"))
# boy=float(input("Lütfen boyunuzu giriniz(CM cinsinden):"))

# boy = boy/100   #metreye çevirmek için bunu kullandık.
# vki = kilo/(boy**2)

# if vki > 30:
#   print(vki,"Obez")

# elif 25 < vki < 30:
#   print(vki,"Fazla")

# elif 18 <= vki <= 25:
#   print(vki,"Normal")
 
# else:
#   print(vki,"Zayıf")


# Soru 2

# sayi = int(input("Sayı giriniz: "))
# rakamlar = []

# while sayi > 0:
#     rakam = sayi % 10
#     rakamlar.append(rakam)
#     sayi = sayi//10

# for rakam in rakamlar:
#     print("x"*rakam)
# print(rakamlar)


# Soru 3

# liste = []

# while True:
#   rakam = input("0 ile 9 arasında rakam giriniz. Bitirmek için q'ya basınız: ")
#   if rakam == "q":
#     break

#   elif rakam.isdigit() and 0 <= int(rakam) <= 9:
#     liste.append(rakam) 
#   else:
#     print("Hatalı giriş yaptınız.")

# str_sayi = ""
# for rakam in liste:
#   str_sayi += rakam

# sayi = int(str_sayi)

# karekök = sayi ** 0.5

# print(karekök)

# Soru 4

# Son sorudan pek birşey anlamadım