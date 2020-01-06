FROM python:3.6-alpine

RUN apk add --no-cache curl python pkgconfig python-dev openssl-dev libffi-dev musl-dev make gcc

ADD requirements.txt /

RUN pip install -r requirements.txt

RUN mkdir .test_files

ADD . /

ENTRYPOINT ["python", "app.py"]