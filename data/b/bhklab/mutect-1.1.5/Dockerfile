FROM anapsix/alpine-java:7

ADD https://github.com/broadinstitute/mutect/releases/download/1.1.5/muTect-1.1.5-bin.zip /tmp/

RUN cd /tmp/ unzip muTect-1.1.5-bin.zip \
    && unzip muTect-1.1.5-bin.zip \
    && mv /tmp/muTect-1.1.5.jar /usr/bin/mutect.jar
