FROM php:cli-alpine
MAINTAINER Olivier Mouren <mouren.olivier@gmail.com>

RUN apk add --update openssh-client rsync

RUN mkdir /deployer

RUN cd /deployer && curl -LO https://deployer.org/deployer.phar \
&& mv deployer.phar /usr/local/bin/dep \
&& chmod +x /usr/local/bin/dep

VOLUME ["/app"]
WORKDIR /app

ENTRYPOINT ["dep"]