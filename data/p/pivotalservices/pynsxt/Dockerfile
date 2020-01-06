FROM ubuntu:latest

ADD pynsxt/ /opt/pynsxt/

# install base python packages and PyNSXt
RUN \
  apt-get update && \
  apt-get upgrade -y && \
  apt-get -y install python-pip openssl libxml2 libxml2-dev libxslt1-dev libssl-dev libffi-dev python-dev build-essential && \
  pip install --upgrade setuptools && \
  python /opt/pynsxt/setup.py install --user
