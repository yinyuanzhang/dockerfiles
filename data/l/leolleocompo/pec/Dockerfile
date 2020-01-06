FROM lissonpsantos2/debian-jessie-basic:latest

LABEL maintainer="Leonardo Cavalcante do Prado <leolleo.comp@gmail.com>"

ENV PEC_FOLDER /opt/e-SUS/jboss-as-7.2.0.Final/bin/init.d/jboss-as-standalone-lsb.sh
ENV IMAGE_ALIAS ESUS 3.0.13
ENV PEC_FOLDER mkdir -p /var/lock/subsys/ \
    && service e-SUS-AB-PostgreSQL restart \
    && service e-SUS-AB-PostgreSQL start \
    && sh /opt/e-SUS/jboss-as-7.2.0.Final/bin/init.d/jboss-as-standalone-lsb.sh restart

ENV SEPARATOR -
ENV INFO_IMAGE "To start the PEC3.2.2 run: sh ${PEC_FOLDER} start"

RUN mkdir /home/PEC \
    && apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y openjdk-7-jdk

WORKDIR /home/PEC

RUN wget https://arquivos.bridge.ufsc.br/AB/PEC/3.2.17/treinamento/instalador/Instalador-eSUS-AB-PEC-3.2.17-Treinamento-Linux.zip -O pec.zip \
    && unzip pec.zip -d /home/PEC/install

WORKDIR /home/PEC/install

RUN curl -o /etc/locale.gen https://raw.githubusercontent.com/leolleocomp/pec-docker-image/master/locale \
    && curl -o /etc/java.conf https://raw.githubusercontent.com/leolleocomp/pec-docker-image/master/javaconf \
    && apt-get install -y locales \
    && locale-gen \
    && sh instalador_linux.sh

WORKDIR /

ENTRYPOINT mkdir -p /var/lock/subsys/ \
    && service e-SUS-AB-PostgreSQL restart \
    && service e-SUS-AB-PostgreSQL start \
    && sh /opt/e-SUS/jboss-as-7.2.0.Final/bin/init.d/jboss-as-standalone-lsb.sh start ; /bin/bash
