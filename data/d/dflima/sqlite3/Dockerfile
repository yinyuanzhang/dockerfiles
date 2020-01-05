FROM debian:stable
MAINTAINER Danilo Lima <danlima69@gmail.com>

RUN apt-get update && \
    DEBIAN_FRONTEND=nointeractive \
    apt-get -y -qq install sqlite3

RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp*
