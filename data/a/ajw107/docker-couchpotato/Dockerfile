FROM lsiobase/alpine.python:3.5
MAINTAINER sparklyballs, ajw107 (Alex Wood)

# set python to use utf-8 rather than ascii.
ENV PYTHONIOENCODING="UTF-8"

#add extra environment settings
ENV CONFIG="/config"
ENV APPDIRNAME="couchpotato"
ENV APP_ROOT="/app"
ENV APP_OPTS="--config_file=${CONFIG}/config.ini --data_dir=${CONFIG}/data"
ENV APP_EXEC="CouchPotato.py"
ENV APP_COMP="python"
ENV GITURL="https://github.com/CouchPotato/CouchPotatoServer.git"
ENV GITBRANCH="develop"

#make life easy for yourself
RUN apk update && \
    apk add nano git
ENV TERM=xterm-color
RUN echo $'#!/bin/bash\nls -alF --color=auto --group-directories-first --time-style=+"%H:%M %d/%m/%Y" --block-size="\'1" $@' > /usr/bin/ll
RUN chmod +x /usr/bin/ll

# add local files
COPY root/ /

# ports and volumes
EXPOSE 5050
WORKDIR "${APP_ROOT}/${APPDIRNAME}"
VOLUME "${CONFIG}" /mnt
