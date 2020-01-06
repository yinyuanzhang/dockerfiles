FROM pataquets/ubuntu:xenial

RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y --no-install-recommends install sslh \
  && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

ENTRYPOINT [ "sslh", "-f" ]
CMD [ "-p", "0.0.0.0:22", "-p", "0.0.0.0:80", "-p", "0.0.0.0:443", "--ssh", "ssh:22", "--http", "http:80", "--ssl", "ssl:443" ]
