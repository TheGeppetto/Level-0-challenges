def celsius_to_fahrenheit(celsius_temp):
    fahrenheit_temp = (celsius_temp * 9/5) + 32
    return fahrenheit_temp

def fahrenheit_to_celsius(fahrenheit_temp):
    celsius_temp = (fahrenheit_temp - 32) * 5/9
    return celsius_temp

print(celsius_to_fahrenheit(32))
print(fahrenheit_to_celsius(32))
