FROM mhart/alpine-node:9

ADD . /ethstats-server
WORKDIR /ethstats-server

RUN npm install && npm install -g grunt-cli && /usr/bin/grunt poa

EXPOSE  3000
CMD ["npm", "start"]
