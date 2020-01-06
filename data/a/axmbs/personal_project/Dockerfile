FROM python:latest AS alexpython
COPY requirements.txt /
RUN pip install -r requirements.txt

COPY python /app
WORKDIR /app

CMD ["python3", "main.py"]