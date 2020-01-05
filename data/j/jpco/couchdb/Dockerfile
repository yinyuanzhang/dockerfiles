FROM debian:jessie as build

MAINTAINER  J.P.C. Oudeman

# Loosely based on instructions from https://docs.couchdb.org/en/latest/install/unix.html#installation-from-source

ARG VERSION=2.3.0

RUN apt-get update 
RUN apt-get --no-install-recommends -y install \
    build-essential \
    pkg-config \
    erlang \
    libicu-dev \
    libmozjs185-dev \
    libcurl4-openssl-dev \
    wget
# Install CouchDB 
RUN wget --no-check-certificate --header="accept-encoding: gzip" https://github.com/apache/couchdb/releases/download/$VERSION/apache-couchdb-$VERSION.tar.gz -O - | tar -C /tmp -xz
WORKDIR /tmp/apache-couchdb-$VERSION
RUN ./configure --disable-docs
RUN make release
RUN mv ./rel/couchdb /tmp/couchdb

FROM debian:jessie
COPY --from=build /tmp/couchdb /usr/local/lib/couchdb
COPY assets/bin/entrypoint.sh /usr/local/bin

RUN apt-get update \ 
&& apt-get --no-install-recommends -y install \
    erlang \
    libmozjs185-1.0 \
    libicu52 \
    libcurl4-openssl-dev \
    sudo \
# Set up a couchdb daemon account
&& groupadd -r couchdb \
&& useradd -d /var/lib/couchdb -g couchdb couchdb \
&& chmod +x /usr/local/bin/*.sh \
&& chown -R couchdb:couchdb /usr/local/lib/couchdb \
\
# Cleanup
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

ENV COUCHDB_USER=couchadmin \
COUCHDB_PASSWORD=couchpasswd 
VOLUME /usr/local/lib/couchdb/data

ENTRYPOINT ["entrypoint.sh"]
CMD ["/usr/local/lib/couchdb/bin/couchdb"]
