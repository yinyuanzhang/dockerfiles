FROM frolvlad/alpine-glibc

RUN set -ex && \
    export MECAB_VERSION=0.996 \
           IPADIC_VERSION=2.7.0-20070801 \
           MECAB_URL="https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE" \
           IPADIC_URL="https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM" && \
    apk add --no-cache libstdc++ && \
    apk add --no-cache --virtual=build-dependencies build-base openssl curl git bash file sudo openssh && \
    curl -SL -o mecab-$MECAB_VERSION.tar.gz $MECAB_URL && \
    tar zxf mecab-$MECAB_VERSION.tar.gz && \
    cd mecab-$MECAB_VERSION && \
    ./configure --enable-utf8-only --with-charset=utf8 && \
    make install && \
    cd / && \
    curl -SL -o mecab-ipadic-$IPADIC_VERSION.tar.gz $IPADIC_URL && \
    tar zxf mecab-ipadic-$IPADIC_VERSION.tar.gz && \
    cd mecab-ipadic-$IPADIC_VERSION && \
    ./configure --with-charset=utf8 && \
    make install && \
    cd / && \
    git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git && \
    mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -y && \
    apk del build-dependencies && \
    rm -rf /mecab*
CMD ["mecab", "-d", "/usr/local/lib/mecab/dic/mecab-ipadic-neologd"]
