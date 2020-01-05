FROM ubuntu:18.04

RUN apt-get update && apt-get install -y iperf

COPY iperf-*.sh /
RUN  chmod 755 /iperf-*.sh
