FROM node

RUN apt-get update -y && apt-get upgrade -y

RUN curl -kL https://bootstrap.pypa.io/get-pip.py | python
RUN apt-get install -y python2.7-dev
RUN apt-get install -y groff-base

RUN pip install awscli

