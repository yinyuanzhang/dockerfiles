FROM ubuntu:14.04

RUN apt-get update && apt-get install -y nodejs nodejs-legacy npm 

RUN mkdir -p /srv/www
ADD . /srv/www
WORKDIR /srv/www

RUN npm install

EXPOSE  8080
CMD ["node", "src/index.js"]