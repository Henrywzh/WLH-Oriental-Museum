import matplotlib.pyplot as plt

def main():
    font1 = {'family': 'DejaVu Sans',
        'weight' : 'bold',
        'size'   : 15,
        'color'  : 'white'}

    content = ['Oil paints','Jade/Porcealin','Books','Ink Paint','Others','Total']
    totalPrice1 = [386.428620, 887.505886, 2.035198, 796.181486, 8.777195, 2080.928385]
    totalPrice2 = [254.894637, 1044.256216, 95.048393, 3395.927895, 320.629858, 5110.756999]
    avprice2 = [46.968,18.732,4.393,32.855,5.858,21.214]
    avprice1 = [207.423,36.321,7.401,88.171,283.135,58.397]
    quantity2 = [5427,55747,21638,103361,54736,240909]
    quantity1 = [1863,24435,275,9030,31,35634]

    plot(font1,content,totalPrice1,totalPrice2,avprice2,avprice1,quantity2,quantity1)


def plot(font1,content,totalPrice1,totalPrice2,avprice2,avprice1,quantity2,quantity1):
    fig, ax = plt.subplots(3,1, figsize=(15,8), facecolor='black')
    ax[0].bar(content, quantity1, label='Oversea')
    ax[0].bar(content, quantity2, bottom=quantity1, label='Mainland')
    ax[0].legend()
    ax[0].set_ylabel('Quantity', **font1)
    ax[1].bar(content, totalPrice1, label='Oversea')
    ax[1].bar(content, totalPrice2, bottom=totalPrice1, label='Mainland')
    ax[1].legend()
    ax[1].set_ylabel('USD/$1,000,000', **font1)
    ax[2].plot(content, avprice1, label='Oversea')
    ax[2].plot(content, avprice2, label='Mainland')
    ax[2].legend(loc='upper left')
    ax[2].set_ylabel('USD/$1000', **font1)

    for i in range(3):
        ax[i].spines['bottom'].set_color('white')
        ax[i].spines['top'].set_color('white')
        ax[i].spines['right'].set_color('white')
        ax[i].spines['left'].set_color('white')
        ax[i].tick_params(axis='y', colors='white')
        ax[i].set_facecolor("black")

    ax[2].tick_params(axis='x', colors='white')
    ax[0].set_title('Total Chinese Artifacts Sold', **font1)
    ax[1].set_title('Total Price in USD', **font1)
    ax[2].set_title('Average Price in USD', **font1)

if __name__ == '__main__':
    main()
    plt.show()
