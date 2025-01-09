# Uppgift 11
# Skapa en funktion word_count(text) som returnerar antalet ord i en given text.

def word_count(text_ex:str):
   split_line = text_ex.split()   #altri metodi?    #1 step: dividere string in parole con split
   count = 0                                        #2 step creare variabile conunt per salvare i risultati
   for x in split_line:                             #3 step: for loop che aggiunge 1 per ogni parola contata
     count += 1
   return count
   
print(word_count('hello worlll'))  #funkar

'''def word_count2(ex2:str):
   string_divided = ex2.split()
   print(len(string_divided))

print(word_count2('provar detta om det fungerar')) #perché risulta anche 'none'?'''