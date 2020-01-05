FROM mysql:5.6

ENV RIDGEPOLE_VERSION ridgepole_0.7.4+20180826042918-1_amd64
RUN set -ex \
    && apt-get update && apt-get install -y --no-install-recommends ca-certificates wget build-essential libmysqlclient-dev && rm -rf /var/lib/apt/lists/* \
    && wget https://github.com/winebarrel/ridgepole/releases/download/v0.7.4/$RIDGEPOLE_VERSION.deb \
    && dpkg -i $RIDGEPOLE_VERSION.deb \
    && rm -rf $RIDGEPOLE_VERSION.deb \
    && /opt/ridgepole/embedded/bin/gem install mysql2 \
    && apt-get purge -y --auto-remove ca-certificates wget build-essential
