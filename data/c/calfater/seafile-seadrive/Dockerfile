FROM calfater/base-image:ubuntu-16.04

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 8756C4F765C9AC3CB6B85D62379CE192D401AB61
# jessie for Debian / xenial for Ubuntu 16.04
RUN echo deb http://deb.seadrive.org xenial main | tee /etc/apt/sources.list.d/seafile.list
RUN apt-get -q update
RUN apt-get -q -y install curl fuse seadrive-daemon

ARG UNAME=seadrive
ARG GNAME=seadrive

ENV UNAME=$UNAME
ENV GNAME=$GNAME

ENV UID=1000
ENV GID=1000

ENTRYPOINT ["/bin/bash", "/home/seadrive/entrypoint.sh"]

VOLUME ["/config", "/drive"]

COPY ["scripts/", "/home/seadrive"]
COPY ["conf/", "/home/seadrive"]
RUN chmod +x /home/seadrive/*.sh
RUN ["ln", "-s", "/home/seadrive/configure.sh", "/configure" ]

