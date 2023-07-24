# Truzz Blogg - Youtube link: https://youtu.be/q-N6IcgCqCE
# Speech recognition in Python ::: How to convert an Audio File to Text

import speech_recognition as sr
import pyttsx3



def write_f(name,content):
    with open(name,"w") as file:
        file.write(content)


def read_audio(filename):

    r = sr.Recognizer()

    #filename = "IA.wav"

    # open the file
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data, language='es-ES')
        #print(text)
        write_f("prueba",text)
        

def read_f(name):
    with  open(name,'r') as file:
        return file.read()

if __name__ == "__main__":
    
    filetxt = read_f("prueba.txt")
    engine = pyttsx3.init()
    engine.say(filetxt)
    engine.runAndWait()



#text = r.recognize_google(audio, language='es-ES')    