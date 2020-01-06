FROM jdeathe/centos-ssh:latest@sha256:808153e5a72a4e0e0683a4c445bb8b3bb5f6c01cba5ee3eb5cc059ea3bd565c8

RUN yum install -y vim

RUN yum install -y wget \
 && wget -qO- https://get.docker.com/ | sh \
 && systemctl enable docker.service

RUN yum install -y python-pip \
 && pip install docker-compose