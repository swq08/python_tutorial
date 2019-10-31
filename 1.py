import requests
url='https://www.baidu.com/'
header={
    'Host': 'www.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
}
res=requests.get(url,headers=header)
res.encoding='utf-8'
print(res.text)
fileName='E:\\pycharm\\百度贴吧'+'\\'+'a.txt'
with open(fileName,'a',encoding='utf-8') as f:
    f.write(res.text)
    f.close()