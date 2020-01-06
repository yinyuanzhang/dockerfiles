FROM alpine:latest
MAINTAINER ZzenlD

RUN apk add --no-cache bash ssmtp gettext

COPY run.sh /run.sh

ENV SMTP_PORT=587 \
    LISTEN_PORT=55555

CMD /run.sh
