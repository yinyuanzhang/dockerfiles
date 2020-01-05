FROM jupyter/minimal-notebook

MAINTAINER Kozo Nishida <knishida@riken.jp>

USER root

RUN apt-get update && apt-get install -yq libtool pkg-config autoconf zlib1g-dev libssl-dev && \
    apt-get clean && cd ~ && \
    git clone --depth=1 https://github.com/zeromq/libzmq && \
    git clone --depth=1 https://github.com/zeromq/czmq && \
    cd libzmq && ./autogen.sh && ./configure && make && make install && \
    cd ../czmq && ./autogen.sh && ./configure && make && make install && \
    cd .. && rm -rf ./libzmq ./czmq && \
    wget https://cache.ruby-lang.org/pub/ruby/2.4/ruby-2.4.1.tar.gz && tar xf ruby-2.4.1.tar.gz && cd ruby-2.4.1 && \
    ./configure && make && make install && \
    rm -rf ./ruby-2.4* && \
    gem install cztop iruby rbplotly daru daru_plotly && \
    rm -rf /var/lib/apt/lists/* && ldconfig

# Switch back to jovyan to avoid accidental container runs as root
USER $NB_USER

RUN iruby register
