FROM jalaziz/base:alpine

RUN  apk add --update python py2-pip groff less \
  && pip install awscli \
  && apk del py2-pip \
  && rm -rf /var/cache/apk/*

ENTRYPOINT [ "/usr/bin/aws" ]
