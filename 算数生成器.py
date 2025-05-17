import random
length=(int(input("数字长度:")))
step=int(input("题数（37题一页）"))
maximum=10**(length+1)-1
minimum=10**length
question=[]
answer=[]
#print(minimum,maximum)
def calc(minimum,maximum,answer):
    a=str(random.randint(minimum,maximum))
    b=str(random.randint(minimum,maximum))
    output = a+'×'+b+'='
    answer.append(str(int(a)*int(b)))
    return output
for k in range(0,step):
    ques=calc(minimum,maximum,answer)
    question.append(ques)
#print(question,answer)
with open ('C:\\Users\\Administrator\\Desktop\\算数.txt','w+',encoding='UTF-8') as file:#注意替换为自己想要的路径
    file.write("[Question]"+'\t\t\t\t'+'[Answer]'+'\n')
    for k in range(0,len(question)):
        writeContain=question[k]+"\t\t"+answer[k]+"\n"
        file.write(writeContain)
    file.close()
