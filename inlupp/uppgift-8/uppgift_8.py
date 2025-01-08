# Uppgift 8
# Skapa en funktion count_letters(string) som returnerar en dictionary med varje bokstav som nyckel och antalet förekomster som värde.

def count_letters(x:str):                      #dictionary: {'A':'8', 'B': '6'}
    dictionary_upp = {}                        #1 step: apro funzione dictionary da completare - come fare?
    bokstav_count = 0                                #x['bokstav']= '5', per aggiungere temrini in dict
    for bokstav in x:
       if bokstav in dictionary_upp == 0:      #2 step: aggiungere i valori di x:str al dizionario (for loop?)
          return dictionary_upp['bokstav'] = ''
       while bokstav in dictionary_upp:        #3 step: quando una letters e presente nel dict, aggiornare il count
        return bokstav_count =+ 1                #help!

print(count_letters('exit'))