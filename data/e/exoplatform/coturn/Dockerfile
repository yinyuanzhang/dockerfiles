# Dockerizing Coturn
#
# Build:    docker build -t exoplatform/coturn .
#
# Run:      docker run -ti --rm --name=coturn -p 3478:3478 -p 5349:5349 exoplatform/coturn
#           docker run -d --name=coturn -p 3478:3478 -p 5349:5349 exoplatform/coturn

FROM  exoplatform/ubuntu:18.04
LABEL maintainer="eXo Platform <docker@exoplatform.com>"

RUN apt-get -qq update && \
  apt-get -qq -y upgrade ${_APT_OPTIONS} && \
  apt-get -qq -y install ${_APT_OPTIONS} coturn=4.5.0.7* && \
  apt-get -qq -y autoremove && \
  apt-get -qq -y clean && \
  rm -rf /var/lib/apt/lists/*

COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN  chmod u+x /docker-entrypoint.sh

ENTRYPOINT ["/usr/local/bin/tini", "--", "/docker-entrypoint.sh"]
