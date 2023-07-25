# Truzz Blogg - Youtube link: https://youtu.be/q-N6IcgCqCE
# Speech recognition in Python ::: How to convert an Audio File to Text

import speech_recognition as sr
import re
import os
from gtts import gTTS


def write_f(name,content):
    with open(name,"w") as file:
        file.write(content)


def read_audio(filename,filetxt):

    r = sr.Recognizer()

    #filename = "IA.wav"

    # open the file
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data, language='es-ES')
        #print(text)
        write_f(filetxt,text)
        

def read_f(name):
    with  open(name,'r', encoding='utf-8') as file:
        return file.read()


def removeAccents(word):
    repl = {'à': 'a', 'á': 'a', 'â': 'a', 'ã': 'a',
            'é': 'e', 'ê': 'e',
            'í': 'i',
            'ó': 'o', 'ô': 'o', 'õ': 'o',
            'ú': 'u', 'ü': 'u'}

    new_word = ''.join([repl[c] if c in repl else c for c in word])
    return new_word


if __name__ == "__main__":
    filewav = "IA.wav"
    filetxt = "prueba.txt"
    read_audio(filewav,filetxt)
    readtxt = read_f(filetxt)
    #tokenised = removeAccents(filetxt)
    tts = gTTS(text=readtxt, lang='es')
    filemp3 = "hello.mp3"
    tts.save(filemp3)
    os.system(f"start {filemp3}")
  