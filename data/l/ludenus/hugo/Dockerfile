FROM alpine:3.8

ARG VERSION=0.40.1

ARG TAR_GZ=hugo_${VERSION}_Linux-64bit.tar.gz

ARG TAR_GZ_URL=https://github.com/gohugoio/hugo/releases/download/v${VERSION}/${TAR_GZ}

RUN cd /usr/local/bin &&\
    wget ${TAR_GZ_URL} &&\
    tar -xvf ${TAR_GZ} &&\
    rm -f ${TAR_GZ} LICENSE README.md
