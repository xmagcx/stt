# Truzz Blogg - Youtube link: https://youtu.be/q-N6IcgCqCE
# Speech recognition in Python ::: How to convert an Audio File to Text

import speech_recognition as sr
import os
#from gtts import gTTS
from fastapi import FastAPI, HTTPException,Request, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware




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
        #write_f(filetxt,text)
        return text

def read_f(name):
    with  open(name,'r', encoding='latin-1') as file:
        return file.read()


def removeAccents(word):
    repl = {'à': 'a', 'á': 'a', 'â': 'a', 'ã': 'a',
            'é': 'e', 'ê': 'e',
            'í': 'i',
            'ó': 'o', 'ô': 'o', 'õ': 'o',
            'ú': 'u', 'ü': 'u'}

    new_word = ''.join([repl[c] if c in repl else c for c in word])
    return new_word


app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def home():
    return {"<b> It's works </b>"}


def save_upload_file(upload_file: UploadFile, destination: Path) -> None:

    # https://github.com/tiangolo/fastapi/issues/426#issuecomment-542828790

    try:
        with open(destination, "wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
    finally:
        upload_file.file.close()


@app.post("/uploadfile", status_code=201)
def upload_sequences(
    file: UploadFile = File(...)
    ):
    try:
        path = str(os.path.join(os.getcwd(),"upload"))
        pathfile = str(os.path.join(os.getcwd(),"upload",file.filename))
        isExist = os.path.exists(path)
        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(path)
            print("The new directory is created!")
        
        save_upload_file(file, pathfile)
        result = read_audio(pathfile)
    except Exception as e:
        error = str(e)
        raise HTTPException(status_code=500, detail=error)
    
    response = {"response": result} 

    return response 
    