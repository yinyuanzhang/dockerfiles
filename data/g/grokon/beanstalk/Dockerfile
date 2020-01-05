FROM alpine:3.8
# set mainainer
LABEL maintainer="Grokon"
# add beanstalkd
RUN apk add --no-cache --update beanstalkd
# set volume
VOLUME [ "/var/lib/beanstalkd" ]
# set ports
EXPOSE 11300/TCP
# Define default command.
CMD ["beanstalkd", "-V", "-f", "0", "-b", "/var/lib/beanstalkd", "-l", "127.0.0.1"]