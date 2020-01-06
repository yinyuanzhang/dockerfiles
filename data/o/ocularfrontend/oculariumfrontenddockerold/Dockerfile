FROM mhart/alpine-node:8

RUN echo "http://dl-2.alpinelinux.org/alpine/edge/main" > /etc/apk/repositories
RUN echo "http://dl-2.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN echo "http://dl-2.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories

#Install git
RUN apk update && apk add -y git

#Install SSH
RUN apk update && apk add -y openssh

RUN npm install -g ember-cli@2.11.0

RUN npm install -g bower

RUN npm install -g phantomjs@2.1 --unsafe-perm

CMD ["/bin/sh"]
ENTRYPOINT ["/bin/sh", "-c"]