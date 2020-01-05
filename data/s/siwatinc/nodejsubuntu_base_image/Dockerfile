FROM siwatinc/ubuntubaseimage_unraid:latest
RUN apt-get -y update
RUN apt-get install -y g++ gcc make
RUN curl -sSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | sudo apt-key add - 
RUN echo "deb https://deb.nodesource.com/node_12.x bionic main" | sudo tee /etc/apt/sources.list.d/nodesource.list 
RUN apt-get install -f -y
RUN apt-get update
RUN aptitude -y install nodejs npm
