'''
######################################
#####一个基于PyQt5的舞台音效播放器#######
######################################
'''
from PyQt5 import QtMultimedia
from PyQt5.QtCore import QUrl
import time
###创建音频内容和播放器
Vol=100 #音量
page=0
Step=0
beforeTime=0#上次播放时间
continuePlay = True#是否继续播放？如果否，则关闭控制台
command = ""#str类型，用于获得输入的命令
'''
#######################
####在此处预加载文件#####
#######################
'''
file=QUrl.fromLocalFile("枪声.mp3")
gun=QtMultimedia.QMediaContent(file)#枪声

file=QUrl.fromLocalFile("打雷声.mp3")
thunder=QtMultimedia.QMediaContent(file)#雷声

file=QUrl.fromLocalFile("Kyrie Eleison-[Slowed down].mp3")
kyrieEleison=QtMultimedia.QMediaContent(file)#KyrieEleison,结幕音乐

file=QUrl.fromLocalFile("雨声.mp3")
rain=QtMultimedia.QMediaContent(file)#雨声

file=QUrl.fromLocalFile("蝉鸣声.mp3")
zhiliao=QtMultimedia.QMediaContent(file)


'''
###############################
####### 以上为加载文件部分########
###############################
'''
player = QtMultimedia.QMediaPlayer()
#创建一个播放器
'''
#####################
#####播放函数#########
#####################
'''

def play(soundName,Vol=100):#参数：音频名
        print("[play]")
        player.stop()
        player.setMedia(soundName)#给播放器设定内容
        player.setVolume(Vol)#设置音量
        player.play()
def play_withPosition(soundName,Vol=100,position=0):#用来快进
        print("[play] With a exact position")
        player.setMedia(soundName)#给播放器设定内容
        player.setVolume(Vol)#设置音量
        player.play()
        player.setPosition(position)
def _wait(s):#等待
    before = 1.01
    before = float(before)
    s=float(s)
    before = time.time()
    if int(time.time()-before) >= s:
        return 0
    else:
        pass
def Credits(link,Time):#读取txt,播放制作名单
    with open(link,'r',encoding='UTF-8') as staff:#如果报错，把"encoding='UTF-8'"删掉
        data = staff.readlines()
        for k in data:
                time.sleep(Time)
                print(k)
with open("雷雨第四幕.txt",'r',encoding="ANSI") as text:
        Text=text.readlines()
        for k in Text:
                page = page + 1
print(page)
                
            
'''
###################
#####控制台部分######
####################
'''       
def main():
    Step = 0
    while  continuePlay == True:
        command = str(input(""))
        if command == '':
            if Step <= page:
                    Step=Step+1
                    print(Text[Step])
                    
        if command == "22":
            play(gun)
        if command == "21":
            beforeTime=player.position()
            play(thunder)
            time.sleep(1.5)
            play_withPosition(rain,position=beforeTime)
        if command == "23":
            play(kyrieEleison)
        if command == "12":
           play(rain)
        if command == "11":
           play(zhiliao)
        if command =="33":
                Credits('Credits.txt',1)
if __name__ == '__main__':
    main()
    
        
    
















