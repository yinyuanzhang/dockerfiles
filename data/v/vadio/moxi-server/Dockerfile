FROM ubuntu:12.04

ENV DEB=moxi-server_2.5.0_x86_64.deb
ENV MOXI=http://packages.couchbase.com/releases/2.5.0/$DEB

RUN apt-get -y install curl

RUN curl -O $MOXI \
    && dpkg -i $DEB \
    && rm $DEB

ENTRYPOINT ["/opt/moxi/bin/moxi"]
EXPOSE 11211
