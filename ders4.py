# def find_repeated_words(text):

#     text = "Hello world"

#     tekrarlanan = []
#     for item in set(text):
#         if text.count(item) > 1:
#             tekrarlanan.append(item)
#     return tekrarlanan
# print(find_repeated_words("Hello world"))

#argumentsiz funksiya
# def function():
#     pass
# print(type(function()))

 
# def  function_with_argument(name, surname, age):
#     return f"Name: {name}, Surname: {surname}, Age: {age}"
# print(function_with_argument("test" ,"Jack", 20 ))


# def function_with_keyword(name = "Test", surname = "Jack"):
#     return f"{name} {surname}"
# print(function_with_keyword())


# def calculator(a, b, c = '+'):
#     if c=="+":
#         return a+b
    
# print(calculator(5,6))


# def function_args(*args):
#     print(args)
#     return
# function_args(10,12,13,13,4,1,2,4,5,3)


def function_sonsuz_sayda_kwargs( **kwargs):
    for key, value in kwargs.items():
        print(key, value)
    return kwargs
function_sonsuz_sayda_kwargs(name = "test", surname = "jack", age = 20)