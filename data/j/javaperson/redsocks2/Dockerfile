FROM ubuntu:16.04

RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get -y install libevent-dev  \
    && rm -rf /var/lib/apt/lists/*

ADD ./etc/* /etc/
ADD ./bin/* /usr/bin/

EXPOSE 12345

RUN ["chmod", "+x", "/usr/bin/redsocks2"]

CMD /usr/bin/redsocks2 -c /etc/redsocks.conf