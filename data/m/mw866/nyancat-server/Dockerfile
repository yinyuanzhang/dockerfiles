FROM alpine:3.8
LABEL \
    maintainer="Chris Wang <docker@chriswang.tech>" \
    verion="1.0" \
    description="Nyancat Telnet Server"

RUN \
    apk upgrade --update && \
    apk add g++ make git autoconf automake && \
    cd /tmp && git clone https://github.com/klange/nyancat.git && \
    cd /tmp/nyancat && make && \
    cp ./src/nyancat /usr/local/bin/ && \
    cd / && rm -rf /tmp/nyancat && \
    cd /tmp && git clone http://offog.org/git/onenetd.git && \
    cd /tmp/onenetd && autoreconf -vfi && ./configure && make && \
    cp ./onenetd /usr/local/bin && \
    cd / && rm -rf /tmp/onenetd && \
    apk del --purge g++ make git autoconf automake && \
    :

EXPOSE 23

ENTRYPOINT ["onenetd", "-v1", "0", "23", "nyancat", "--telnet"]
