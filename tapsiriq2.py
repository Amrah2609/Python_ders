# Task 2. Yuxarıdakı tapşırığa əlavə olaraq verilmiş textlərin içərisində təkrarlanan simvolları `*` ilə əvəz edin. Əgər təkrarlanan simvol yoxdursa sözün özünü çap edin.

# Input: Hello
# Output: He**o

# Input: programming
# Output: p*og*a**ing

# Input: aaaaaa
# Output: ******

# Input: bananaapple
# Output: b********le

# Input: python
# Output: python


# def tekrarlanan(soz):
#     tekrar_olunan_elementler = []
#     for i in soz:
#         if i in tekrar_olunan_elementler:
#             continue
#         count = soz.count(i)
#         if count > 1:
#             tekrar_olunan_elementler.append(i)
#     return len(tekrar_olunan_elementler)
# print(tekrarlanan("hello"))



# def replace_symbol(word):
#     yoxlanilmis = []  
#     netice = [] 
#     for i in word:
#         if word.count(i) > 1: 
#             netice.append("*")  
#         else:
#             netice.append(i)  
#     return ''.join(netice)  


# print(replace_symbol("bananaapple"))



# student = {