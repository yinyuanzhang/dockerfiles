FROM ubuntu:trusty

RUN apt-get update && apt-get install -y build-essential curl \
    && cd /tmp \
    && curl -L https://github.com/dpw/iperf/tarball/master | tar xzf - \
    && cd dpw-iperf-* \
    && ./configure --prefix=/usr \
    && make install \
    && cd .. \
    && rm -rf dpw-iperf-* \
    && apt-get purge -y build-essential curl

EXPOSE 5201
ENTRYPOINT ["/usr/bin/iperf3"]
CMD ["-s"]
