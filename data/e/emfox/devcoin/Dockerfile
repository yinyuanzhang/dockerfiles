#
# Dockerfile for Devcoind
#
# version: 0.1.0
#

FROM debian:7 as builder
MAINTAINER Fernando Paredes Garcia <fernando@develcuy.com>

# Update packages and install package dependencies
RUN apt-get update && apt-get install -y --force-yes build-essential libboost-all-dev git wget \
    && rm -rf /var/lib/apt/lists/*;

ENV SRC /usr/local/src
ENV BDBVER db-4.8.30.NC
WORKDIR $SRC
# Download and Compile Berkeley DB 4.8
RUN set -ex; \
        mkdir -p $SRC/db4_dest; \
        wget --quiet http://download.oracle.com/berkeley-db/$BDBVER.tar.gz; \
        echo "12edc0df75bf9abd7f82f821795bcee50f42cb2e5f76a6a281b85732798364ef  $BDBVER.tar.gz" | sha256sum -c - || exit 1; \
        tar -xzf $BDBVER.tar.gz; \
        cd $BDBVER/build_unix/; \
        sed s/__atomic_compare_exchange/__atomic_compare_exchange_db/g -i ../dbinc/atomic.h; \
        ../dist/configure --enable-cxx --disable-shared --with-pic --prefix=$SRC/db4_dest; \
        make install; \
        cd $SRC; \
        rm -rf $BDBVER $BDBVER.tar.gz db4_dest/docs

# Download Devcoind source
RUN git clone --depth=1 https://github.com/devcoin/core.git $SRC/devcoin
# Compile & Install Devcoind
RUN set -ex; \
        cd $SRC/devcoin/src; \
        make -j4 -f makefile.unix USE_UPNP=- BDB_LIB_PATH=$SRC/db4_dest/lib/ BDB_INCLUDE_PATH=$SRC/db4_dest/include/; \
        strip devcoind; \
        mv devcoind /usr/local/bin/; \
        make -f makefile.unix clean

FROM debian:7

COPY --from=builder /usr/local/bin/devcoind /usr/local/bin/devcoind
# Update packages and install package dependencies
RUN apt-get update && apt-get install -y --force-yes \
        libboost-system1.49.0 libboost-filesystem1.49.0 libboost-program-options1.49.0 libboost-thread1.49.0 \
        openssl supervisor procps \
    && rm -rf /var/lib/apt/lists/*;

# Configure Devcoind
RUN useradd devcoin
RUN mkdir -p /home/devcoin/.devcoin
RUN echo '#Noob config file for devcoind, should be enough!\n\
server=1\n\
daemon=1\n\
rpcuser=devcoind\n\
rpcpassword=devcoin\n\
# OpenSSL settings used when rpcssl=1\n\
rpcsslciphers=TLSv1+HIGH:!SSLv2:!aNULL:!eNULL:!AH:!3DES:@STRENGTH\n\
rpcsslcertificatechainfile=server.cert\n\
rpcsslprivatekeyfile=server.pem\n\
rpcport=52332\n\
rpcallowip=*\n\
# Set gen=1 to attempt to generate coins\n\
gen=0\n\
# Allow direct connections for the 'pay via IP address' feature.\n\
allowreceivebyip=1\n\
# Enable transaction index\n\
txindex=1\n\
'\
> /home/devcoin/.devcoin/devcoin.conf
RUN chown devcoin: -R /home/devcoin

# Configure supervisor
RUN echo '[supervisord]\n\
nodaemon=true\n\
\n\
[program:devcoind]\n\
command=/usr/bin/pidproxy /var/run/devcoind.pid /bin/su devcoin -c "/usr/local/bin/devcoind"\n\
redirect_stderr=true\n'\
>> /etc/supervisor/conf.d/supervisord.conf

EXPOSE 52332

# Start supervisor
CMD ["/usr/bin/supervisord"]
