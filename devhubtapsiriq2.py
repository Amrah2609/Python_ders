# Bir tələbənin imtahan nəticələri verilmişdir. Aşağıdakı dictionary-də fənlər və onların qiymətləri saxlanılır.
#  
# Riyaziyyat  85, Fizika 78, Kimya 90, İngilis dili  88, Tarix 76

# Tapsiriq1

# dictionary = {
#     "Riyaziyyat": 85,
#     "Fizika": 78,
#     "Kimya": 90,
#     "Ingilis dili": 88,
#     "Tarix": 76
# }

# for fen, qiymeti in dictionary.items():
#     print(f"{fen}: {qiymeti}")



# Tapşırıq:
# İstifadəçidən yaşını daxil etməsini istəyin və aşağıdakı qaydalara əsasən ona mesaj verin:

# 0-12 yaş: "Uşaqsan"
# 13-19 yaş: "Gəncsən"
# 20-64 yaş: "Böyüksən"
# 65 və yuxarı: "Yaşlısan"


# age = int(input("Zəhmət olmasa yaşınızı daxil edin: "))
# if 12 > age > 0:
#     netice = "Uşaqsan"
# elif 19 > age > 13:
#     netice = "Gəncsən"
# elif 64 > age > 20:
#     netice = "Böyüksən"
# else:
#     netice = "Yaşlısan"
# print(netice)




# Tapşırıq
# 1-dən 10-a qədər olan cüt ədədləri çap edən bir döngü yazın.

for i in range(10):
    if i % 2 == 0:
        print(i)