FROM ubuntu:precise

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gcc \
    python \
    python-dev \
    python-pip \
    python-yaml \
    sudo \
  && rm -rf /var/lib/apt/lists/*

RUN pip install ansible==1.9.4
