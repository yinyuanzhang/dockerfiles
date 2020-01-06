FROM debian:stable

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    iperf3 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

EXPOSE 5201

CMD ["/usr/bin/iperf3", "-s"]
