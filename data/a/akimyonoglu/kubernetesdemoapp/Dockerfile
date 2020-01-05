FROM alpine

RUN apk add --update python python-dev py-pip && rm -rf /var/cache/apk/*

WORKDIR /src
COPY ./src .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
