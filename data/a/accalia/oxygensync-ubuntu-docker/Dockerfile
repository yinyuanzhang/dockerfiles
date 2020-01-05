FROM ubuntu

LABEL maintainer="docker@elementia.me"

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8


EXPOSE 26504/tcp 26504/udp 26511/tcp 26511/udp

# VOLUME /home/ubuntu
ADD app /app

RUN \
  groupadd -g 1000 ubuntu \
  && \
  useradd --uid 1000 --shell /bin/bash -m --home-dir /home/ubuntu -g ubuntu ubuntu \
  && \
  chown -R ubuntu:ubuntu /home/ubuntu \
  && \
  chown -R ubuntu:ubuntu /app

USER ubuntu

WORKDIR /app

CMD ["/bin/bash", "/app/run.sh"]