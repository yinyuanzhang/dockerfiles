FROM alpine:latest AS builder
WORKDIR /build
RUN apk update ;\
    apk upgrade ;\
    apk add gcc curl make musl-dev ;\
    addgroup build ;\
    adduser -D -h /build -s /bin/sh -G build builder
USER builder
RUN curl -LOJ https://github.com/beanstalkd/beanstalkd/archive/v1.11.tar.gz ;\
    tar -zxvf beanstalkd-1.11.tar.gz ;\
    cd beanstalkd-1.11 ;\
    make

FROM alpine:latest
LABEL net.easypo.docker.software="beanstalkd"
RUN apk update ;\
    apk upgrade ;\
    addgroup beanstalk ;\
    adduser -D -h / -s /sbin/nologin -G beanstalk beanstalk ;\
    mkdir /data ;\
    chown beanstalk:beanstalk /data
COPY --from=builder /build/beanstalkd-1.11/beanstalkd /usr/bin/beanstalkd
VOLUME /data
USER beanstalk
EXPOSE 11300
CMD ["/usr/bin/beanstalkd", "-b", "/data", "-c", "-f", "1000"]
STOPSIGNAL 15
