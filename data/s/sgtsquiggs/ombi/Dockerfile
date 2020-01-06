FROM sgtsquiggs/alpine.mono:3.4
MAINTAINER sgtsquiggs

# environment settings
ENV XDG_DATA_HOME="/config"
ENV XDG_CONFIG_HOME="/config"

RUN \
# install packages
    apk add --no-cache \
        sqlite-libs &&\
    apk add --no-cache \
        --virtual=build-dependencies \
        curl \
        unzip &&\

# install ombi
    latest_tag=$(curl -sX GET "https://api.github.com/repos/tidusjar/Ombi/releases/latest" \
        | awk '/tag_name/{print $4;exit}' FS='[""]') &&\
    curl -o \
        /tmp/ombi-src.zip -L \
        https://github.com/tidusjar/Ombi/releases/download/$latest_tag/Ombi.zip &&\
    unzip \
        -q /tmp/ombi-src.zip \
        -d /tmp &&\
    mv /tmp/Release /app/ombi &&\

# cleanup
    apk del build-dependencies &&\
    rm -rf \
        /tmp/*

# add local files
COPY root/ /

# ports and volumes
VOLUME /config
EXPOSE 3579
