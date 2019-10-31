def score_input(name,english,chinese,math,python):
    score_all=[]
    score_list=[name,english+chinese+math+python]
    score_all.append(score_list)
    print(score_all)
    return score_list
def stu_grade(s_list):
    if s_list[1]>= 85:
        print('优秀 ')
    elif s_list[1]>= 75:
        print('良好')
    elif s_list>[1]>= 60:
        print('合格')
    else:
        print('不合格')

stu_score=score_input('li',22,21,23,24)
stu_grade(stu_score)
print(f'{stu_score[0]}的成绩是{stu_score[1]}')
stu_s=open('student.txt','a')
stu_s.write(str(stu_score))
stu_s.close()