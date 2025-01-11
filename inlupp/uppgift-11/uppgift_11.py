# Uppgift 11
# Skapa en funktion word_count(text) som returnerar antalet ord i en given text.

def word_count(text_ex:str):
   split_line = text_ex.split()   #man delar den angivne string i ord genom split(). default: str delas mellan whitespaces
   return len(split_line)         #returnerar antalet ord da len raknar ord texten blev uppdelat i
   

