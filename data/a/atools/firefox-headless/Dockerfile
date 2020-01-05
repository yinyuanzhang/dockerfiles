ARG JDK_MAVEN_NODE=mvn3-jdk8-node12

FROM atools/jdk-maven-node:${JDK_MAVEN_NODE}
USER root


# install firefox
ARG FIREFOX_VERSION=latest
RUN FIREFOX_DOWNLOAD_URL=$(if [ "latest" = "latest" ]; then echo "https://download.mozilla.org/?product=firefox-$FIREFOX_VERSION-ssl&os=linux64&lang=en-US"; else echo "https://download-installer.cdn.mozilla.net/pub/firefox/releases/$FIREFOX_VERSION/linux-x86_64/en-US/firefox-$FIREFOX_VERSION.tar.bz2"; fi) && \
    apt-get -qqy update && \
    apt-get -qqy install libxt-dev libgtk-3-bin libdbus-glib-1-2 && \
    wget --no-verbose -O /tmp/firefox.tar.bz2 $FIREFOX_DOWNLOAD_URL && \
    tar -C /opt -xjf /tmp/firefox.tar.bz2 && \
    rm /tmp/firefox.tar.bz2 && \
    mv /opt/firefox /opt/firefox-$FIREFOX_VERSION && \
    ln -fs /opt/firefox-$FIREFOX_VERSION/firefox /usr/bin/firefox && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/*
