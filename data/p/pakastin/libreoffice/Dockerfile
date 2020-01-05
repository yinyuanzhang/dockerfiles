FROM ubuntu:trusty

RUN apt-get -y update
RUN apt-get -y install default-jre
RUN apt-get -y install --no-install-recommends libreoffice 

ENTRYPOINT ["libreoffice"]
