FROM ubuntu:19.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
  apt-get dist-upgrade -y && \
  apt-get install -y python3-venv python3-pip libgdal-dev git && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists*

