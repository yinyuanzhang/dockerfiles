FROM ubuntu:16.04

# Upgrade base system
RUN apt-get update
WORKDIR /venv
COPY cpudata.sh /venv
RUN chmod a+x /venv/*
CMD ./cpudata.sh
