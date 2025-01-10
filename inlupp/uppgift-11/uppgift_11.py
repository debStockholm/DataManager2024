# Uppgift 11
# Skapa en funktion word_count(text) som returnerar antalet ord i en given text.

def word_count(text_ex:str):
   split_line = text_ex.split("o w")   #altri metodi?    #1 step: dividere string in parole con split
   return len(split_line)
   
print(word_count('hello worlll fdde'))  #funkar

'''def word_count2(ex2:str):
   string_divided = ex2.split()
   print(len(string_divided))

print(word_count2('provar detta om det fungerar')) #perché risulta anche 'none'?'''