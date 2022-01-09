import urllib.request
import urllib.parse
import re

def main():
    url = 'http://www.getit01.com/p201806273385757/'
    data = getData(url)

    realP = re.findall('成交價：[0-9].{9}',data)

    for i in range(len(realP)):
        while realP[i][-1] != '元':
            realP[i] = realP[i][:-1]
        realP[i] = realP[i][4:]

    dataList = []

    for i in range(len(realP)):
        realP[i] = realP[i].replace('萬',' 10000 ')
        realP[i] = realP[i].replace('億',' 100000000 ')
        l = realP[i].split(' ')
        p = round(float(l[0]) * float(l[1]), 2)
        curr = l[2]
        if curr == '美元':
            p *= 0.7379529198
        elif curr == '元':
            p *= 0.116127223
        elif curr == '港元':
            p *= 0.0946741938
        dataList.append(round(p,2))

    print(dataList)


def getData(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
    }

    try:
        req = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        return html

    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)

if __name__ == '__main__':
    main()
