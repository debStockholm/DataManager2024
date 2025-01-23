import matplotlib.pyplot as plt
import numpy as np

'''x = [0 , 3 , 5, 6, 9, 10, 12, 15]
y = [2 , 3 , 4 , 5 , 6 , 7, 8, 9]

plt.stem(x, y)   #plot, scatter, bar, stairs, stem, fill_between (x, y1, y2), stem  PAIRWISE DATA

plt.title("Exempel på scatterplot")
plt.xlabel("X-axel")
plt.ylabel("Y-axel")
plt.show()

break'''

x = [ 'sapphire', 'diamond', 'topaz', 'rubin']
y = [34, 130, 18, 47]


plt.pie(y)                                         #COME FACCIO UN PIE CHART?
colors = 'blues'   #cosa scrivo qua
fig, ax = plt.subplots()
ax.pie(y, colors= colors, radius= 5, center = (2.5,2.5), frame = True)

plt.show()