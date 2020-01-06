FROM alpine

RUN apk update -f && apk --no-cache add -f \
  git \
  openssh

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

VOLUME /root/.ssh
ENTRYPOINT /entrypoint.sh
