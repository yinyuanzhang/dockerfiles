FROM irakli/alpine-nodejs:latest

MAINTAINER "Irakli Nadareishvili"
ENV REFRESHED_AT 2015-10-28-23_00

RUN echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
 && apk --update upgrade && apk add runit && rm -rf /var/cache/apk/* && apk --update search
ADD runit_init /sbin/
RUN chmod u+x /sbin/runit_init

CMD ["/sbin/runit_init"]
