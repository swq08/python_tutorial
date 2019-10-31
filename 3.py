from bs4 import BeautifulSoup
import requests

fileName='E:\\pycharm\\百度贴吧'+'\\'+'a.txt'
with open(fileName,'r',encoding='utf-8') as f:
    html=f.read()
    print('文件读取成功！')
# print(html)
soup=BeautifulSoup(html,'html.parser')
img=soup.select('img')
# print(img)
i=0
imgUrlList[]
for eachImg in img:
    if eachImg['src'][-3:]!='png':
        print(eachImg['src'])
        imgUrlList.append(eachImg['src'])
        i+=1
    # print(eachImg['src'])
path='E:\\pycharm\\百度贴吧'+'\\'
# 图片存放路径
i=0
for eachImg in imgUrlList:
    print(eachImg.split('/')[-1])
    # 分割，取最后一个/后面的串，输出文件名
    img=requests.get(eachImg).content   #
    i+=1
    with open(path+imgName,'wb') as f:
        f.write(img)
        time.sleep(2)  #停顿2秒
        print('第{}张图片下载完成！'.format(i))