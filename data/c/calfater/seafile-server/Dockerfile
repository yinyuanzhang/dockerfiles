FROM calfater/base-image:ubuntu-18.04

#RUN add-apt-repository ppa:seafile/seafile-client
RUN apt-get -q update

#RUN apt-get -q -y install sqlite3
RUN apt-get -q -y install python
RUN apt-get -q -y install python2.7 libpython2.7 python-setuptools python-pil python-ldap python-urllib3 ffmpeg python-pip sqlite3 python-requests
RUN pip install pillow moviepy

RUN apt-get -q -y install nginx

ARG UNAME=seafile
ARG GNAME=seafile
ARG VERSION="6.3.1"

ENV UNAME=$UNAME
ENV GNAME=$GNAME
ENV UID=1000
ENV GID=1000
ENV VERSION="$VERSION"

ENTRYPOINT ["/bin/bash", "/home/seafile/entrypoint.sh"]

#VOLUME ["/home/seafile/config", "/home/seafile/libraries"]

COPY ["nginx-default", "/etc/nginx/sites-enabled/default"]
COPY ["entrypoint.sh", "/home/seafile/"]
COPY ["script.sh", "/home/seafile/"]
RUN ["chmod", "+x", "/home/seafile/entrypoint.sh", "/home/seafile/script.sh"]


EXPOSE 80 
