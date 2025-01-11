# Uppgift 10
# Skapa en funktion celsius_to_fahrenheit(celsius) som konverterar en temperatur från Celsius till Fahrenheit.
# Enkelt konvertering (vet ej om det finns nagon inbyggd fuktion), jag bara googlade hur man -matematisk-t koverterade 
# C till F. 

def celsius_to_fahrenheit(tempC:int):
    Temp_F = tempC*1.8 + 32
    return round(Temp_F, 2)   #adderade decimaler, men kanske behovdes ej?
   

