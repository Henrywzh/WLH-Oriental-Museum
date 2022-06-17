import matplotlib.pyplot as plt
import pandas as pd

font = {'family' : 'DejaVu Sans',
        'weight' : 'bold',
        'size'   : 15,
        'color'  : 'white'} # Custom font

color = ['#438ABD','#F39739','#59A84A','#CF4B3E','#9F82C4','#976C60']

df = pd.read_csv('/Users/henry/Desktop/Sheet9.csv')

fig, ax = plt.subplots(1,1, figsize=(15,8), facecolor='black') # Line graph
ax.plot(df['Year'],df['Oil paints & modern'],label='Oil paints & modern')
ax.plot(df['Year'],df['Ceramics'],label='Ceramics')
ax.plot(df['Year'],df['Ancient books'],label='Ancient books')
ax.plot(df['Year'],df['Calligraphy & painting'],label='Calligraphy & painting')
ax.plot(df['Year'],df['Others'],label='Others')
ax.plot(df['Year'],df['Total'],label='Total')

ax.spines['bottom'].set_color('white') # Customising spine colour
ax.spines['top'].set_color('white')
ax.spines['right'].set_color('white')
ax.spines['left'].set_color('white')

ax.tick_params(axis='both', colors='white') # Painting x,y axis to white
ax.set_facecolor("black")
ax.legend(loc='upper left') # Showing information of different lines

ax.set_ylabel('Average Price/USD', **font) # Titles
ax.set_xlabel('Year', **font)
ax.set_title('Chinese Artifacts Industry(Oversea)', **font)

plt.show()
