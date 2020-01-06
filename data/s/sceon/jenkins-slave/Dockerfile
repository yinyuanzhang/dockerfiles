FROM docker:1.8.2-dind

RUN apk add --update \
    bash \
    openssh \
    git \
    openjdk7-jre

COPY wrapper.sh /usr/local/bin/wrapper

ENTRYPOINT ["/usr/local/bin/wrapper"]

CMD []
