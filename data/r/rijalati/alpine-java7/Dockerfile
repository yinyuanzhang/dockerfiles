FROM gliderlabs/alpine:latest
MAINTAINER rijalati@gmail.com

RUN apk update
RUN apk add openjdk7
RUN apk add apache-ant --update-cache --repository http://dl-4.alpinelinux.org/alpine/edge/testing/ --allow-untrusted
RUN apk add git tar mksh socat
ENV ANT_HOME /usr/share/java/apache-ant
ENV PATH $PATH:$ANT_HOME/bin
CMD ["/usr/bin/java", "-version"]
