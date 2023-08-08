
===
## Project Information
- Title:  `API - Speach To Text`


## Install & Dependence
- python 3.10
- Docker


## Use
- using python
  ```
  python3 pip install -r requirements.txt
  python3 -m uvicorn app:app --host 0.0.0.0 --port 8080 --reload --timeout-keep-alive 600
  ```
- using docker
  ```
  docker build -t stt:latest .
  docker run -d -p 8080:80 stt:latest
  ```
## Execute

- using python
  ```
  import requests
  myurl = 'http://localhost:8080/uploadfile/'
  files = {'file': (open(r'C:/Users/mauri/Downloads/IA.wav', 'rb'))}
  getdata = requests.post(myurl, files=files)
  print(getdata.text)

  ```

## Directory Hierarchy
```
|—— .gitignore
|—— Dockerfile
|—— LICENCE
|—— app.py
|—— readme.MD
|—— requirements.txt
```

## References
- N/A
  
## License
- MIT
