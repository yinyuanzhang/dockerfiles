FROM hyalx/java
MAINTAINER Indexyz <r18@iinde.xyz>

RUN set -ex \
    && apk add --no-cache --virtual .fetch-deps curl gnupg \
    && curl -fSL "https://www.python.org/ftp/python/2.7.11/Python-2.7.11.tar.xz" -o python.tar.xz \
    && curl -fSL "https://www.python.org/ftp/python/2.7.11/Python-2.7.11.tar.xz.asc" -o python.tar.xz.asc \
    && export GNUPGHOME="$(mktemp -d)" \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "C01E1CAD5EA2C4F0B8E3571504C367C218ADD4FF" \
    && gpg --batch --verify python.tar.xz.asc python.tar.xz \
    && rm -r "$GNUPGHOME" python.tar.xz.asc \
    && mkdir -p /usr/src \
    && tar -xJC /usr/src -f python.tar.xz \
    && mv "/usr/src/Python-2.7.11" /usr/src/python \
    && rm python.tar.xz \
    \
    && apk add --no-cache --virtual .build-deps  \
        bzip2-dev \
        gcc \
        libc-dev \
        linux-headers \
        make \
        ncurses-dev \
        openssl-dev \
        pax-utils \
        readline-dev \
        sqlite-dev \
        zlib-dev \
    && cd /usr/src/python \
    && ./configure --enable-shared --enable-unicode=ucs4 \
    && make -j$(getconf _NPROCESSORS_ONLN) \
    && make install \
    && curl -fSL 'https://bootstrap.pypa.io/get-pip.py' | python2 \
    && pip install --no-cache-dir --upgrade pip \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
            | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
            | sort -u \
            | xargs -r apk info --installed \
            | sort -u \
    )" \
    && apk add --virtual .python-rundeps $runDeps \
    && apk del .build-deps .fetch-deps \
    && rm -rf /usr/src/python

RUN apk add --update curl zip unzip

RUN mkdir /minecraft && \
    mkdir /minecraft/Runtime
VOLUME /minecraft/Runtime
ADD . /minecraft/Runtime

RUN curl 'http://ftp.iinde.xyz/Gamer/Minecraft/launcher.zip' -o '/minecraft/launcher.zip' && \
    unzip /minecraft/launcher.zip -d /minecraft && \
    chmod +x /minecraft/run

EXPOSE 25565:25565
CMD python2 /minecraft/run run
