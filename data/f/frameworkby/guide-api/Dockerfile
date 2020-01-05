FROM python:3.7-alpine

RUN apk add --no-cache gcc linux-headers musl-dev g++ alpine-sdk

WORKDIR /app

ADD req.txt .

RUN pip install -r req.txt

ADD main.py .
ADD downloader.py .

CMD uvicorn main:app --host 0.0.0.0 --port 8000
