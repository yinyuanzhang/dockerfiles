FROM python:3.7.1-alpine3.8

WORKDIR /usr/src/app
EXPOSE 80

RUN pip install --no-cache-dir flask

COPY main.py .

CMD [ "python", "./main.py" ]
