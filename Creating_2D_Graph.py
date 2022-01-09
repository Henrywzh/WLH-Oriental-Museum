import matplotlib.pyplot as plt
import numpy

yr1 = [2006,2008,2010,2013,2015,2019,2014,2020,2014,2015,2018,2015,2017,2015,2014,2018,2018,2017,2019,2020,2017,2018,2017]
p1 = [66400,101790,119590,131500,89130.229, 80481.329, 71304.183, 56336.93, 41365.934, 33655.575, 27800.636, 29168.165, 27500.0, 28046.312, 28046.312, 25947.26, 22579.658, 16250.0, 16096.266, 12742.877, 7986.069, 6438.506, 4024.066]

yr2 = [2006,2008,2010,2013,2013,2014,2014,2015,2016,2016,2017,2018,2019,2019,2020]
p2 = [66400,101790,119590,131500,128347.53,135002.587,201300,147700,211060.383,225000,227600,225796.58,237000,174500,221710]

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 20,
        'color'  : 'white'}

mymodel1 = numpy.poly1d(numpy.polyfit(yr2, p2, 4))
myline = numpy.linspace(2006, 2020, 100)
mymodel2 = numpy.poly1d(numpy.polyfit(yr1, p1, 4))

class CreateGraph:
    def __init__(self, year1, year2, price1, price2, model1, model2, line, font):
        self.year1 = year1
        self.year2 = year2
        self.price1 = price1
        self.price2 = price2
        self.model1 = model1
        self.model2 = model2
        self.line = line
        self.font = font

    def plotting(self):
        plt.figure(facecolor='black')
        ax = plt.axes()
        ax.set_facecolor("black")
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.spines['left'].set_color('white')
        plt.scatter(self.year2, self.price2, label='Good quality', color='#00ff99')
        plt.scatter(self.year1, self.price1, label='Low quality', color='#ff00ff')
        plt.plot(self.line, self.model1(self.line), color='#00ff99')
        plt.plot(self.line, self.model2(self.line), color='#ff00ff')
        ax.tick_params(axis='x', colors='white')    #setting up X-axis tick color to red
        ax.tick_params(axis='y', colors='white')
        plt.xlabel('Year', **self.font)
        plt.ylabel('GBP/£', **self.font)
        plt.title("The Price Comparison Of Different Muye Cup's Quality", **self.font)
        plt.legend(loc="upper left")
        plt.show()

if __name__ == '__main__':
    mygraph = CreateGraph(yr1, yr2, p1, p2, mymodel1, mymodel2, myline, font)
    mygraph.plotting()
