FROM jruby:9.1.5.0-jre

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        bzip2 \
        libfontconfig \
        curl \
    && mkdir /tmp/phantomjs \
    && curl -L https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 \
           | tar -xj --strip-components=1 -C /tmp/phantomjs \
    && mv /tmp/phantomjs/bin/phantomjs /usr/local/bin \
    && apt-get clean \
    && rm -rf /tmp/* /var/lib/apt/lists/*

RUN echo "alias bec='bundle exec cucumber'" >> /root/.bashrc

RUN echo "alias bi='bundle install'" >> /root/.bashrc
