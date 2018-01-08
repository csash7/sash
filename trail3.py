import speech_recognition as sr
import pyttsx
import webbrowser
#from youtubeex import *
from gpiozero import LED
from gpiozero.pins.pigpiod import PiGPIOPin
from time import sleep
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

VADon=True
enginer = sr.Recognizer()
enginer.energy_threshold=2000
engines = pyttsx.init()

pin_a = PiGPIOPin(21, host='192.168.0.103')
pin_b = PiGPIOPin(7,host='192.168.0.103')
hall = LED(pin_a)
bed = LED(pin_b)

action=['OPEN','CLOSE','SWITCH','STOP','QUIT','PLAY','TURN']
question=['WHO','WHAT','WHERE']

def speak(text):
    engines.say(text)
    engines.runAndWait()

def switch(switchl):
    if ('light' in switchl or 'lights' in switchl):
        if 'on' in switchl:
          if ('hall' in switchl or 'hallroom' in switchl):
            speak('Switching on hall room lights.')
            hall.on()
          elif ('bed' in switchl or 'bedroom' in switchl):
            speak('Switching on bed room lights.')
            bed.on()
          else:
            speak('Switching on lights.')
            hall.on()
            bed.on()
        elif 'off' in switchl:
            if ('hallroom' in switchl or 'hall' in switchl):
                speak('Switching off hall room lights.')
                hall.off()
            elif ('bed' in switchl or 'bedroom' in switchl):
                speak('Switching off bed room lights.')
                bed.off()
            else:
                speak('Switching off lights.')
                hall.off()
                bed.off()
    elif ('camera' in switchl):
        if 'on' in switchl:
            speak('Switching on surveillance camera')
            sur()
        elif 'off' in switchl:
            speak('Switching on surveillance camera')
            cap.release()
    else:
        speak("Sorry I can't operate them yet.")

def perform_action(actionl):
    if actionl[0].upper()=='SWITCH' or actionl[0].upper()=='TURN':
            switch(actionl)

def ask():
    with sr.Microphone(device_index=1) as source:
        enginer.adjust_for_ambient_noise(source)
        while True:
            try:
                audio=enginer.listen(source)
                recognisedtext=enginer.recognize_google(audio)
                print (recognisedtext)
                if 'YES' in recognisedtext.upper():
                    return True
                    break
                elif 'NO' in recognisedtext.upper():
                    return False
                    break
                else:
                     speak("Sorry I dont understand, please repeat.")
            except:
                continue

def recognise():
    with sr.Microphone(device_index=1) as source:
         enginer.adjust_for_ambient_noise(source)
     #print("Say something!")
         while True:
             try:
                found=list()
                audio = enginer.listen(source)
                recognisedtext=enginer.recognize_google(audio)
                print (recognisedtext) #or use sphinx instead of google
                found=recognisedtext.split(' ')
                found[0]=found[0].upper()
                if found[0] in action:
                    perform_action(found)
                    break
                elif found[0] in question:
                    solve_question(found)
                    break
                else:
                    speak("Sorry I don't understand. please repeat")

             except:
          #speak("Sorry I don't understand. Please repeat.")
                continue


def VAD():
    global VADon
    with sr.Microphone(device_index=1) as source:
      enginer.adjust_for_ambient_noise(source,duration=1)
     #print("Say something!")
      while True:
        try:
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

def sur():
  while True:
   ret,frame = cap.read()
   img=frame
   gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
   faces = face_cascade.detectMultiScale(gray,minSize=(200,200))
   for (x, y, w, h) in faces:
       speak("Do you want me to switch on lights?")
       if ask():
           speak("switching on the lights.")
           hall.on()
           bed.on()
           break
       else:
           speak("As you wish.")
           break
       break


while True:
   if VADon:
       VAD()
   else:
       break
