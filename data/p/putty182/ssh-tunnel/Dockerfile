FROM alpine
MAINTAINER putty182

RUN apk add --update openssh-client && rm -rf /var/cache/apk/*
COPY init.sh /
RUN chmod +x /init.sh
CMD sh -c /init.sh
