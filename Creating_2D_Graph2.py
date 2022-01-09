import matplotlib.pyplot as plt
import numpy


def main():
    p1 = [2518.7, 664.2, 1135.3, 167.0, 267.1, 173.6, 327.2, 173.6, 535.0, 623.6, 365.3, 360.6, 2510.7, 1602.6, 1427.9, 1148.5, 1073.7, 1005.4, 949.6, 871.4, 717.7, 540.6, 560.9, 435.7, 363.4, 2670.9, 1564.0, 1215.3, 1095.1, 877.0, 670.3, 822.2, 614.4, 614.1, 460.1, 4255.0, 730.0]
    yr1 = [2015,2013,2012,2020,2017,2015,2013,2014,2014,2014,2019,2011,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2017,2017,2017,2017,2017,2017,2017,2017,2017,2017,2016,2016,2016,2016,2016]

    p2 = [36990.0, 28190.0, 24340.0, 27451.85, 24977.86, 24735.1, 20018.82, 20018.82, 14750.0, 13570.0, 10896.0]
    yr2 = [2016,2016,2016,2016,2016,2016,2017,2017,2017,2017,2017]

    mymodel = numpy.poly1d(numpy.polyfit(yr1, p1, 3))
    myline = numpy.linspace(2011, 2020, 100)

    font = {'family' : 'normal',
            'weight' : 'bold',
            'size'   : 15,
            'color'  : 'white'}

    fig, ax = plt.subplots(2,1, figsize=(15,8),facecolor='black')

    plotting(ax,yr1,p1,yr2,p2,mymodel,myline,fig,font)

def plotting(ax,yr1,p1,yr2,p2,mymodel,myline,fig,font):

    ax[0].scatter(yr1,p1,label='Normal Price', color='#4d94ff')
    ax[0].plot(myline, mymodel(myline), color='#4d94ff')
    ax[1].scatter(yr1,p1,label='Normal Price', color='#4d94ff')
    ax[1].scatter(yr2,p2,label='Top price', color='#ffff33')
    ax[1].plot(myline, mymodel(myline), color='#4d94ff')

    for i in range(2):
        ax[i].spines['bottom'].set_color('white')
        ax[i].spines['top'].set_color('white')
        ax[i].spines['right'].set_color('white')
        ax[i].spines['left'].set_color('white')
        ax[i].tick_params(axis='x', colors='white')
        ax[i].tick_params(axis='y', colors='white')
        ax[i].set_facecolor("black")

    fig.text(0.04, 0.5, 'GBP/1000£', va='center', rotation='vertical', **font)
    fig.text(0.5, 0.04, 'Year', ha='center', **font)

    ax[0].set_title('Recent Chinese Bronze Artifacts Prices', **font)
    ax[1].set_title('Recent Chinese Bronze Artifacts Prices(Including the Top prices)', **font)

    plt.show()

if __name__ == '__main__':
    main()
