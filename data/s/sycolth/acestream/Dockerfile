FROM ubuntu:16.04
MAINTAINER A Rinaudo <alberto.rinaudo@gmail.com>

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y curl libpython2.7 net-tools python-apsw python-lxml python-m2crypto python-pkg-resources
RUN curl -s http://dl.acestream.org/linux/acestream_3.1.16_ubuntu_16.04_x86_64.tar.gz | tar --extract --gzip
RUN mv acestream_3.1.16_ubuntu_16.04_x86_64 /opt/acestream

EXPOSE 6878 8621 62062

CMD /opt/acestream/start-engine --log-stdout --client-console
