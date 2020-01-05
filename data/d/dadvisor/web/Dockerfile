FROM python:3.6-slim

WORKDIR /app
COPY . /app

RUN pip install flask

EXPOSE 6000

CMD ["python", "-u", "app.py"]
