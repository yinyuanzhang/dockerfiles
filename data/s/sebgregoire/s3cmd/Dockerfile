FROM ubuntu:trusty
MAINTAINER sebastien@cakemail.com

RUN apt-get update -yqq && \
    apt-get install -yqq s3cmd

ADD files/s3cfg /root/.s3cfg
ADD files/run.sh /run.sh

VOLUME [ "/source", "/destination" ]

WORKDIR /
ENTRYPOINT ["/run.sh"]
