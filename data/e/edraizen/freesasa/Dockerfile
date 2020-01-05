FROM ubuntu:12.04

# install necessary dependencies
RUN apt-get update && \
    apt-get install -y build-essential wget libjson0 libjson0-dev libxml2 libxml2-dev libxml2-utils autoconf automake libtool

WORKDIR /opt

RUN wget --no-check-certificate https://s3.amazonaws.com/json-c_releases/releases/json-c-0.13.1.tar.gz
RUN tar -xzf json-c-0.13.1.tar.gz
WORKDIR /opt/json-c-0.13.1
RUN ./configure --prefix=/usr --disable-static
RUN make && make install

WORKDIR /opt
RUN rm json-c-0.13.1.tar.gz
RUN rm -r json-c-0.13.1

RUN wget http://freesasa.github.io/freesasa-2.0.3.tar.gz
RUN tar -xzf freesasa-2.0.3.tar.gz
WORKDIR /opt/freesasa-2.0.3
RUN ./configure CFLAGS="-fPIC -O2" --prefix=`pwd` --disable-xml
RUN make
RUN make install

WORKDIR /opt
RUN rm freesasa-2.0.3.tar.gz

COPY wrapper.sh /opt/freesasa-2.0.3

RUN mkdir /data
WORKDIR /data

ENTRYPOINT ["sh", "/opt/freesasa-2.0.3/wrapper.sh"]
