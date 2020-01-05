FROM ubuntu:16.04
MAINTAINER Eduardo Marques <edrdo@dcc.fc.up.pt>

# Install necessary packages
RUN apt-get update && apt-get upgrade -y && apt-get install  -y \
    gcc \
    make \
    tcl \ 
    apache2 \
    apache2-suexec-pristine \
    curl \
    vim \
    lpr \
    time \
    cron \
    rsync \
    bind9-host \
    libxml2-utils \
    xsltproc \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* 

# Configure Apache
RUN \
  cd /etc/apache2/mods-enabled && \
  ln -s ../mods-available/cgi.load && \
  ln -s ../mods-available/userdir.conf && \
  ln -s ../mods-available/userdir.load && \
  ln -s ../mods-available/suexec.load

COPY apache-userdir.conf /etc/apache2/mods-available/userdir.conf

# Download and install Mooshak
ENV MOOSHAK_VERSION=1.6.3
RUN \
  cd /tmp && \
  curl -L https://mooshak.dcc.fc.up.pt/download/mooshak-$MOOSHAK_VERSION.tgz -o mooshak-$MOOSHAK_VERSION.tgz && \
  tar xvzf mooshak-$MOOSHAK_VERSION.tgz

RUN service apache2 start && \
    sleep 5 && \
    cd /tmp/mooshak-$MOOSHAK_VERSION && \
    ./install && \
    service apache2 stop && \
    rm -fr /tmp/mooshak*

EXPOSE 80

# Entry point
ENTRYPOINT service apache2 start && \
           cd /home/mooshak && \
           su mooshak 


