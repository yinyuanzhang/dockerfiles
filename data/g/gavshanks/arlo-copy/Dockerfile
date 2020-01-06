FROM python:3.6-alpine

COPY /docker/requirements.txt /

RUN pip install -r /requirements.txt

COPY /docker/src/ /app
WORKDIR /app

VOLUME [ "/videos" ]

ENV ARLOUSER something@somewhere.com
ENV ARLOPASSWORD supersecure

CMD [ "python", "./arlo-test.py" ]