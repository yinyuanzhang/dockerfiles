FROM python:3.6

RUN pip install flask

RUN mkdir /app
WORKDIR /app
COPY app.py ./

CMD ["python", "app.py"]
