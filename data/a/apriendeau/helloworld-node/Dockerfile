FROM node:latest

ADD . /srv/app
WORKDIR /srv/app
RUN ["npm", "install"]

EXPOSE 3535
ENTRYPOINT ["node"]
