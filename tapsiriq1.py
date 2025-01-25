# print ("by M!rza calculator")
# import math
# def a(x, y):
#     return x + y

# def b(x, y):
#     return x - y

# def c(x, y):
#     return x * y

# def d(x, y):
#     return x / y
# def q(x, y):
#     return math.pow(x,y)
# def k(x,y):
#     return math.pow(x,1/y)
# def f(x):
#     return math.factorial(x)
    
# try:
#     reqem1 = float(input("Birinci ədədi daxil edin: "))
# except ValueError:
#     print("Zəhmət olmasa rəqəm daxil edin.")
        


# while True:   
#     print("Əməli seçin:")
#     print("1.topla")
#     print("2.çıx")
#     print("3.vur")
#     print("4.böl")
#     print("5.qüvvətə yüksəlt")
#     print("6.kök al")
#     print("7.faktorialı tap")    
#     seçim= input("(1/2/3/4/5/6/7): ")
#     if seçim in ('1', '2', '3', '4'):
#         try:
            
#              reqem2 = float(input("İkinci ədədi daxil edin: "))
#         except ValueError:
#             print("Zəhmət olmasa rəqəm daxil edin.")
#             continue

#         if seçim == '1':
#             print(f"{reqem1}+{reqem2}={a(reqem1, reqem2)}")
            

#         elif seçim == '2':
#             print(f"{reqem1}-{reqem2}={b(reqem1, reqem2)}")

#         elif seçim == '3':
#             print(f"{reqem1}*{reqem2}={c(reqem1, reqem2)}")

#         elif seçim == '4':
#             print(f"{reqem1}÷{reqem2}={d(reqem1, reqem2)}") 
#     if seçim == '5' :
#         try:
#             reqem2 = float(input("qüvvətin dərəcəsini daxil edin: "))
#         except ValueError:
#             print("Natural ədəd daxil edin.")
#             break
#         print(f"{reqem1}^{reqem2}={q(reqem1,reqem2)}")    
#     elif seçim =='6':
#         try:
#             reqem2 = float(input("kökün dərəcəsini daxil edin: "))
#         except ValueError:
#             print("Rəqəm daxil edin.")
#             continue
#         print(f"{reqem1}^1/{reqem2}={k(reqem1,reqem2)}")
#     elif seçim =='7':
#         try:
        
#             reqem1=int(input("Ədədi daxil edin:"))
#         except ValueError:
#             print("Tam ədəd daxil edin.")
#             continue
            
#         print(f"{reqem1}!={f(reqem1)}")
#     if seçim in('1', '2', '3', '4', '5' ,'6','7'):
#         pass
#     else:
#         print ("Səhv seçim.")  
#     break


#Tapsiriq 1

# number1 = float(input("1-ci Reqem daxil edin: "))
# number2 = float(input("2-ci Reqem daxil edin: "))
# operation = input("Emeliyyati daxil edin: ")

# if operation == "topla":
#     netice = number1 + number2
# elif operation == "cixma":
#     netice = number1 - number2
# elif operation == "vurma":
#     netice =  number1 * number2
# elif operation == "bolme":
#     if number2 != 0:
#         netice = number1 / number2
#     else:
#         netice = "Sifira bolmek mumkun deyil"
# else:
#     netice = "Sehv emelliyat"
# print(netice)


#tapsiriq 2

# gelir = int(input("Ayliq gelir: "))
# kira = int(input("Kira xerci: "))
# magaza = int(input("Magaza xerci: "))
# ictimai_neqliyyat = int(input("Ictimai neqliyyat xerci: "))
# xerc = kira + magaza + ictimai_neqliyyat
# qaliq = gelir - xerc
# print(f" qaliq_mebleq: {qaliq}")


#tapsiriq 3

# yas = int(input("Yasinizi daxil edin: "))
# ay= int(input("Ayi daxil edin: "))
# qalan_ay = ay * 30
# print(f"sizin novbeti ad gununuze {qalan_ay} qalib. ")


#tapsiriq 4

# cevrilme = int(input("1 - Selsidən Fahrenhayt'a, 2 - Fahrenhaytdan Selsiyə: "))

# if cevrilme == 1:
#     selsi = float(input("Selsi temperaturunu daxil edin: "))
#     fahrenheit = (selsi * 9/5) + 32
#     print(f"{selsi}° C, fahrenhaytda {fahrenheit:.2f}° F")
# elif cevrilme == 2:
#     fahrenheit = float(input("Fahrenhayt temperaturunu daxil edin: "))
#     selsi = (fahrenheit - 32) * 5/9
#     print(f"{fahrenheit}° F, selsidə {selsi:.2f}° C")
# else:
#     print("Yanlış seçim etdiniz, 1 və ya 2 daxil edin.")


#tapsiriq 5

# secret_number = 7
# while True:
#     istifadeci = int(input("1-den 10-a qeder reqed texmin edin: "))
#     if istifadeci > secret_number:
#         print("Verdiiniz reqem yuksektir: ")
#     elif istifadeci < secret_number:
#         print("Verdiyiniz reqem kicikdir: ")
#     else:
#         print("Tebrikler duz tapdiniz: ")
#         break



# tapsiriq 6

# number = int(input("Bir eded daxil edin: "))
# if number % 2 == 0 and number % 3 == 0 and number % 5 == 0:
#     print("Reqem 2, 3, 5 bolunur.")
# elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
#     print("bolunur")
# else:
#     print("Bu reqem bu ededlerin hec birine bolunmur.")




#tapsiriq 7
# number1 = int(input("1-ci ededi daxil edin: "))
# number2 = float(input("2-ci ededi daxil edin: "))

# if number1 > 0 and number2 > 0:
#     cem = number1 + number2
#     print(f" Reqemlerin cemi: {cem}")
# elif number1 < 0 and number2 < 0:
#     hasil = number1 * number2
#     print(f"Reqemlerin hasili: {hasil}")
# else:
#     print("Ferqli isareli reqemler daxil etmisiz.")





#tapsiriq 8

# number1 = float(input("Illik kapitalini daxil edin: "))
# faiz_number = float(input("Illik faiz derecesini hesab;layin: "))

# if faiz_number > 15:
#     print("Bu cox yuksek faizdir.")
# elif faiz_number < 5:
#     print("Bu cox asagi faizdir.")
# else:
#     gelir = number1 * faiz_number / 100
#     print(f"Faiz geliri: {gelir:.2f}")


# Dəyərli Mal Yoxlayıcı

# İstifadəçidən bir malın qiymətini (float) və keyfiyyət balını (int, 1-10 arasında) daxil etməsini istəyin. Əgər:

#     Qiymət 100 AZN-dən azdır və keyfiyyət 8-dən böyükdürsə: "Bu, çox yaxşı bir seçimdir!"
#     Qiymət 100 AZN-dən çoxdur və keyfiyyət 5-dən azdırsa: "Bu, yaxşı seçim deyil."
#     Digər hallarda: "Bu məhsulu daha yaxından araşdırmalısınız."

#tapsiriq 9
qiymet = float(input("Malin qiymerini daxil edin: "))
keyfiyyet = int(input("1-10 Arasi reqem daxil edin: "))
if qiymet < 100 and keyfiyyet > 8:
    print("Bu, cox yaxsi bir secimdir")
elif qiymet > 100 and keyfiyyet < 5:
    print("Bu, yaxsi secim deyil.")
else:
    print("Bu, mehsulu daha yaxsi arasdirmalisiniz.")