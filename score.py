for i in range(5):
    try:
        name=input('输入姓名')
        score=int(input('输入分数'))
    except Exception as e:
        print('输入错误，成绩为整型')
        print(e)
        continue
    if score>=85:
        print('优秀 ')
    elif score>=75:
        print('良好')
    elif score>=60:
        print('合格')
    else:
        print('不合格')
print(f'成绩打印完毕')