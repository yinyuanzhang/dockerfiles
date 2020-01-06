FROM python:3.6-slim-buster
MAINTAINER Ofir Kelly (okelly3@gmail.com)


RUN apt-get update\
# INSTALL GCC (required for ibm-db compilation)
    && apt-get -y install gcc \
# UPDATE PIP
    && pip install --upgrade pip \
# INSTALL ibm-db
    && pip install ibm-db \
# REMOVE APT CACHE
    && rm -rf /var/lib/apt/lists/* \
# REMOVE GCC (no longer needed)
    && apt-get purge -y --auto-remove 'gcc'
