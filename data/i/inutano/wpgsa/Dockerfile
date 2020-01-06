# Docker container for wPGSA
# See https://github.com/eiryo-kawakami/wPGSA
# VERSION 0.5.2

# Pull base image.
FROM inutano/research-base:0.1.1

MAINTAINER Tazro Inutano Ohta, inutano@gmail.com

USER root

ENV CONTAINER_USER nijntje

RUN cd /home/$CONTAINER_USER/work && \
  git clone -b 0.4.2 https://github.com/inutano/wPGSA && \
  cd /home/$CONTAINER_USER/work/wPGSA && \
  chmod 755 /home/$CONTAINER_USER/work/wPGSA/wPGSA.py && \
  chmod 755 /home/$CONTAINER_USER/work/wPGSA/hclust.py && \
  ln -s /home/$CONTAINER_USER/work/wPGSA/wPGSA.py /usr/bin/wpgsa && \
  ln -s /home/$CONTAINER_USER/work/wPGSA/hclust.py /usr/bin/hclust

USER nijntje