import matplotlib.pyplot as plt
import pandas as pd

font = {'family' : 'DejaVu Sans',
        'weight' : 'bold',
        'size'   : 15,
        'color'  : 'white'}

color = ['#438ABD','#F39739','#59A84A','#CF4B3E','#9F82C4','#976C60']

df = pd.read_csv('/Users/henry/Desktop/Sheet10.csv')

labels = ['Oil paints & modern', 'Ceramics', 'Ancient books', 'Calligraphy & painting', 'Others']
fig, ax = plt.subplots(1,1, figsize=(15,8), facecolor='black')
ax.stackplot(df['Year'],df['Oil paints & modern'],df['Ceramics'],df['Ancient books'],df['Calligraphy & painting'],df['Others'])

ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['right'].set_color('white')
ax.spines['left'].set_color('white')

ax.tick_params(axis='both', colors='white')
ax.set_facecolor("black")
ax.legend(labels, loc='upper right')

ax.set_ylabel('Number of transactions', **font)
ax.set_xlabel('Year', **font)
ax.set_title('Chinese Artifacts Industry(Mainland)', **font)

plt.show()
