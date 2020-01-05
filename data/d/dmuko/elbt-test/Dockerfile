FROM ubuntu:12.04

RUN apt-get -y update
RUN apt-get -y install python-setuptools
RUN apt-get -y install python-dev gcc

RUN easy_install pip

ADD requirements.txt /src/requirements.txt
RUN cd /src; pip install -r requirements.txt

ADD . /src

EXPOSE 5000

CMD ["python", "/src/application.py"]
