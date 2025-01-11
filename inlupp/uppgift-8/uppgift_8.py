#uppgift 8
# Skapa en dict som innehaller samtliga bokstaver av en text med bokstav som nyckel och antal som varde.


def count_letters(x:str):                      #dictionary: {'A':'8', 'B': '6',}
    dictionary_upp = {}                        #1 step: skapa en variabel som innehaller den nya dict {dictionary_upp} 
    for bokstav in x:                          #tillaga varde i en: {} dict['bokstav']= 'x'
        if bokstav not in dictionary_upp:        #2 step: kora il else satsen: 
         dictionary_upp[bokstav] = 1           #om en bokstav ej fanns i dict: tillags
        else: 
         dictionary_upp[bokstav] += 1                   #om en boksav finns i dict: count + 1
    return dictionary_upp

      

    