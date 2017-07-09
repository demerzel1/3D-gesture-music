import os
import tkinter
import tkinter.filedialog
import random
import time
import threading
import pygame
'''
import serial
addr = 'COM3'
baudrate = 9600
timeout = 1
dev = serial.Serial()
dev.baudrate = baudrate
dev.port = addr
dev.timeout = timeout
dev.open()
dev.readline()

'''
folder = 'D:\\test'

def play():
    global folder
    musics = [folder+'\\'+music
              for music in os.listdir(folder) \
              if music.endswith(('.mp3', '.wav'))]
    pygame.mixer.init()
    while playing:
        if not pygame.mixer.music.get_busy():
            nextMusic = random.choice(musics)
            pygame.mixer.music.load(nextMusic.encode())
            pygame.mixer.music.play(0)
            musicName.set('playing....'+nextMusic)
        else:
            time.sleep(0.3)
root = tkinter.Tk()
root.title('musicplayer')
root.geometry('280x100')
root.resizable(False, False)
def closeWindow():
    global playing
    playing = False
    time.sleep(0.3)
    try:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    except:
        pass
    root.destroy()
root.protocol('WM_DELETE_WINDOW', closeWindow)
pause_resume = tkinter.StringVar(root, value='NotSet')
playing = False

def buttonPlayClick():
    global folder
    if not folder:
        folder = tkinter.filedialog.askdirectory()
    if not folder:
        return
    global playing
    playing = True
    t = threading.Thread(target=play)
    t.start()
    buttonPlay['state'] = 'disabled'
    buttonStop['state'] = 'normal'
    buttonPause['state'] = 'normal'
    buttonNext['state'] = 'normal'
    pause_resume.set('Pause')

buttonPlay = tkinter.Button(root,
                            text='Play',
                            command=buttonPlayClick)
buttonPlay.place(x=20, y=10, width=50, height=20)
def buttonStopClick():
    global playing
    playing = False
    pygame.mixer.music.stop()
    musicName.set('没有播放音乐')
    buttonPlay['state'] = 'normal'
    buttonStop['state'] = 'disabled'
    buttonPause['state'] = 'disabled'
    buttonNext['state'] = 'disabled'
    global folder
    folder = 'D:\\test'

buttonStop = tkinter.Button(root,
                            text='Stop',
                            command=buttonStopClick)
buttonStop.place(x=80, y=10, width=50, height=20)
buttonStop['state'] = 'disabled'


def buttonPauseClick():
    if pause_resume.get() == 'Pause':
        pygame.mixer.music.pause()
        pause_resume.set('Resume')
    elif pause_resume.get() == 'Resume':
        pygame.mixer.music.unpause()
        pause_resume.set('Pause')
buttonPause = tkinter.Button(root,
                             textvariable=pause_resume,
                             command=buttonPauseClick)
buttonPause.place(x=140, y=10, width=50, height=20)
buttonPause['state'] = 'disabled'

def buttonNextClick():
    global playing
    playing = False
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    buttonPlayClick()
buttonNext = tkinter.Button(root,
                            text='Next',
                            command=buttonNextClick)
buttonNext.place(x=200, y=10, width=50, height=20)
buttonNext['state'] = 'disabled'
musicName = tkinter.StringVar(root,value='没有播放音乐')
labelName = tkinter.Label(root,textvariable=musicName)
labelName.place(x=0, y=40, width=270, height=20)
motionName = tkinter.StringVar(root,value='您没有动作')
labelName2 = tkinter.Label(root,textvariable=motionName)
labelName2.place(x=0, y=60, width=270, height=20)
def oymotion():
    while 1:
        '''
       s=bytes(dev.readline()).decode('ascii')
       '''
        s=input()
        if not s=='':
            a=int(s)
            print(a)
            if a==2:
                if buttonPlay['state']=='normal':
                    motionName.set("握拳:控制播放")
                    buttonPlayClick()
            if a==4:
                if buttonStop['state']=='normal':
                    motionName.set("射击:控制停止")
                    buttonStopClick()
            if a==6:
                if buttonPause['state'] == 'normal':
                    motionName.set("捻:控制暂停/恢复")
                    buttonPauseClick()
            if a==5:
                if buttonNext['state']=='normal':
                    motionName.set("手外摆:控制下一首")
                    buttonNextClick()

tt = threading.Thread(target=oymotion)
tt.start()

root.mainloop()
