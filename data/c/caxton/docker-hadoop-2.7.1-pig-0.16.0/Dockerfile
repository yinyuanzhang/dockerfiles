FROM sequenceiq/hadoop-docker:2.7.1
MAINTAINER Caxton Chan <kaifu.chan@gmail.com>

RUN curl -LO http://ftp.tc.edu.tw/pub/Apache/pig/pig-0.16.0/pig-0.16.0.tar.gz
RUN tar xzf pig-0.16.0.tar.gz

ENV PATH $PATH:/pig-0.16.0/bin

ENV PATH="$PATH:/usr/local/hadoop-2.7.1/bin:/usr/local/hadoop-2.7.1/sbin"

RUN mkdir /home/pig/
COPY ./pig_data /home/pig/
