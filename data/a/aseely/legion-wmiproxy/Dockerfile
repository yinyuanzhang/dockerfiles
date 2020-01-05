FROM ubuntu:xenial

ADD wmi-proxy-simulator /opt/wmi-proxy-simulator

RUN apt-get update && apt-get install -y libboost-dev libboost-iostreams-dev libboost-filesystem-dev libboost-system-dev libboost-thread-dev

EXPOSE 3000/tcp

ENTRYPOINT ["/opt/wmi-proxy-simulator/bin/wmi-proxy-simulator"]

