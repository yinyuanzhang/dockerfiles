FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    apt-add-repository ppa:ansible/ansible && \
    apt-get update && \
    apt-get install -y ansible vim

RUN echo '[local]\nlocalhost\n' > /etc/ansible/hosts
