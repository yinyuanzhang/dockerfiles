FROM alpine:latest

WORKDIR /root

RUN apk --no-cache update && \
  apk --no-cache add python py-pip jq bash zip ca-certificates && \
  pip --no-cache-dir install awscli && \
  apk --no-cache del py-pip && \
  rm -rf /var/cache/apk/*

RUN echo "alias md5=md5sum" >> /etc/profile

ENTRYPOINT [ "/bin/bash", "--login" ]