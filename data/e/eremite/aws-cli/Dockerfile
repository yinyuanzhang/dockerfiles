FROM alpine:3.8
ENV EDITOR vi # For Elastic Beanstalk
RUN apk -v --update add \
  ca-certificates \
  git \
  groff \
  jq \
  less \
  mailcap \
  openssh \
  openssl \
  py-pip \
  python \
  && update-ca-certificates \
  && pip install --upgrade \
  pip==19.0.1 \
  awscli==1.16.96 \
  s3cmd==2.0.2 \
  awsebcli==3.14.10 \
  python-magic \
  && rm /var/cache/apk/*
