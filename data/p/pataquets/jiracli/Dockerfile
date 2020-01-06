FROM python:2

RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install \
      nano vim \
  && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/ \
  && \
  pip install --no-cache-dir jiracli

ENTRYPOINT [ "jiracli" ]
