def convert_int(k):
    return int(k.replace(",",""))

print(convert_int("1,234,567"),type(convert_int("1,234,567")))