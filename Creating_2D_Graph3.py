import pandas as pd
import csv
import matplotlib.pyplot as plt

font1 = {'family': 'DejaVu Sans',
        'weight' : 'bold',
        'size'   : 18,
        'color'  : 'white'}

def data():
    mydata = pd.read_csv('Artifacts.csv')
    df = pd.DataFrame(mydata)
    return df

def plotGraph(df):
    fig, ax = plt.subplots(1,1, figsize=(15, 8), facecolor='black')
    ax.plot(df['Year'], df['World'], label='World', color='#00ff99')
    ax.plot(df['Year'], df['Beijing'], label='Beijing', color='#ffff33')
    ax.plot(df['Year'], df['HK'], label='HK', color='#4d94ff')
    ax.plot(df['Year'], df['Newyork & London'], label='Newyork & London', color='#ff00ff')
    ax.set_ylabel('Price Index', **font1)
    ax.set_xlabel('Year', **font1)
    ax.set_title('The Change In Price Index Of Chinese Artifacts From 2001 To 2017', **font1)
    ax.tick_params(colors='white')
    ax.set_xticks(df['Year'])
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.legend(loc='lower right')
    ax.set_facecolor("black")

if __name__ == '__main__':
    dataframe = data()
    plotGraph(dataframe)
    plt.show()
