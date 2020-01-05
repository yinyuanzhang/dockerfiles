
FROM docker.io/exaile/gst-python:ubuntu19.04
MAINTAINER Dustin Spicuzza <dustin@virtualroadside.com>

RUN true \
  && export DEBIAN_FRONTEND=noninteractive \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
    python-pytest \
    python-mox3 \
    make \
    curl \
    ca-certificates \
  && rm -rf /var/lib/apt/lists/*

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
  && python get-pip.py

RUN pip install setuptools wheel
RUN pip install sphinx sphinx-rtd-theme

