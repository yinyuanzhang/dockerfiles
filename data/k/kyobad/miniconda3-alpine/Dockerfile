FROM frolvlad/alpine-glibc:latest

MAINTAINER K.Kato

ENV PATH=/opt/conda/bin:$PATH \
    MINICONDA=Miniconda3-latest-Linux-x86_64.sh

RUN apk add --no-cache --virtual=build-deps --update-cache \
    wget bash \
    && wget -q --no-check-certificate https://repo.continuum.io/miniconda/$MINICONDA \
    && /bin/bash $MINICONDA -b -p /opt/conda \
    && rm -rf /root/.continuum /opt/conda/pkgs/* \
    && rm $MINICONDA \
    && apk del build-deps 
    
CMD ["/bin/sh"]



