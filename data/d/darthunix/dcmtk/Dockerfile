FROM alpine:latest
RUN apk update && \
    apk add --no-cache libstdc++ g++ make git && \
    git clone https://github.com/DCMTK/dcmtk.git && \
    cd dcmtk && \
    ./configure && \
    make all && \
    make install && \
    make distclean && \
    cd .. && \
    rm -r dcmtk && \
    apk del g++ make git && \
    rm /var/cache/apk/*
