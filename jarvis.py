import pyttsx3 as pyttsx # pyttsx3 for python 3
#from youtubeex import *
import speech_recognition as sr
#import pyglet
import os
#from pydub import AudioSegment

# also install pypiwin32 on new system

'''pyglet.lib.load_library('avbin')
pyglet.have_avbin=True'''

doinggood=['fine',"i'm fine",'okay',"i'm okay",'good',"i'm good",'well',"i'm doing fine",'great',"i'm great","i'm doing great"]
doingbad=['bad','not so good','not okay','not good','not fine',"i'm not okay"]
mood=''

enginer = sr.Recognizer()
engines = pyttsx.init()

def speak(text):
    engines.say(text)
    engines.runAndWait()

def recognise():
    with sr.Microphone(device_index=1) as source:
         enginer.adjust_for_ambient_noise(source)
     #print("Say something!")
    while True:
      try:
        audio = enginer.listen(source)
        recognisedtext=enginer.recognize_sphinx(audio)
        print (recognisedtext) #or use sphinx instead of google
        #speak('I think you said, '+recognisedtext)
        break
      except:
        speak("Sorry I don't understand. Please repeat.")
        continue


def VAD():
    global VADon
    with sr.Microphone(device_index=1) as source:
      enginer.adjust_for_ambient_noise(source,duration=1)
     #print("Say something!")
      while True:
        try:
             '''speak('Hey!')
             speak('My name is Jarvis. May I know your name?')'''
          #while True:
             audio = enginer.listen(source)
             recognisedtext=enginer.recognize_google(audio)
             print (recognisedtext) #or use sphinx instead of google
             #speak('I think you said, '+recognisedtext)
             if 'hey Jarvis' in recognisedtext:
                 speak('How can I help you?')
                 recognise()
                 break
          #break
        except sr.UnknownValueError:
                    continue

#paraf = open('values.txt','r+')

while True:
    VAD()




'''name=recognise() #or use sphinx instead of google
speak(name+'!! nice name! how are you doing?')

while mood=='':
    doing=recognise()
    if doing in doinggood:
        speak('Great to hear! So what do you want to do today?')
        mood='great'
    elif doing in doingbad:
        speak("Oh! Sad to hear. Boredom should not stand a chance against us. Let's have fun.")
        mood='dull'
    else:
        speak("I don't understand it. Please repeat")

mood='great'
speak("Who is your favourite artist?")
artist = recognise()
speak('What is your favourite genre?')
genre = recognise()
speak('Now, let me entertain you!')
'''



'''
if mood=='great':
    songtitle=youtubeplay(artist)
else:
    songtitle=youtubeplay(genre+' songs')
print songtitle
wav_audio = AudioSegment.from_file(songtitle+".m4a", format="m4a").export(songtitle+".mp3", format="mp3")
os.system('start C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe '+songtitle+'.mp3')
player=pyglet.media.player()
player.queue(songtitle+'.mp3')
player.play()'''
