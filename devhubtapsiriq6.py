# Tapsiriq1:
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

#______________________________________________________________________________________________________________________________

# Tapsiriq 2: 
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


#______________________________________________________________________________________________________________________________


# Tapsiriq 3:
# Məqsəd: Baza sinif (superclass) və ondan irsi götürən törəmə siniflərin (subclass) yaradılmasını məşq etmək.

# Təlimatlar:

# Animal adlı baza sinfi yaradın, name və age atributları olsun.
# Animal sinfində make_sound() adlı metod yaradın. Məsələn, print("Some generic sound").
# Dog və Cat adlı iki törəmə sinif yaradın və Animal-dan miras alsınlar.
# make_sound() metodunu hər sinifdə yenidən (override) təyin edin. Məsələn, Dog üçün print("Bark!"), Cat üçün print("Meow!").
# Dog və Cat obyektləri yaradın, make_sound() metodlarını çağırın və fərqli nəticələr aldığınızı yoxlayın.

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def make_sound(self):
#         print("Some generic sound")

# class Dog(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)
        
#     def melumat(self):
#         print(f"Dog melumat: Name = {self.name}, Age = {self.age}")

#     def make_sound(self):
#         print("Bark!")

# class Cat(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#     def melumat(self):
#         print(f"Cat melumat: Name = {self.name}, Age = {self.age}")

#     def make_sound(self):
#         print("Meov")


# dog = Dog("Hex", 5)
# cat = Cat("Kedi", 4)

# dog.melumat()
# cat.melumat()
# dog.make_sound()
# cat.make_sound()



#______________________________________________________________________________________________________________________________

# Tapsiriq 4:

# Məqsəd: Sinifə məxsus olan verilənlərlə hər bir obyektə məxsus olan verilənlərin fərqini göstərmək.

# Təlimatlar:

# Car adlı sinif yaradın və total_cars adlı sinif dəyişəni təyin edin; bu dəyişən yaradılan Car obyektlərinin ümumi sayını saxlasın.
# __init__ metodunda hər dəfə yeni Car obyekti yaradıldıqda total_cars dəyişənini artırın.
# Obyekt səviyyəsində (instance attribute) model və year atributları əlavə edin.
# Bir neçə Car nümunəsi yaradın və total_cars-ın necə dəyişdiyini, model və year kimi atributların isə hər obyektdə fərqli olduğunu nümayiş etdirin.


# class Car:
#     total_cars = 0

#     def __init__(self, model, year):
#         self.model = model
#         self.year = year
        
#         Car.total_cars += 1

#     def display_info(self):
#         print(f"Model: {self.model}, Year: {self.year}")

# car1 = Car("Toyota ", 2020)
# car2 = Car("BMW", 2018)
# car3 = Car("Ford ", 2022)

# car1.display_info()
# car2.display_info()
# car3.display_info()

# print(f"Umumi say: {Car.total_cars}")