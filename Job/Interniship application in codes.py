print('Hej, let us talk about work/internship possibilities!')

print('...company team scanning available roles)...')

work_position = 'available'
deb = 'this candidate'

if work_position == 'available':
    print(f"{deb} is an amazing opportunity, let's reach her out!")
elif work_position == 'not available':
    other_relevant_openings = False
    if other_relevant_openings:
        print(f"let's see what else can suit {deb} best!")
    else: 
        print(f"can't miss this outstanding opportunity though, let's look better for {deb}' possibilities!")
else:
    print( 'do we really wanna miss this once in a lifetime opportunity? :-( ')


print('Thank you for your time' + ' and')
Weekend_approach = False     

for greeting in range(3):
    if Weekend_approach:
        print('wish you a great weekend!')
    else:
        print('wish you a proficuous week!')

#OBS
print(f'{deb} has some humor')



import pandas as pd

Best_candidate = {
    'Skills': ['Python coding', 'SQL', 'Humor', 'ChatGPT', 'Rail infrastructure designing', 'Brings sweets to office', 'Mind her own business' ],
    'On a scale from 1 (lower) to 10': [3, 6, 10, 8, 7, 20, 9]
}

best_cand=pd.DataFrame(Best_candidate)
best_cand.to_csv('best candidate application.csv', index = False)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Best_best= pd.read_csv('best candidate application.csv')
Best_of_the_best = Best_best.sort_values(by= 'On a scale from 1 (lower) to 10', ascending =True)
print(Best_of_the_best)

sns.barplot(data= Best_of_the_best, x='Skills', y = 'On a scale from 1 (lower) to 10')
plt.title('Debora the best candidate:')
plt.show()   

print('Do you think my code is terrible? Reach me out and show me how to do best!')