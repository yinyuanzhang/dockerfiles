FROM python:3.6-stretch
MAINTAINER Darren

ADD . /Bombax/

ENV BOMBAX_CONFIG_PATH /Bombax/deploy

WORKDIR /Bombax

RUN pip3 install -r /Bombax/requirements.txt

ENTRYPOINT ["python3", "run.py"]