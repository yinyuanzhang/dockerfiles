FROM alpine:latest
MAINTAINER nickg
WORKDIR /tmp
RUN /bin/true \
  && apk update && apk upgrade \
  && apk add python3 bash git \
  && git clone --depth=1 https://github.com/openstack-dev/pbr.git \
  && cd pbr \
  && python3 setup.py install \
  && cd /tmp \
  && git clone --depth=1 https://github.com/openstack-dev/bashate.git \
  && cd bashate \
  && python3 setup.py install \
  && cd /tmp \
  && rm -rf pbr bashate \
  && apk del git \
  && rm -rf /var/cache/apk/*
USER daemon
ENTRYPOINT [ "/usr/bin/bashate" ]
