FROM mono:latest
LABEL maintainer="danny@sotzny.de"

RUN apt-get update \
  && apt-get install -y ssh \
  && rm -rf /var/lib/apt/lists/* /tmp/*
