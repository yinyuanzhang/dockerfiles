FROM plexinc/pms-docker:public
MAINTAINER bulzipke <bulzipke@naver.com>

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y fuse unzip rename sqlite && \
    sed -i "2ibash /setup.sh" /plex-common.sh && \
    sed -i "3isqlite3 -header -line \"/config/Library/Application Support/Plex Media Server/Plug-in Support/Databases/com.plexapp.plugins.library.db\" \"PRAGMA default_cache_size = 1000000\"" /etc/services.d/plex/run

COPY scripts/* /

EXPOSE 32400/tcp
