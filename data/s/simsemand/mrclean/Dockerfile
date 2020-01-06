FROM python:3.6.8-jessie

ENV TZ=Europe\Copenhagen

COPY ./requirements.txt .
COPY ./task.py /app/task.py

RUN pip install -r requirements.txt


CMD ["python", "/app/task.py"]
