import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



# -- Gathering data from csv files that are previously downloaded from the internet
class GatherData:
    def data1(self):
        dfC = pd.read_csv('/Users/henry/Desktop/christie.csv')
        dfS = pd.read_csv('/Users/henry/Desktop/sotheby.csv')

        changeC = [float(i[:-1]) for i in dfC['Change %']]
        stockChangeC = []

        changeS = [float(i[:-1]) for i in dfS['Change %']]
        stockChangeS = []

        pC = [float(i) for i in dfC['Price']]
        priceC = []

        pS = [float(i) for i in dfS['Price']]
        priceS = []

        year = [1990+i for i in range(int(len(changeC)/12))]

        for i in range(int(len(changeC)/12)):
            stockChangeC.append(round(sum([changeC[i*12 + j] for j in range(12)])/12,2))
            priceC.append(round(sum([pC[i*12 + j] for j in range(12)])/12,2))

            stockChangeS.append(round(sum([changeS[i*12 + j] for j in range(12)])/12,2))
            priceS.append(round(sum([pS[i*12 + j] for j in range(12)])/12,2))

        return year, priceC, stockChangeC, priceS, stockChangeS

    def data2(self):
        df2 = pd.read_csv('/Users/henry/Desktop/gdp.csv')
        annualChange = [float(i[:-1]) for i in df2['Annual Change']]
        growth = [float(i[:-1]) for i in df2['GDP Growth (%)']]

        return growth, annualChange

    def data3(self):
        df3 = pd.read_csv('/Users/henry/Desktop/confidence.csv')
        cci = df3['Consumer']
        bci = df3['Business']
        consumer = []
        business = []

        for i in range(int(len(cci)/12)):
            consumer.append(round(sum([cci[i*12 + j] for j in range(12)])/12,2))
            business.append(round(sum([bci[i*12 + j] for j in range(12)])/12,2))

        return consumer, business

    def data4(self):
        heightC = [1.2, 0.1, 1.85, 1.1, 1.08, 1.55, 1.77, 2.6, 2.33, 2.7, 2.9, 2.2, 2.2,
                   2.35, 2.78, 4.45, 7, 9.65, 7.7, 4.15, 6.75, 7.1, 8.1, 9.65, 11.7, 11.5]

        turnoverC = []

        heightS = [2.1, 0.6, 1.15, 1.35, 1.4, 1.85, 1.65, 2.1, 2.35, 3.1, 2.6, 2.15, 2.5,
                   2.4, 4.3, 3.9, 6.1, 9.05, 8.8, 3.6, 6.55, 7.8, 7.25, 8.45, 10.3, 10.6]

        turnoverS = []

        for i in range(len(heightC)):
            turnoverC.append(round(heightC[i] / 2.3  * 1000000000))
            turnoverS.append(round(heightS[i] / 2.3  * 1000000000))

        return turnoverC, turnoverS

    def data5(self):
        df5 = pd.read_csv('/Users/henry/Desktop/gdpGrowthCountry.csv')
        gbr = [float(i[:-1]) for i in df5['GBR']]
        usa = [float(i[:-1]) for i in df5['USA']]
        chn = [float(i[:-1]) for i in df5['CHN']]

        return gbr, usa, chn

    def table(self):
        year, priceC, stockChangeC, priceS, stockChangeS = GatherData.data1(self)
        growth, annualChange = GatherData.data2(self)
        consumer, business = GatherData.data3(self)
        turnoverC, turnoverS = GatherData.data4(self)
        gbr, usa, chn = GatherData.data5(self)

        data = {
            'Year': year,
            'Christie Price': priceC,
            'Christie Stock change': stockChangeC,
            'Sotheby Price': priceS,
            'Sotheby Stock change': stockChangeS,
            'GDP growth': growth,
            'GDP annual change': annualChange,
            'Consumer Confidence': consumer,
            'Business Confidence': business,
            'Christie Turnover': turnoverC,
            'Sotheby Turnover': turnoverS,
            'UK growth': gbr,
            'US growth': usa,
            'China growth': chn
        }

        return data


