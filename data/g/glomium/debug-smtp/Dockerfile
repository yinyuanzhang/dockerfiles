FROM alpine:3.11.2
MAINTAINER Sebastian Braun <sebastian.braun@fh-aachen.de>
# base alpine template

ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
RUN apk add --no-cache python3
# base python template

EXPOSE 25

CMD python3 -u -m smtpd -c DebuggingServer 0.0.0.0:25
