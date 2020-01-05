#@# vim: set filetype=dockerfile:
FROM python:3.8.0
MAINTAINER Takahiro INOUE <hinata@mail.3dcg-arts.net>

ENV DEBIAN_FRONTEND noninteractive
ENV WORK_ROOT_DIR /work

WORKDIR /tmp

####
## dependent packages for docker build
####

RUN apt update        && \
    apt -y install       \
      build-essential

ADD ./requirements.txt .

RUN pip install -r requirements.txt

####
## application deployment
####

WORKDIR ${WORK_ROOT_DIR}

ADD . ${WORK_ROOT_DIR}

EXPOSE 50051

CMD [ "python", "-u", "./server.py", "--bind=0.0.0.0", "--port=50051", "--database=./database_example.json" ]
