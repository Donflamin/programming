# Kelvin till celsius
def kelvin_till_celsius(K):
    C = K - 273.15
    return C

# Celsius till fahrenheit
def celsius_till_fahrenheit(C):
    F = C * 9/5 + 32
    return F

# Fahrenheit till celsius
def fahrenheit_till_celsius(F):
    C = (F - 32) * 5/9
    return C

# Kelvin till fahrenheit
def kelvin_to_fahrenheit(K):
    F = (K - 273.15) * 9/5 + 32
    return F 

print(kelvin_till_celsius(20))
print(celsius_till_fahrenheit(20))
print(fahrenheit_till_celsius(20))
print(kelvin_till_farenheit(20))
