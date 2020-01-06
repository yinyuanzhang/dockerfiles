FROM debian:jessie
RUN apt-get update
RUN apt-get install -y gcc g++ \
    wget make automake \
    python python-dev
RUN cd /root; \
    wget https://nodejs.org/dist/v5.5.0/node-v5.5.0.tar.gz; \
    tar xzvf node-v5.5.0.tar.gz; \
    cd node-v5.5.0; \
    ./configure --prefix=/usr; \
    make; make install; \ 
    apt-get autoclean; \
    cd ..; \
    rm node-v5.5.0.tar.gz;\
    rm -r node-v5.5.0