# -- Creating a table, finding correlation, drawing linear regression graphs
class Graphs:
    def getTable(self):
        myData = GatherData()
        data = myData.table()

        myDf = pd.DataFrame(data)
        print(myDf.to_string())
        print(myDf.corr().to_string())

        return myDf

    # -- Creating a table with variables that are related
    def getNewTable(self):
        myData = GatherData()
        data = myData.table()

        myDf = pd.DataFrame(data)
        newDf = myDf.drop(19)
        newDf = newDf[['Year', 'Christie Price', 'Sotheby Price', 'GDP growth', 'Business Confidence', 'Christie Turnover', 'Sotheby Turnover']]

        print(newDf.to_string())
        print(newDf.corr().to_string())

        return newDf

    # -- Graphs
    # -- All 8 graphs
    def corrGraphs(self, myDf):
        font = {'family' : 'DejaVu Sans',
                'size'   : 15}

        xlabels = ['Business Confidence', 'GDP growth', 'Christie Turnover', 'Sotheby Turnover']
        ylabels = ['Christie Price', 'Sotheby Price']
        x = [myDf['Business Confidence'], myDf['GDP growth'], myDf['Christie Turnover'], myDf['Sotheby Turnover']]
        y = [myDf['Christie Price'], myDf['Sotheby Price']]

        fig, ax = plt.subplots(4,2)

        for i in range(4):
            for j in range(2):
                ax[i,j].scatter(x[i], y[j], label=xlabels[i])
                ax[i,j].set_ylabel(ylabels[j])
                ax[i,j].legend(loc='upper left')

        fig.suptitle('Relations Between Stock Price And Other Variables', **font)

        plt.show()

    def eachGraphs(self, newDf):
        font = {'family' : 'DejaVu Sans',
                'size'   : 15}

        xlabels = ['Business Confidence Index', 'GDP Growth Rate/%', 'Christie Turnover/$', 'Sotheby Turnover/$']
        ylabels = ["Christie's Stock Price", "Sotheby's Stock Price"]
        x_axis = [newDf['Business Confidence'], newDf['GDP growth'], newDf['Christie Turnover'], newDf['Sotheby Turnover']]
        y_axis = [newDf['Christie Price'], newDf['Sotheby Price']]

        for i in range(4):
            fig, ax = plt.subplots(2,1, figsize=(15,8))

            ax[0].set_title(f'Stock price and {xlabels[i]}', **font)
            ax[0].scatter(x_axis[i], newDf['Christie Price'])
            ax[0].set_ylabel("Christie's Price", **font)
            ax[1].scatter(x_axis[i], newDf['Sotheby Price'])
            ax[1].set_ylabel("Sotheby's Price", **font)
            ax[1].set_xlabel(xlabels[i], **font)

            for j in range(2):
                x, y = x_axis[i], y_axis[j]
                m = self.b1(x, y)
                c = self.b0(x, y)
                print(f'The equation for {ylabels[j]} against {xlabels[i]} is: y = {m:.4}x + {c:.4}')
                yList = [self.draw(x, m, c) for x in x_axis[i]]
                ax[j].plot(x_axis[i], yList, label=f'y = {m:.4}x + {c:.4}')
                ax[j].legend(loc='upper left')

            plt.show()

    def mean(self, x, y):
        ex = sum([i for i in x])/len(x)
        ey = sum([j for j in y])/len(y)

        return ex, ey

    def b1(self, x, y):
        ex, ey = self.mean(x, y)
        xi = [i - ex for i in x]
        yj = [j - ey for j in y]
        eqn = (sum(xi[i]*yj[i] for i in range(len(xi))))/(sum([(i - ex)**2 for i in x]))

        return eqn

    def b0(self, x, y):
        ex, ey = self.mean(x, y)
        b = self.b1(x, y)

        return ey - ex * b

    def draw(self, x, m, c):
        return x*m + c

    def multipleRegression(self, newDf):
        l = []
        companies = [newDf['Christie Price'], newDf['Sotheby Price']]
        turnovers = [newDf['Christie Turnover'], newDf['Sotheby Turnover']]
        names = ["Christie's", "Sotheby's"]

        for i in range(2):
            y = np.array(companies[i]).transpose()
            x = np.array([np.array([1 for i in companies[i]]), np.array(newDf['Business Confidence']), np.array(newDf['GDP growth']), np.array(turnovers[i])])
            c = np.linalg.inv(x.dot(x.transpose()))
            b = (c.dot(x)).dot(y)
            l.append(b)

            print(f'{names[i]} Stock Price Equation:')
            print(f'y = {b[0]} + {b[1]}x1 + {b[2]}x2 + {b[3]}x3')
            print(f'x1: Business Confidence Index\nx2: GDP growth rate\nx3: {names[i]} Turnover')

        return l

    def r2(self, l, predY):
        meanY = sum([i for i in l])/len(l)
        actualY = list(l)
        rSquared = 1 - (sum([(actualY[i] - predY[i])**2 for i in range(len(predY))]))/(sum([(actualY[i] - meanY)**2 for i in range(len(predY))]))
        return rSquared

    def regModelTest(self, table):
        a = eqns[0]
        b = eqns[1]

        year = list(table['Year'])
        year.extend([2016, 2017, 2018, 2019])
        christiePrice = list(table['Christie Price'])
        christiePrice.extend([100.29, 100.46, 118.21, 102.71])
        sothebyPrice = list(table['Sotheby Price'])
        sothebyPrice.extend([31.86, 48.87, 48.69, 48.75])
        bci = list(table['Business Confidence'])
        bci.extend([100.085, 101.109, 101.227, 99.87])
        gdp = list(table['GDP growth'])
        gdp.extend([2.61, 3.28, 3.03, 2.33])
        turnC = list(table['Christie Turnover'])
        turnC.extend([3.087*10**9, 4.4348*10**9, 5.0435*10**9, 3.674*10**9])
        turnS = list(table['Sotheby Turnover'])
        turnS.extend([2.913*10**9, 3.3913*10**9, 4*10**9, 3.6087*10**9])

        predC = []
        predS = []

        for i in range(len(christiePrice)):
            predC.append(round(a[0] + a[1]*bci[i] + a[2]*gdp[i] + a[3]*turnC[i], 2))
            predS.append(round(b[0] + b[1]*bci[i] + b[2]*gdp[i] + b[3]*turnS[i], 2))

        print("r2 score for Christie's stock price multiple regresison model: ", self.r2(christiePrice, predC))
        print("r2 score for Sotheby's stock price multiple regresison model: ", self.r2(sothebyPrice, predS))

        font = {'family' : 'DejaVu Sans',
                'size'   : 15}

        fig, ax = plt.subplots(2,1, figsize=(15, 8))
        ax[0].set_title('Stock Price Model', **font)
        ax[0].plot(year, predC, label='Predicted Values')
        ax[0].scatter(year, christiePrice, label='Actual Values')
        ax[0].set_ylabel("Christie's Stock Price", **font)
        ax[0].legend(loc='upper left')
        ax[1].plot(year, predS, label='Predicted Values')
        ax[1].scatter(year, sothebyPrice, label='Actual Values')
        ax[1].set_ylabel("Sotheby's Stock Price", **font)
        ax[1].set_xlabel('Year', **font)
        ax[1].legend(loc='upper left')
        plt.show()

        predC = []
        predS = []

        for x in range(len(turnS)):
            y1 = (1.848*10**-8)*turnC[x] + 41.16
            y2 = (6.824*10**-9)*turnS[x] + 8.587
            predC.append(y1)
            predS.append(y2)

        print("r2 score for Christie's linear model: ", self.r2(christiePrice, predC))
        print("r2 score for Sotheby's linear model: ", self.r2(sothebyPrice, predS))



if __name__ == '__main__':
    myGraphs = Graphs()
    table = myGraphs.getNewTable()
    myGraphs.corrGraphs(myGraphs.getTable())
    myGraphs.eachGraphs(myGraphs.getNewTable())
    eqns = myGraphs.multipleRegression(table)
    myGraphs.regModelTest(table)
