fileName='E:\\pycharm\\百度贴吧'+'\\'+'a.txt'
with open(fileName,'r',encoding='utf-8') as f:
    html=f.read()
    print('文件读取成功！')
print(html)
