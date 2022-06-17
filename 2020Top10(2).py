import pandas as pd
import matplotlib.pyplot as plt

font = {'family' : 'DejaVu Sans',
        'weight' : 'bold',
        'size'   : 12,
        'color'  : 'white'} # Custom font

df = pd.read_csv('/Users/henry/Desktop/Sheet7.csv')
print(df)

explode=(0.1,0,0,0,0,0,0,0,0,0)
fig, ax = plt.subplots(1,2,facecolor='black',figsize=(15,5))
ax[0].pie(df['Price/USD'], labels=df['Company'], autopct='%1.1f%%', textprops={'size':10,'color':'w'}, explode=explode)
ax[0].set_title('2020 Top 10 Companies (Price)',**font)

color = ['#438ABD','#F39739','#59A84A','#CF4B3E','#9F82C4','#976C60','#DE95CA','#919292','#C8C54D','#58C6D5']
ax[1].bar(df['Company'], df['No. of transactions'], color=color)
ax[1].set_title('2020 Top 10 Companies (No. of transactions)',**font)
ax[1].spines['bottom'].set_color('white')
ax[1].spines['top'].set_color('white')
ax[1].spines['right'].set_color('white')
ax[1].spines['left'].set_color('white')
ax[1].tick_params(axis='y', colors='white')
ax[1].set_facecolor("black")

plt.show()
