FROM python:3.7.2-alpine

RUN apk add --no-cache --update alpine-sdk
RUN pip install mmh3
COPY main.py ./
ENTRYPOINT ["python","main.py"]
