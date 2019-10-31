score_all=[]
mark=True
while mark:
    name=input('输入姓名')
    english=int(input('输入分数'))
    chinese=int(input('输入分数'))
    math=int(input('输入分数'))
    python=int(input('输入分数'))
    score_dict={'english':english,'chinese':chinese,'math':math,'python':python}
    score_list={name:score_dict}
    score_all.append(score_list)
    print(score_all)
    score=score_dict['english']+score_dict['chinese']+score_dict['math']+score_dict['python']
    max_s=max(score_dict['english'],score_dict['chinese'],score_dict['math'],score_dict['python'])
    if score>=85:
        print('优秀 ')
    elif score>=75:
        print('良好')
    elif score>=60:
        print('合格')
    else:
        print('不合格')
    mark=input('是否继续输入n/y？')
    if mark=='n':
        mark=False
print(f'最高分{max_s}')
print(f'成绩打印完毕')