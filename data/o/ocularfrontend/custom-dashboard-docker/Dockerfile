FROM mhart/alpine-node:8

RUN echo "http://dl-2.alpinelinux.org/alpine/edge/main" > /etc/apk/repositories
RUN echo "http://dl-2.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN echo "http://dl-2.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories

#Install git
RUN apk update && apk add -y git

RUN apk add python make perl g++ build-base gcc automake autoconf nasm wget optipng libtool libpng-dev libjpeg-turbo-dev --repository http://nl.alpinelinux.org/alpine/v3.8/community/

#Install SSH
RUN apk update && apk add -y openssh
RUN rm -r /var/cache/apk/

RUN npm install -g vue@latest

CMD ["/bin/sh"]
ENTRYPOINT ["/bin/sh", "-c"]
