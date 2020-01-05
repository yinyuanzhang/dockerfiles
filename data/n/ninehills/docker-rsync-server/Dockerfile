FROM debian:stretch
MAINTAINER Tao Yang <swulling@gmail.com>

RUN apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends rsync && \
  apt-get clean autoclean && \
  apt-get autoremove -y && \
  rm -rf /var/lib/apt/lists/*

EXPOSE 873
VOLUME /data

ADD ./run /usr/local/bin/run
RUN chmod a+x /usr/local/bin/run

ENTRYPOINT ["/usr/local/bin/run"]
