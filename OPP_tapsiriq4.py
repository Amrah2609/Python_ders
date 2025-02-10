# Bir e-ticarət platforması üçün sadə sifariş idarəetmə sistemi qurmalısan. Aşağıdakı klassları yaz:

 
# Tapşırıq: Sifariş İdarəetmə Sistemi
# Bir e-ticarət platforması üçün sadə sifariş idarəetmə sistemi qurmalısan. Aşağıdakı klassları yaz:

# 1. Product (Məhsul)
# Xüsusiyyətlər:
# name (str) → məhsulun adı
# price (float) → məhsulun qiyməti
# Metodlar:
# __str__() → "Məhsul: Laptop - 999.99 AZN" kimi formatlanmış məlumat qaytarmalıdır
# 2. OrderItem (Sifariş elementi)
# Xüsusiyyətlər:
# product (Product obyekti) → sifariş edilən məhsul
# quantity (int) → məhsulun sayı
# Metodlar:
# get_total_price() → ümumi məbləği qaytarır (price * quantity)
# __str__() → "2x Laptop - 1999.98 AZN" şəklində məlumat qaytarmalıdır.
# Order (Sifariş)
# Xüsusiyyətlər:

# items (OrderItem siyahısı) → sifariş olunan məhsullar
# customer_name (str) → müştərinin adı
# Metodlar:

# add_item(product, quantity) → yeni sifariş maddəsi əlavə edir.
# get_total() → sifarişin ümumi məbləğini qaytarır.
# __str__() → sifarişin tam xülasəsini qaytarmalıdır:
# İstifadə nümunəsi

# laptop = Product("Laptop", 999.99)
# mouse = Product("Mouse", 19.99)

# order = Order("John Doe")
# order.add_item(laptop, 2)
# order.add_item(mouse, 1)

# print(order)  # Sifariş detallarını və ümumi məbləği göstərir. aşağıdakı kimi
# Sifariş: John Doe
# 2x Laptop - 1999.98 AZN
# 1x Mouse - 19.99 AZN
# Ümumi: 2019.97 AZN



# Tapsiriq 4:


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Məhsul: {self.name} - {self.price:.2f} AZN."

class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.quantity}* {self.product.name} - {self.get_total_price():.2f} AZN"

class Order:
    def __init__(self, customer_name):
        self.items = []  # Burada boş bir siyahı təyin olunur
        self.customer_name = customer_name

    def add_item(self, product, quantity):
        order_item = OrderItem(product, quantity)
        self.items.append(order_item)

    def get_total(self):
        return sum(item.get_total_price() for item in self.items)

    def __str__(self):
        order_details = [f"Sifariş: {self.customer_name}"]
        for item in self.items:
            order_details.append(str(item))
        order_details.append(f"Ümumi: {self.get_total():.2f} AZN")
        return "\n".join(order_details)
    
laptop = Product("Laptop", 999.99)
mouse = Product("Mouse", 99.99)

order = Order("John Doe")
order.add_item(laptop, 2)
order.add_item(mouse, 1)

print(order)  