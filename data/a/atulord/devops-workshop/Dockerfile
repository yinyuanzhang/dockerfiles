FROM mhart/alpine-node

MAINTAINER Chuka Ebi <chukaebi@yahoo.com>

ADD /unicorn /unicorn

WORKDIR /unicorn

RUN npm install

EXPOSE 5000

CMD ["node", "app.js"]
