FROM python:3.6-slim

WORKDIR /app
RUN mkdir -p /mldata

COPY . . 
RUN pip3 install --no-cache-dir --compile -r requirements.txt

