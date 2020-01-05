FROM python:2.7-slim

MAINTAINER Richard Mathie "Richard.Mathie@amey.co.uk"

RUN apt-get update \
    && apt-get install -y gcc python-dev \
    && apt-get install -y libev4 libev-dev \
    && pip install --no-cache-dir six futures lz4 twisted gevent eventlet cython pytz scales \
    && pip install --no-cache-dir cassandra-driver \
    && apt-get -y purge gcc python python-dev \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf ~/.cache /var/lib/apt/lists/* /tmp/* /var/tmp/*

