FROM alpine:3.6

RUN apk --no-cache add \
      bash \
      python3 \
    && pip3 install awsebcli --upgrade \
    && mkdir ~/.aws

VOLUME ["~/.aws"]

CMD ["/usr/bin/eb"]
