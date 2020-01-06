FROM alpine:3.7

ADD https://gitlab.com/finestructure/pipeline-trigger/raw/master/trigger.py \
    https://raw.githubusercontent.com/petervanderdoes/gitflow-avh/develop/contrib/gitflow-installer.sh \
    /usr/local/share/

RUN apk update \
   &&  apk upgrade \
   &&  apk add --no-cache bash git sudo curl openssh sed python3 docker \
   &&  apk add --no-cache coreutils \
   &&  pip3 install python-gitlab==1.8.0 \
   &&  adduser -D -u 1000 builduser \
   &&  echo "builduser ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/builduser \
   &&  chmod 0440 /etc/sudoers.d/builduser \
   &&  ln -s /usr/bin/python3 /usr/bin/python \
   &&  ln -s /usr/local/share/trigger.py /usr/bin/trigger \
   &&  chmod a+rx /usr/bin/trigger \
   &&  chmod a+rx /usr/local/share/gitflow-installer.sh \
   &&  /usr/local/share/gitflow-installer.sh install stable \
   &&  rm -rf /var/cache/apk/*
USER builduser