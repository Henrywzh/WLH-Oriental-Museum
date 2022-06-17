import matplotlib.pyplot as plt

font = {'family' : 'DejaVu Sans',
        'weight' : 'bold',
        'size'   : 15,
        'color'  : 'white'} # Custom font

year = [2020,2019,2018,2017,2016,2015,2014,2013]
mainlandT = [4366099609,3783436398,4239298459,5110756999,4835455861,4489418231,5597169221,6174556188]
overseaT = [1350535948,1961494640,2175094350,2080928385,1910478516,2648383659,2312552292,2339518329]
mainlandAvg = [18409,15253,16769,21214,18967,17697,17068,17135]
overseaAvg = [44566,42782,46821,58397,41910,54265,49855,50449]

fig, ax = plt.subplots(2,1, figsize=(15,8), facecolor='black')
ax[0].bar(year, mainlandT, label='Mainland')
ax[0].bar(year, overseaT, bottom=mainlandT, label='Oversea')
ax[0].legend()
ax[0].set_ylabel('Total Price/USD', **font)
ax[0].set_title('Chinese Artifacts Industry', **font)

ax[1].plot(year, mainlandAvg, label='Mainland')
ax[1].plot(year, overseaAvg, label='Oversea')
ax[1].set_ylabel('Average Price/USD', **font)
ax[1].set_xlabel('Year', **font)
ax[1].legend()

for i in range(0,2):
        ax[i].spines['bottom'].set_color('white')
        ax[i].spines['top'].set_color('white')
        ax[i].spines['right'].set_color('white')
        ax[i].spines['left'].set_color('white')
        ax[i].tick_params(axis='both', colors='white')
        ax[i].set_facecolor("black")

plt.show()
