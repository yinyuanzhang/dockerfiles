FROM lsiobase/alpine
COPY root/ /
RUN apk add --no-cache curl nano git python2 py-gevent py-psutil \
    && cd /tmp/ \
    && curl -L https://sybdata.de/files/public-docs/acestream_3.1.31_webUI_x86.tar.gz -o acestream_x86.tar.gz \
    && tar xzfv acestream_x86.tar.gz \
    && rm -rf acestream_x86.tar.gz 
RUN mv /tmp/androidfs/ /acestream.engine/
RUN find /acestream.engine/androidfs/system -type d -exec chmod 755 {} \; \
    && find /acestream.engine/androidfs/system -type f -exec chmod 644 {} \; \
    && chmod 755 /acestream.engine/androidfs/system/bin/* /acestream.engine/androidfs/acestream.engine/python/bin/python \
    && chmod +x /acestream.engine/acestream.start \
    && chmod +x /acestream.engine/acestream.stop \
    && rm -rf /tmp/* \
    && cd / && git clone https://github.com/pepsik-kiev/HTTPAceProxy.git \
    && mkdir -p /mnt/films/
EXPOSE 6878 62062 8621 8000

