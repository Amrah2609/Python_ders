# Task 1: Lüğət 

# Input: 
# person = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }
# Output:
# Aşağıdakıları çap edin:
# Adamın adı.
# Adamın yaşı.
# ========================================

# person = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }

# print(f" Adamin adi: {person['name']}, Adamin yasi: {person['age']}" ) 


# Task 2: İç-içə Lüğət

# Input:
# student = {
#     "name": "John",
#     "grades": {
#         "math": 90,
#         "science": 85,
#         "history": 88
#     }
# }
# Output:
# Tələbənin elmi dərəcəsini çap edin.
# ========================================


# student = {
#     "name": "John",
#     "grades": {
#         "math": 90,
#         "science": 85,
#         "history": 88
#     }
# }

# print(f"Tələbənin elmi dərəcəsi: {student['grades']['science']}")




# Task 3: Lüğət üzərində dövrlər

# Input:
# inventory = {
#     "apples": 10,
#     "bananas": 5,
#     "oranges": 8
# }
# Output:
# Hər meyvəni və onun miqdarını aşağıdakı formatda çap edin:
# apples 10
# bananas 5
# oranges 8

# ========================================


# inventory = {
#     "apples": 10,
#     "bananas": 5,
#     "oranges": 8
# }

# for fruit, quantily in inventory.items():

#     print(f"{fruit} {quantily}")



# Task 4: Lüğətlərin siyahısını təhlil etmək

# Input:
# employees = [
#     {"name": "Alice", "role": "Developer", "age": 30},
#     {"name": "Bob", "role": "Designer", "age": 28},
#     {"name": "Charlie", "role": "Manager", "age": 35}
# ]

# Output:
# 30 yaşdan kiçik bütün işçilərin adlarını çap edin.
# ========================================


# employees = [
#     {"name": "Alice", "role": "Developer", "age": 30},
#     {"name": "Bob", "role": "Designer", "age": 28},
#     {"name": "Charlie", "role": "Manager", "age": 35}
# ]
# for employee in employees:
#     if employee["age"] < 30:
#         print(employee["name"])






# Task 5: Mürəkkəb İç-içə Lüğət

# Input:
# data = {
#     "company": "TechCorp",
#     "departments": {
#         "development": {
#             "employees": [
#                 {"name": "Alice", "role": "Developer", "projects": ["App1", "App2"]},
#                 {"name": "Bob", "role": "Developer", "projects": ["App3"]},
#                 {"name": "Mark", "role": "Lead", "projects": []}
#             ]
#         },
#         "design": {
#             "employees": [
#                 {"name": "Charlie", "role": "Designer", "projects": ["Design1"]},
#                 {"name": "Diana", "role": "Designer", "projects": []}
#             ]
#         }
#     }
# }

# Output:
# "development" şöbəsindəki bütün işçilərin adlarını işlədikləri layihələrin sayı ilə birlikdə çap edin. Əgər işçinin heç bir layihəsi yoxdursa, "Layihə yoxdur" yazın.
# ========================================



data = {
    "company": "TechCorp",
    "departments": {
        "development": {
            "employees": [
                {"name": "Alice", "role": "Developer", "projects": ["App1", "App2"]},
                {"name": "Bob", "role": "Developer", "projects": ["App3"]},
                {"name": "Mark", "role": "Lead", "projects": []}
            ]
        },
        "design": {
            "employees": [
                {"name": "Charlie", "role": "Designer", "projects": ["Design1"]},
                {"name": "Diana", "role": "Designer", "projects": []}
            ]
        }
    }
}

for employee in data["departments"]["development"]["employees"]:
    name = employee["name"]
    projects_count = len(employee["projects"])
    
    if projects_count == 0:
        print(f"{name}: Layihə yoxdur")
    else:
        print(f"{name}: {projects_count} layihə")



