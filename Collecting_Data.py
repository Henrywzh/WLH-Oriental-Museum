import re
import urllib.request, urllib.error

def main(): #Main function
    data = askURL('http://www.sohu.com/a/471131994_120500588') #A chinese website
    save = saveData(data)
    getData(save)

def getData(x): #Clean and change data, eg removing blank space and changing currency
    price = []
    for i in range(len(x)):
        x[i] = x[i][4:]
    for j in x:
        new = j.split(' ')
        for k in new:
            if k == '':
                new.remove(k)
        new[0] = new[0].replace(',', '')
        if new[1] == 'HKD':
            new[0] = round(float(new[0]) * 0.0950722446, 3)
        elif new[1] == 'RMB':
            new[0] = round(float(new[0]) * 0.116639607, 3)
        elif new[1] == 'USD':
            new[0] = round(float(new[0]) * 0.741350295, 3)
        else:
            new[0] = float(new[0])
        new[1] = 'GBP'
        price.append(new[0])
    print(price)

def saveData(savepath):
    return re.findall('成交价.+HKD|成交价.+USD|成交价.+GBP|成交价.+[^HKDUGBP]RMB',savepath) #Searching the price, 成交价 means the released price in chinese

def askURL(url): #Getting data online
    head = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
    request = urllib.request.Request(url=url, headers=head)
    html = ''
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        return html

    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)

if __name__ == '__main__': #Run the function
    main()
