# from getpass import getpass
# username = input("Username: ")
# password = getpass()
# print(username)


# import hashlib
# password = "Secret word"
# print(password.encode("utf-8"))

# hash = hashlib.sha256(password.encode("utf-8"))
# print(hash.hexdigest())


# def check_dictionary(obj):
#     name = ""  
#     try:
#         if obj["name"]:
#             name = obj["name"]  
#             print("Yes, name is in object")
#     except Exception as error:  
#         print(error)
#     return name


# result1 = check_dictionary({
#     "test": 12345
# })

# result2 = check_dictionary({
#     "name": 12345
# })

# result3 = check_dictionary({
#     "test2": 12345
# })

# print(result1) 
# print(result2)  
# print(result3)  




import logging


log =logging.getLogger("example")
log.setLevel("DEBUG")

def function(a,b):
    log.debug(f"Birinci argument: {a}")
    log.debug(f"Ikinci argument: {b}")

    try:
        return a/b
    except Exception as error:
        pass
print(function(10, 5))
print("Done")