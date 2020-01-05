#PhantomJS

FROM ubuntu:latest
MAINTAINER Bradley Cicenas <bradley.cicenas@gmail.com>

ENV PHANTOMJS_VERSION 2.0

#prereqs
RUN apt-get -yqq update && \
    apt-get install -yq git \
                        build-essential \
                        g++ \
                        flex \
                        bison \
                        gperf \
                        ruby \
                        perl \
                        python \
                        libsqlite3-dev \
                        libfontconfig1-dev \
                        libicu-dev \
                        libfreetype6 \
                        libssl-dev \
                        libpng-dev \
                        libjpeg-dev && \
    apt-get clean

#build
RUN cd /tmp && \
    git clone git://github.com/ariya/phantomjs.git && \
    cd phantomjs/ && \
    git checkout $PHANTOMJS_VERSION && \
    echo y | ./build.sh && \
    mv -v bin/phantomjs /usr/bin/ && \
    #cleanup
    rm -rf /tmp/*

ENTRYPOINT [ "phantomjs" ]
