import matplotlib.pyplot as plt

font = {'family' : 'DejaVu Sans',
        'weight' : 'bold',
        'size'   : 12,
        'color'  : 'white'} # Custom font

object = ['Oil paints & modern', 'Ceramics', 'Ancient books', 'Calligraphy & painting', 'Others']
numM = [7769, 72212, 18552, 74474, 64166]
priceM = [430788812, 1042231188, 103017638, 2434237449, 355824522]

numO = [2251, 23360, 297, 4320, 76]
priceO = [548560983, 493168257, 13910607, 289284787, 5611314]

fig, ax = plt.subplots(2,2,facecolor='black')
ax[0,0].pie(numM, labels=object, autopct='%1.1f%%', textprops={'size':10,'color':'w'})
ax[0,0].set_title('2020 Number of transactions(Mainland)',**font)
ax[0,1].pie(priceM, labels=object, autopct='%1.1f%%', textprops={'size':10,'color':'w'})
ax[0,1].set_title('2020 Price comparison(Mainland)',**font)
ax[1,0].pie(numO, labels=object, autopct='%1.1f%%', textprops={'size':10,'color':'w'})
ax[1,0].set_title('(Oversea)',**font)
ax[1,1].pie(priceO, labels=object, autopct='%1.1f%%', textprops={'size':10,'color':'w'})
ax[1,1].set_title('(Oversea)',**font)

plt.show()
