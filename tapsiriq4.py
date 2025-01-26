# Task 1:
# Sadə kalkulyator proqramı yazın. funksiyanin 3 arqumenti olsun. a, b, və operation. a və b tələb olunan arqument olsun operation isə vacib olmasın əgər funksiyanı çağıran zaman operation yoxdursa a və b ni toplasın. operation 4 cür ola bilər toplama vurma çıxma və bölmə sonda nəticəni ekrana çap eləsin. hər 4 variantdada işləsin. Əgər operator yanlış daxil edilərsə ekranda `yanlış seçim zəhmət olmasa düzgün əməliyyatları seçin` çixsın.
# Input:
# calculator(5, 6) # 11
# calculator(10, 5, "-") # 5
# calculator(10, 5, "/") # 2.0
# calculator(10, 5, "*") # 50
# calculator(10, 5, "+") # 15
# calculator(10, 5, "test") # yanlış seçim zəhmət olmasa düzgün əməliyyatları seçin

# ========================================

# def calculator(a, b, operation='+'):
#     if operation == "+":
#         result = a + b
#     elif operation == "-":
#         result = a - b
#     elif operation == "*":
#         result = a * b
#     elif operation == "/":
#         if b == 0:
#             return "Xəta: sıfıra bölmə olmaz!"
#         result = a / b
#     else:
#         return "yanlış seçim zəhmət olmasa düzgün əməliyyatları seçin"

#     return result

# print(calculator(5, 6))  # 11
# print(calculator(10, 5, "-"))  # 5
# print(calculator(10, 5, "/"))  # 2.0
# print(calculator(10, 5, "*"))  # 50
# print(calculator(10, 5, "+"))  # 15
# print(calculator(10, 5, "test")) 


# Task 2.
# Verilmiş yazıdakı sözlərin sayını tapan funksiya yaradın. İlkin argument söz olsun. nəticədə sayını qaytarsın

# Input:
# find_word_count("Hello world is this a sample text") # 7
# ========================================

# def find_count(text):
#     words = text.split()
#     return len(words)
# print(find_count("Hello world is this a sample "))


# Task 3.
# Siyahinin içərisindən axtarış edən funksiya yaradın. 2 arqumenti olsun. array, word. Əgər verilmiş söz siyahıda varsa o zaman Boolean True qaytarsın yoxdursa onda False.

# Input:
# find_in_list([5, 6, 7, 2, 4], 2) # True
# find_in_list([5, 6, 7, 2, 4], 9) # False
# find_in_list(['alma', 'armud'], 'armud') # True
# find_in_list(['alma', 'armud'], 'nar') # False
# ========================================

# def find_in_list(array, word):
#     return word in array 

# # Test nümunələri
# print(find_in_list([5, 6, 7, 2, 4], 2))  # True
# print(find_in_list([5, 6, 7, 2, 4], 9))  #False
# print(find_in_list(['alma', 'armud'], 'armud'))  # True
# print(find_in_list(['alma', 'armud'], 'nar'))  # False


# Task 4. 
# Funksiya siyahının içərisindəki hər bir ədədləri qüvvətə yüksəltsin və sonda alınan nəticəni toplasın. bir arqumenti olacaq. məsələn
# Input:
# pow_the_list_and_find_maximum([1,2,9,4,5,6]) # 163
# pow_the_list_and_find_maximum([6,23,235,74,36,14]) # 62758
# pow_the_list_and_find_maximum([5,26,223,76,634]) # 

# def power_number(numbers):
#     squared_numbers = [x**2 for x in nu]
#     return sum(squared_numbers)
# print(power_number([1,2,9,4,5,6])) # 163



# Task 5.
# Lüğətdən istifadə edərək tələbə qiymətlərini idarə edən Python proqramı yazın. Aşağıdakı funksiyaları həyata keçirin. Hər birini izahlı şəkildə yazmışam aşağıdaki koddan istifadə edərək funksiyalar yaradın. add_student -> 3 argumentli (dictionary, name, grade).
# remove_student -> 2 argumentli (dictionary, name)
# get_grade -> 2 argumentli (dictionary, name)
# average_grade -> 1 argumentli (dictionary)
# get_all_students -> 1 argumentli (dictionary)

# Aşağıdakı kodda hər bir funksiyanın nə qaytaracağını və nəcür işləməli olduğunu yazmışam sizə sadəcə funksiyaları yazmaq lazımdı əgər kod işləsə həll olmuş sayılır.

# Input:
# # Boş lüğəti yaradın
# grades = {}

# # İçərisinə tələbələri əlavə edin
# add_student(grades, "Alice", 85)
# add_student(grades, "Bob", 90)
# add_student(grades, "Charlie", 78)

# # Lüğəti çap edin
# print(grades)  
# # Output: {'Alice': 85, 'Bob': 90, 'Charlie': 78}

# # Tələbəni çıxarın
# remove_student(grades, "Bob")
# print(grades)  
# # Output: {'Alice': 85, 'Charlie': 78}

# # tələbənin qiymətini çap edin.
# print(get_grade(grades, "Alice"))  
# # Output: 85
# # Əgər tələbə yoxdursa o zaman `Not found` çap edin
# print(get_grade(grades, "David"))  
# # Output: Not found

# # Tələbərin Orta qiymətlərini hesablayın
# print(average_grade(grades))  
# # Output: 81.5

# # Bütün tələbələrin adlarını çap edin
# print(get_all_students(grades))  
# # Output: ['Alice', 'Charlie']


