# Uppgift 10
# Skapa en funktion celsius_to_fahrenheit(celsius) som konverterar en temperatur från Celsius till Fahrenheit.
# Enkelt konvertering (vet ej om det finns nagon inbyggd funktion), jag bara googlade hur man -matematiskt- koverterade 
# C till F. 

def celsius_to_fahrenheit(tempC:int):
    Temp_F = tempC*1.8 + 32
    return round(Temp_F, 2)   #adderade decimaler, men kanske behovdes ej?
   

