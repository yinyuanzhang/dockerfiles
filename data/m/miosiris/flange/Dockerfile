FROM python:3.6-stretch

MAINTAINER OpenLab <ezkissel@indiana.edu>

EXPOSE 8000/tcp
EXPOSE 8001/tcp
EXPOSE 9001/tcp

RUN apt-get update
RUN apt-get -y install sudo cmake gcc libaprutil1-dev libapr1-dev lldpd python-setuptools python-pip supervisor
RUN sudo pip3 install tornado

RUN export uid=1000 gid=1000 && \
    mkdir -p /home/osiris && \
    echo "osiris:x:${uid}:${gid}:OSIRIS,,,:/home/osiris:/bin/bash" >> /etc/passwd && \
    echo "osiris:x:${uid}:" >> /etc/group && \
    echo "osiris ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/osiris && \
    chmod 0440 /etc/sudoers.d/osiris && \
    chown ${uid}:${gid} -R /home/osiris && \
    chown ${uid}:${gid} -R /opt
    
USER osiris
ENV HOME /home/osiris
WORKDIR $HOME

RUN git config --global user.email "osiris@osiris-peri"
RUN git config --global user.name "OSIRIS"

RUN git clone -b develop https://github.com/periscope-ps/unisrt
RUN git clone -b master https://github.com/periscope-ps/lace
RUN git clone -b develop https://github.com/periscope-ps/Flange

ADD build.sh .
RUN bash ./build.sh

ADD flanged_conf.ini /etc/flanged/flanged_conf.ini
ADD flange.conf /etc/supervisor/conf.d/
ADD fladmin_conf.ini /etc/flanged/fladmin_conf.ini

ENV DEBUG DEBUG
ADD run.sh .
CMD bash ./run.sh
