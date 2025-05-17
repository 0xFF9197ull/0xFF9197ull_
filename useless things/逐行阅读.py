line = 0#总页数
page = 0#当前页面
output = ""
TextLink = 'C:\\Users\\Administrator\\Desktop\\新建文件夹\\雷雨第四幕.txt'
'''
#######################
########读取文件########
#######################
'''
with open(TextLink,'r',encoding="ANSI") as file:
    text = file.readlines()
for k in text:
    line = line + 1
print(line,"lines in total")#显示总回车数|页数
#控制台
while page <= (line-2):
    output = "("+str((page+1))+'/'+str((line-1))+')'
    command = str(input(output))
    if command == "":#如果不输入任何东西就下一页
        page = page + 1
        print(text[page])
    if command == "exit":#输入exit退出
        print("[EXIT]")
        break
    if ("goto" in command) == True:#跳转到某一页
        if int(command[5:]) > line:#防止超出范围
            page = line -1
        else:
            page = int(command[5:])
        print(text[page])
    
input("播放完成")  
