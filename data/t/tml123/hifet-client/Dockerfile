#Container is being built in a Linux environment
FROM debian:stable

WORKDIR /

ADD . /

#Installation of all necessary packages and libraries for the various projects that will be run
RUN apt-get update
RUN apt-get install sudo
RUN apt-get install -y sysv-rc
RUN apt-get install -y gnupg
RUN apt-get install -y gnupg2
RUN apt-get install -y wget
RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs
RUN apt-get install -y npm
RUN apt-get install -y vim

RUN npm install -g http-server

#Exposes the various ports which allows us to connect to the container via the web browser
EXPOSE 8000

CMD ["npm", "start"]
