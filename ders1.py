# Tapshiriqlar
# ------------------------------------------------------------------------------------
# Task 1: Sade calculator proqrami
# Description: Istifadeciden 2 reqem sorushsun, 3-cude operasiyani sorushsun eger `topla` dirsa toplasin, `cix` dirsa cixsin, `bolme` dirsa bolsun, `vurma` bu isharedirse reqemleri bir birine vursun. neticeni sonda ekrana cap elesin.

# Input: 5, 10, topla
# Output: 10

# Input: 20, 10, cix
# Output: 10

# Input: 20, 10, bolme
# Output: 10

# Input: 20, 10, vurma
# Output: 200

# ------------------------------------------------------------------------------------
# Task 2. İstifadəçidən aylıq gəlirini və xərclərini (məsələn, kirayə, ərzaq və nəqliyyat) soruşun. Xərclərdən sonra qalan qalıqlarını hesablayın və göstərin. məsələn

# # Input: gelir = 5000, kiraye = 1500, magaza = 1000, ictimai_neqiliyyat = 500
# # Output: qaliq = 2000

# ------------------------------------------------------------------------------------

# Task 3. İstifadəçidən yaşını və növbəti doğum gününə neçə ay qaldığını soruşun. Onların ad gününə qalan günlərin sayını hesablayın və göstərin (sadəlik üçün ayı 30 gün qəbul edin).

# # Input: yas = 25, nece_ay_qalib = 5
# # Output: Ad gunune 150 gun qaldi

# ------------------------------------------------------------------------------------
# Task 4. Teperatur olcən proqram
# Temperaturları Selsi və Fahrenheit arasında çevirən proqram yazın. İstifadəçi çevrilmə istiqamətini seçməli və temperaturu daxil etməlidir. Bundan sonra proqram çevrilmiş dəyəri göstərməlidir.

# Hesablama qaydası:
# 	Selsidən Fahrenheitə: (C × 9/5) + 32
# 	Farenheitdən Selsiyə: (F - 32) × 5/9

# # Input: C, 25°
# # Output: 77°F

# # Input: F, 77
# # Output: 25°C
# ------------------------------------------------------------------------------------

# Task 5. İstifadəçinin 1-dən 10-a qədər gizli nömrəni təxmin etməyə çalışdığı proqram yaradın. Hər təxmindən sonra onların çox yüksək, çox aşağı və ya düzgün olduğunu bildirin. İstifadəçi düzgün təxmin etdikdə oyun bitməlidir.

# # Secret number: 7
# # Input: 4, 9, 7
# # Output: "Çox aşağı", "Çox yüksək", "Təbriklər qazandınız düzdü"


#tapsiriq1

# number1= float(input("1-ci Reqem daxil edin: "))
# number2 = float(input("2-ci Reqem daxil edin: "))
# oparation = input("Emelyati daxil edin: ")
# if oparation == "topla":
#     netice = number1 + number2
# elif oparation == "cix":
#     netice = number1 - number2
# elif oparation == "bolme":
#     if  number2 != 0:
#         netice = number1 / number2
#     else:
#         netice = "Sifira bolmek mumkun deyil "
# elif oparation == "vurma":
#     netice = number1 * number2
# else:
#     netice = "Sehv emeliyyat"
# print(netice)



# #1
# number = int(input("Reqem daxil edin: "))

# if number > 0:
#     print("Positive number ")
# else:
#     print("Negative numbers")

# #2
# def hello_world(name):
#     return f"Hello, {name}!"

# print(hello_world("Python"))

# #3
# name = input("What is your name? ")

# print(f"Hello, {name}")

# #4

# price = input("Enter the price: ")
# price = float(price)

# total_price = price + 5000
# print(total_price)

# #5
# choice = input("Choose an option (1-Start, 2-Exit): ")
# if choice == "1":
#     print("Starting the program... ")
# elif choice == "2":
#     print("Exiting... ")
# else:
#     print("Invalid option")
