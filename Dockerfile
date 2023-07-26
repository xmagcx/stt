FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim-2023-07-03
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt --no-cache-dir


#ENV PORT 8080
EXPOSE 8081

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8081","--timeout-keep-alive","600"]
