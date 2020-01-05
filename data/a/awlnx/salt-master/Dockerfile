FROM alpine:latest
MAINTAINER Annika Wickert <aw@awlnx.space>
RUN apk add salt-master

RUN adduser -Ss /bin/false saltapi
RUN echo "saltapi:saltapi" | chpasswd

CMD salt-master
