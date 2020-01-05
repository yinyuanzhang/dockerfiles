FROM alpine:3.5

MAINTAINER Oleks <oleks@oleks.info>

RUN apk --no-cache add build-base

RUN apk --no-cache add ruby ruby-irb

RUN adduser -D -u 1000 docker
USER docker

WORKDIR /home/docker/

ENV PATH=/home/docker/.local/bin:$PATH

CMD ["irb"]
