FROM alpine:3.2
MAINTAINER Ian Neubert <ian@ianneubert.com>

RUN mkdir /data
RUN apk --update add \ 
      less \
      groff \
      python \
      py-pip \
      jq \
      curl \
      bash && \
      pip install --upgrade awscli s3cmd && \
      mkdir /root/.aws

ENTRYPOINT ["aws"]
WORKDIR /data
