FROM mhart/alpine-node:latest

ADD . /puppeth_cpx-netstats
WORKDIR /puppeth_cpx-netstats

RUN npm install && npm install -g grunt-cli && grunt

EXPOSE  3000
CMD ["npm", "start"]
