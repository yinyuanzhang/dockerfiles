FROM frolvlad/alpine-oraclejdk8:8.192.12-slim
RUN apk --update add bash openssl
RUN apk --update add python py-pip py-setuptools groff
RUN pip install awscli
RUN rm -rf /var/cache/apk/* /tmp/*
