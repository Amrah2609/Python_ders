# Lüğətdən istifadə edərək tələbələrin dərs cədvəlini idarə edən bir Python proqramı yazın. Aşağıdakı funksiyaları həyata keçirin:
# Funksiyalar:
# add_subject:
# 3 arqument qəbul edir: lüğət (dictionary), tələbə adı (name), fənn adı (subject).
# Tələbəyə yeni fənn əlavə edir.
# remove_subject:
# 3 arqument qəbul edir: lüğət (dictionary), tələbə adı (name), fənn adı (subject).
# Tələbədən fənni silir.
# get_subjects:
# 2 arqument qəbul edir: lüğət (dictionary), tələbə adı (name).
# Tələbənin bütün fənlərini qaytarır.
# get_all_students:
# 1 arqument qəbul edir: lüğət (dictionary).
# Bütün tələbələrin adlarını və onların fənlərini qaytarır.
# count_subjects:
# 2 arqument qəbul edir: lüğət (dictionary), tələbə adı (name).
# Tələbənin neçə fənni olduğunu qaytarır.




def add_subject(dictionary, name, subject):
    if name not in dictionary:
        dictionary[name] = []
        dictionary[name].append(subject)


def remove_dictionary(dictionary, name, subject):
    if name in dictionary and subject in dictionary:
        dictionary[name].remove(subject)

def get_subjects(dictionary, name):
    if name in dictionary:
        return dictionary[name]
    else:
        return []
    
def all_students(dictionary):
    return dictionary

def len_subjects(dictionary, name):
    if name in dictionary:
        return len(dictionary[name])
    else:
        return 0
    

dictionary = {}

add_subject(dictionary , "Ali", "Riyaziyyat")
add_subject(dictionary , "Ali", "Fizika")
add_subject(dictionary , "Leyla", "Kimya")

remove_dictionary(dictionary, "Ali", "Fizika")

print(get_subjects(dictionary, "Ali"))

print(all_students(dictionary))

print(len_subjects(dictionary, "Leyla"))  
