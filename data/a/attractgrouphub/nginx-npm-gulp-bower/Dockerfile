FROM debian:latest

MAINTAINER AttractGroup

RUN apt-get update && apt-get install -y nginx nginx-extras curl git

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -

RUN apt-get install -y nodejs

RUN npm install -g bower && npm install -g gulp

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]