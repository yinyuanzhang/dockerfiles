FROM python:3.6

RUN mkdir /opt/thanksbot
WORKDIR /opt/thanksbot

COPY . /opt/thanksbot
RUN pip install -r requirements.txt

ENTRYPOINT sh run.sh
