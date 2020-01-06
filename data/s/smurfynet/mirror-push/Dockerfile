FROM docker.io/alpine:3.6

RUN apk add --no-cache lsyncd rsync openssh-client

VOLUME /root/.ssh /srv
WORKDIR /srv

ADD ./lsyncd.conf /etc/lsyncd/
ADD ./run.sh /run.sh
RUN chmod 755 /run.sh

ENV TARGETS=""

CMD ["/run.sh"]
