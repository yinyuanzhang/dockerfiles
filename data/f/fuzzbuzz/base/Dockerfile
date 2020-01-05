FROM ubuntu:xenial@sha256:76702ec53c5e7771ba3f2c4f6152c3796c142af2b3cb1a02fce66c697db24f12

MAINTAINER Everest Munro-Zeisberger

#################
# USERS N STUFF #
#################

RUN groupadd -g 999 appuser && useradd -r -u 999 -g appuser appuser | chpasswd && adduser appuser sudo
RUN mkdir /etc/sudoers.d
RUN echo "appuser ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/appuser && \
    chmod 0440 /etc/sudoers.d/appuser
RUN apt-get update && apt-get install sudo
RUN mkdir -p /home/appuser
RUN chown appuser: /home/appuser
RUN chmod 775 /home/appuser
USER appuser
ENV HOME=/home/appuser
WORKDIR /home/appuser