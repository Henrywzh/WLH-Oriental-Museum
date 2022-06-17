import pandas as pd
import matplotlib.pyplot as plt

font = {'family' : 'DejaVu Sans',
        'weight' : 'bold',
        'size'   : 15,
        'color'  : 'white'} # Custom font

df = pd.read_csv('/Users/henry/Desktop/Sheet7.csv')

color = ['#438ABD','#F39739','#59A84A','#CF4B3E','#9F82C4','#976C60','#DE95CA','#919292','#C8C54D','#58C6D5']
fig, ax = plt.subplots(1,1, figsize=(15,8), facecolor='black')
ax.barh(df['Company'], df['Transaction rate'], color=color)

ax.set_title('2020 Top 10 Companies (Transaction rate)',**font)
ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['right'].set_color('white')
ax.spines['left'].set_color('white')
ax.tick_params(axis='both', colors='white')
ax.set_xlabel('Percentage/%', **font)
ax.set_facecolor("black")

plt.show()
