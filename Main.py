import speech_recognition as sr
from gtts import gTTS
import os
import time
import warnings
import wikipedia
import calendar
import random
import playsound
import webbrowser

r = sr.Recognizer()


def recognised(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        data= ''
        try:
            data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Sorry Couldn\'t get that :(')
        except sr.RequestError:
            speak('Sorry , I m Down a little :)')

        return data


def speak(audio_string):
    tts = gTTS(text=audio_string,lang='en')
    rand = random.randint(1,1000000)
    audio_file = 'audio-' + str(rand) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)



def response(voice_data):
    if 'what is your name' in voice_data:
        speak('My name as boom')
    if 'what is the time' in voice_data:
        speak(time.ctime())
    if 'search' in voice_data:
        search = recognised('What you wanna Search')
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        speak('Here\'s the Stuff i got for :'+ search)
    if 'find location' in voice_data:
        search = recognised('What location u wanna find?')
        url = 'https://google.in/maps/place/' + search
        webbrowser.get().open(url)
        speak('Here\'s the location u are looking for :' + search)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
speak('May I help U ?')
while 1:
    voice_data = recognised()
    response(voice_data)