FROM alpine:3.7

RUN addgroup -S beanstalkd && adduser -S -G beanstalkd beanstalkd

ENV BEANSTALKD_VERSION 1.10

RUN apk add --no-cache 'su-exec>=0.2'

RUN apk --update add beanstalkd && \
    rm -rf /tmp/* && \
    rm -rf /var/cache/apk/*

RUN mkdir -p /var/lib/beanstalkd \
    && chown beanstalkd:beanstalkd /var/lib/beanstalkd

VOLUME /var/lib/beanstalkd

EXPOSE 11300

ENTRYPOINT ["beanstalkd", "-l", "0.0.0.0", "-p", "11300", "-u", "beanstalkd", "-b", "/var/lib/beanstalkd"]
CMD ["-z", "65535"]
