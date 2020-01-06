FROM ubuntu

RUN apt-get update
RUN apt-get install -y git nodejs npm
RUN ln -s /usr/bin/nodejs /usr/bin/node

EXPOSE 25

ENV NODE_ENV production

ADD bin/entrypoint /entrypoint

ENTRYPOINT /entrypoint