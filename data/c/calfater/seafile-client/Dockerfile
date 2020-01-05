FROM calfater/base-image:ubuntu-18.04

RUN add-apt-repository ppa:seafile/seafile-client
RUN apt-get -q update
RUN apt-get -q install -y seafile-cli

ARG UNAME=seafile
ARG GNAME=seafile

ENV UNAME=$UNAME
ENV GNAME=$GNAME

ENV UID=1000
ENV GID=1000

ENTRYPOINT ["/bin/bash", "/home/seafile/entrypoint.sh"]

VOLUME ["/home/seafile/config", "/home/seafile/libraries"]

COPY ["entrypoint.sh", "/home/seafile/"]
COPY ["script.sh", "/home/seafile/"]
RUN ["chmod", "+x", "/home/seafile/entrypoint.sh", "/home/seafile/script.sh"]

