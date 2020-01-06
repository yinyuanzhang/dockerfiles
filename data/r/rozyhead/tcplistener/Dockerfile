FROM debian:jessie
MAINTAINER Takeshi Miyajima <rozyhead@gmail.com>

RUN apt-get -q update && \
    DEBIAN_FRONTEND="noninteractive" apt-get -q install -y -o Dpkg::Options::="--force-confnew" --no-install-recommends \
      socat && \
    apt-get -q autoremove && \
    apt-get -q clean && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 2375

CMD ["/usr/bin/socat", "-4", "TCP-LISTEN:2375,fork", "UNIX-CONNECT:/var/run/docker.sock"]
