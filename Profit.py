import pandas as pd
import matplotlib.pyplot as plt

# Getting files
df = pd.read_csv('/Users/henry/Desktop/Sheet1.csv')
print(df)

# Finding correlation
print(df.corr().to_string())

# Plotting graph
font = {'family' : 'DejaVu Sans',
        'weight' : 'bold',
        'size'   : 15,
        'color'  : 'white'} # Custom font

fig, ax = plt.subplots(1,1, figsize=(15,8) ,facecolor='black') # Line graph
ax.plot(df['Year'],df['Global/%'],label='Global')
ax.plot(df['Year'],df['Beijing/%'],label='Beijing')
ax.plot(df['Year'],df['HongKong/%'],label='HongKong')
ax.plot(df['Year'],df['Newyork & London/%'],label='Newyork & London')

ax.spines['bottom'].set_color('white') # Customising spine colour
ax.spines['top'].set_color('white')
ax.spines['right'].set_color('white')
ax.spines['left'].set_color('white')

ax.tick_params(axis='x', colors='white') # Painting x,y axis to white
ax.tick_params(axis='y', colors='white')
ax.set_facecolor("black")
ax.legend(loc='upper right') # Showing information of different lines

ax.set_ylabel('Change in Profit/%', **font) # Titles
ax.set_xlabel('Year', **font)
ax.set_title('Recent Chinese Artifacts Profits', **font)

plt.show()
