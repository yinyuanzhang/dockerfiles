FROM alpine:3.6

MAINTAINER Sijo K George <cijo_k_george@yahoo.co.in>

RUN apk add --update python3 openssl groff && \
  wget -O /tmp/awscli-bundle.zip https://s3.amazonaws.com/aws-cli/awscli-bundle.zip && \
  unzip -d /tmp/ /tmp/awscli-bundle.zip && \
  python3 /tmp/awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \
  rm -f /tmp/awscli-bundle.zip && \
  rm -rf /tmp/awscli-bundle

# Busybox version of less doesn't support -R flag,
# thus default PAGER settings in AWS CLI won't work
ENV PAGER="more"

ENTRYPOINT ["/bin/ash"]

WORKDIR /root
