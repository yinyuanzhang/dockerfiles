FROM mhart/alpine-node:9

ADD . /eth-netstats
WORKDIR /eth-netstats

RUN npm install && npm install -g grunt-cli && grunt all

EXPOSE  3000
CMD ["npm", "start"]
