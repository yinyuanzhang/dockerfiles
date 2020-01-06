FROM node:latest

ADD . /srv/http/front

WORKDIR /srv/http/front

RUN npm install
RUN npm run build

VOLUME ["/srv/http/front"]

CMD ["/bin/true"]
