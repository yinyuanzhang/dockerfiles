FROM node:8.12.0

# install docker
RUN apt-get -y update; \
    apt-get -y install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -

RUN add-apt-repository -y \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"

RUN apt-get -y update

RUN apt-get -y install docker-ce


VOLUME [ "/var/lib/docker"]