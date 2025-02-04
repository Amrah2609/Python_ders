number1 = float(input("1-ci rəqəmi daxil edin: "))
number2 = float(input("2-ci rəqəmi daxil edin: "))
operation = input("Emeliyyat daxil edin: ")

if operation == "topla":
    netice = number1 + number2
elif operation == "cix":
    netice = number1 - number2
elif operation == "bolme":
    if  number2 != 0:
        netice = number1 / number2
    else:
        netice = "Sifira bolmek mumkun deyil"
elif operation == "vurma":
    netice = number1 * number2
else:
    netice = "sehv emeliyyat."
print(netice)