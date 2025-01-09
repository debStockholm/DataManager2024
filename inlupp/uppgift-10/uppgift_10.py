# Uppgift 10
# Skapa en funktion celsius_to_fahrenheit(celsius) som konverterar en temperatur från Celsius till Fahrenheit.
 

def celsius_to_fahrenheit(tempC:int):
    Temp_F = tempC*1.8 + 32
    return round(Temp_F, 2)

print(celsius_to_fahrenheit(6)) 


def celsius_to_fahrenheit_2(tempC2:list):
    for Temp_F2 in tempC2:
      Temp_F2 = tempC2*1.8 + 32
    return round(Temp_F2, 2)

print(celsius_to_fahrenheit([9, 6, 3, 12, 15])) 