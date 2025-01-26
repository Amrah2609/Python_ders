# Task 1:
# Sadə kalkulyator proqramı yazın. funksiyanin 3 arqumenti olsun. a, b, və operation. a və b tələb olunan arqument olsun operation isə vacib olmasın əgər funksiyanı çağıran zaman operation yoxdursa a və b ni toplasın. operation 4 cür ola bilər toplama vurma çıxma və bölmə sonda nəticəni ekrana çap eləsin. hər 4 variantdada işləsin. Əgər operator yanlış daxil edilərsə ekranda `yanlış seçim zəhmət olmasa düzgün əməliyyatları seçin` çixsın.
# Input:
# calculator(5, 6) # 11
# calculator(10, 5, "-") # 5
# calculator(10, 5, "/") # 2.0
# calculator(10, 5, "*") # 50
# calculator(10, 5, "+") # 15
# calculator(10, 5, "test") # yanlış seçim zəhmət olmasa düzgün əməliyyatları seçin


def calcutor(a, b, operation = "+"):
    if operation == "+" :
        result = a+b
    elif operation == "-":
        result = a-b
    elif operation == "*":
        result = a*b
    elif operation == "/":
        if b == 0:
            return "Sıfıra bölmək mümkün deyil"
        result = a / b
    else:
        return "yanlış seçim zəhmət olmasa düzgün əməliyyatları seçin"
    return result
try:
    a = int(input("1-ci eded: "))
    b = int(input("2-ci eded: "))
    operation = input("Emeliyyati daxil edin: (+,-,*,/)")
    result = calcutor(a, b, operation)
    print(result)
except ValueError:
    print("Zehmet olmasa duzgun emeliyyat daxil edin!!!!!!")


