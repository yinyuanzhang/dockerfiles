FROM jenkins/jenkins:alpine
MAINTAINER Luna Allan <docker@nallar.me>

ENV LANG=C.UTF-8 \
TZ=Europe/London \
FIX_PERMISSIONS=true

USER root
COPY root/ /
RUN /bin/sh /root/install.sh

USER ${user}
