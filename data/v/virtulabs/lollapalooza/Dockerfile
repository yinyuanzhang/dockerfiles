FROM ubuntu

ENV TEMP=/tmp \
  HOME=/home/root \
  TARGET_ARCH=x64 \
  DEBIAN_FRONTEND=noninteractive

ADD build.sh .
RUN bash build.sh && rm build.sh

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
