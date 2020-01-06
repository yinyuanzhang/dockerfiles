FROM maven:alpine
RUN apk --update add alpine-sdk libxml2-dev xz poppler-dev pango-dev m4 libtool perl autoconf automake coreutils \
    python-dev zlib-dev freetype-dev glib-dev cmake && \
    cd / && \
    git clone https://github.com/BWITS/fontforge.git && \
    cd fontforge && \
    ./bootstrap --force && \
    ./configure --without-iconv && \
    make && \
    make install && \
    cd / && git clone git://github.com/coolwanglu/pdf2htmlEX.git && \
    export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig && \
    cd pdf2htmlEX && \
    cmake . && make && sudo make install && \
    apk del alpine-sdk xz poppler-dev pango-dev m4 libtool perl autoconf automake coreutils python-dev zlib-dev freetype-dev glib-dev cmake && \
    apk add wget libpng python freetype glib libintl libltdl cairo poppler pango && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/* && \
    rm -rf /fontforge /libspiro /libuninameslist /pdf2htmlEX

ENTRYPOINT ["/usr/local/bin/mvn-entrypoint.sh"]
CMD ["mvn"]
