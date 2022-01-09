import urllib.request
import urllib.parse
import re

class Main:
    def __init__(self, url):
        self.url = url

    def getData(self,url):
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

    def saveData(self,data):
        return re.findall('成交价：.+元', data)

    def changeData(self,dataList):
        for i in range(len(dataList)):
            dataList[i] = dataList[i][4:-1]
            dataList[i] = dataList[i].replace(',','')
        print(dataList)

if __name__ == '__main__':
    url = 'http://m.sohu.com/n/456961060/'
    myData = Main(url)
    html = myData.getData(url)
    myData.changeData(myData.saveData(html))
