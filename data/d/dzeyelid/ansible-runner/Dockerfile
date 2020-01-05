FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y \
    software-properties-common

RUN apt-add-repository ppa:ansible/ansible

RUN apt-get update -y

RUN apt-get install -y \
    ansible \
    git

ENV WORK_DIR /project
ENV WORK_USER ansible

RUN useradd -m -U ${WORK_USER}

RUN mkdir ${WORK_DIR} && \
    chown -R ${WORK_USER}:${WORK_USER} ${WORK_DIR}

USER ansible:ansible

WORKDIR ${WORK_DIR}

CMD ansible localhost -m ping