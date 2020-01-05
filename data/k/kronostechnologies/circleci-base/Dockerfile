FROM node:8.1.2-alpine

RUN \
    apk --no-cache -u add groff less python py-pip docker git openssh tar gzip ca-certificates && \
    pip install awscli docker-compose && \
    apk --purge del py-pip

ADD https://raw.githubusercontent.com/kronostechnologies/build/master/docker/aws-push.sh /usr/src/scripts/aws_push.sh

RUN chmod +x /usr/src/scripts/aws_push.sh

WORKDIR /usr/src/scripts/
