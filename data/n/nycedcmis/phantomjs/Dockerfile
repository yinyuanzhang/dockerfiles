FROM debian:jessie
LABEL maintainer.1="alehman@edc.nyc"
LABEL maintainer.2="aho@edc.nyc"

# Install runtime dependencies
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        ca-certificates \
        bzip2 \
        libfontconfig \
        python \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN set -x  \
    # Install oxfficial PhantomJS release
 && apt-get update \
 && apt-get install -y --no-install-recommends \
        curl \
 && mkdir /tmp/phantomjs \
 && curl -L https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 | tar -xj --strip-components=1 -C /tmp/phantomjs \
 && mv /tmp/phantomjs/bin/phantomjs /usr/local/bin \
 && apt-get clean \
 && rm -rf /tmp/* /var/lib/apt/lists/*

ENTRYPOINT ["phantomjs"]