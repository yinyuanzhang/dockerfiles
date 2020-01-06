FROM alpine
MAINTAINER Nektria "it@nektria.com"

RUN apk --update add beanstalkd

RUN rm -rf /var/cache/apk/*

RUN mkdir -p /data

EXPOSE 11300

CMD ["beanstalkd", "-p", "11300"]
