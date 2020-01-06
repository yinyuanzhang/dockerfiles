FROM debian:8
MAINTAINER Tim Court <tctimmeh@gmail.com>

RUN set -xe \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        bzip2 \
        ca-certificates \
        curl \
        libasound2 \
        libdbus-glib-1-2 \
        libgtk-3.0 \
        libgtk2.0-0 \
        libxt6

ARG version
ENV VERSION=${version:-47.0.1}

RUN set -xe \
    && curl -SL https://ftp.mozilla.org/pub/firefox/releases/${VERSION}/linux-x86_64/en-US/firefox-${VERSION}.tar.bz2 -o firefox.tar.bz2

RUN set -xe \
    && tar -xjf firefox.tar.bz2 \
    && rm -rf firefox.tar.bz2 \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get autoremove -y \
        bzip2 \
        curl

COPY profiles.ini /root/.mozilla/firefox/
COPY user.js /root/.mozilla/firefox/default/

CMD ["/firefox/firefox"]

