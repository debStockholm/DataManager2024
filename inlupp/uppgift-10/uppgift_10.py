# Uppgift 10
# Skapa en funktion celsius_to_fahrenheit(celsius) som konverterar en temperatur från Celsius till Fahrenheit.
 

'''def celsius_to_fahrenheit(tempC:int):
    Temp_F = tempC*1.8 + 32
    return round(Temp_F, 2)

print(celsius_to_fahrenheit(6))   #ok!'''


def celsius_to_fahrenheit_2(tempC2:list):
    ny_list5 =[]
    for temp_F2 in tempC2:    #OBS temp f2 e in tempc2!
      yu = temp_F2*1.8 + 32
      ny_list5.append(yu)
    return ny_list5

print(celsius_to_fahrenheit_2([9, 6, 3, 12, 15]))    #come farla funzionare fcon una lista di temperature?