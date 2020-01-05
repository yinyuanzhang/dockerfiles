FROM python:3.7.2-slim

MAINTAINER Samuel Dion-Girardeau <samuel.diongirardeau@gmail.com>

ENV ERRBOT_DIR=/errbot

RUN mkdir -p $ERRBOT_DIR

WORKDIR $ERRBOT_DIR

VOLUME ["/errbot/data", "/errbot/plugins"]

RUN apt-get update \
 && apt-get install -y \
      git \
      libssl-dev \
      libffi-dev \
      python3-dev \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./requirements.txt

RUN pip install \
      --no-cache-dir \
      --disable-pip-version-check \
      -r requirements.txt

CMD ["errbot"]
