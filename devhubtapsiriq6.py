# Məqsəd: Sinifin (class) necə yaradılacağı, nümunələrin (instances) necə istifadə ediləcəyi və atributlara necə müraciət ediləcəyi barədə baza anlayışlarını öyrənmək.

# Təlimatlar:

# Person adlı sinif yaradın.
# Bu sinifdə name və age atributları olsun.
# __init__ metodu yazaraq bu atributları təyin edin.
# Müxtəlif name və age dəyərləri ilə iki-üç Person obyekti yaradın.
# Hər obyektin atributlarını ekranda (print vasitəsilə) göstərin.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# object1 = Person("Nihat", 18)
# object2 = Person("Leyla", 25)
# object3 = Person("Ramal", 30)

# print(f" Name: {object1.name}, Age: {object1.age}")
# print(f" Name: {object2.name}, Age: {object2.age}")
# print(f" Name: {object3.name}, Age: {object3.age}")

# Məqsəd: Obyektin daxilindəki verilənlər üzərində əməliyyat icra edən metodlar yazmaq və enkapsulyasiya prinsiplərini göstərmək.

# Təlimatlar:

# Birinci tapşırıqda yaratdığınız Person sinfinə və ya yeni bir sinifə (məsələn, BankAccount) keçid edin.
# O sinfə obyektin (instance) məlumatlarından istifadə edən metodlar əlavə edin (məsələn, deposit, withdraw, check_balance və s.).
# Əsas blokda (main) və ya test hissəsində bu metodlardan istifadə nümunələri göstərin.



# class BankAccount:
#     def __init__(self, account_houlder, balance=0):
#         self.account_houlder = account_houlder
#         self.balance = balance

#     def deposit(self, mebleg):
#         if mebleg > 0:
#             self.balance += mebleg
#             print(f"{mebleg} AZN deposit olundu. yeni balans: {self.balance} AZN.")
#         else:
#             print("Deposit məbləğ mənfi ola bilməz.")
        

#     def cixarmaq(self, mebleg):
#         if mebleg > 0 and mebleg <= self.balance:
#             self.balance -= mebleg
#             print(f"{mebleg} AZN çıxarildi, Yeni balans: {self.balance} AZN.")
#         elif mebleg > self.balance:
#             print("Kifayət qədər vəsait yoxdur.")
#         else:
#             print("Çıxarılan məbləğ müsbət olmalıdırş")
    
#     def chech_balance(self):
#         print(f"Cari balans: {self.account_houlder}: {self.balance} AZN.")

# account1 = BankAccount("Nihat", 1000)
# account1.chech_balance()
# account1.deposit(500)
# account1.cixarmaq(100)
# account1.cixarmaq(1000000)
# account1.chech_balance()
