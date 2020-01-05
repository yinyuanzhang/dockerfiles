FROM debian:buster-slim

RUN apt-get update -qq
RUN apt-get install -y wget make git python-pip

# From the latest source
RUN pip install --upgrade --force-reinstall git+https://github.com/ewels/MultiQC.git
