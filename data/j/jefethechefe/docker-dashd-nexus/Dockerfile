# Build stage for BerkeleyDB
FROM alpine as berkeleydb

RUN apk --no-cache add autoconf
RUN apk --no-cache add automake
RUN apk --no-cache add build-base
RUN apk --no-cache add libressl

ENV BERKELEYDB_VERSION=db-4.8.30.NC
ENV BERKELEYDB_PREFIX=/opt/${BERKELEYDB_VERSION}

RUN wget https://download.oracle.com/berkeley-db/${BERKELEYDB_VERSION}.tar.gz
RUN tar -xzf *.tar.gz
RUN sed s/__atomic_compare_exchange/__atomic_compare_exchange_db/g -i ${BERKELEYDB_VERSION}/dbinc/atomic.h
RUN mkdir -p ${BERKELEYDB_PREFIX}

WORKDIR /${BERKELEYDB_VERSION}/build_unix

RUN ../dist/configure --enable-cxx --disable-shared --with-pic --prefix=${BERKELEYDB_PREFIX}
RUN make -j4
RUN make install
RUN rm -rf ${BERKELEYDB_PREFIX}/docs

FROM alpine as chiabls

RUN apk --no-cache add autoconf
RUN apk --no-cache add automake
RUN apk --no-cache add build-base
RUN apk --no-cache add libressl
RUN apk --no-cache add git
RUN apk --no-cache add cmake
RUN apk --no-cache add python3-dev

ENV CHIA_BLS_PREFIX=/opt/chiabls

RUN set -x \
  && git clone https://github.com/codablock/bls-signatures.git bls-signatures \
  && cd bls-signatures \
  && git fetch origin \
  && git checkout dash \
  && git submodule update --init --recursive \
  && mkdir build \
  && cd build \
  && cmake -DCMAKE_INSTALL_PREFIX:PATH=${CHIA_BLS_PREFIX} \
    -DCMAKE_PREFIX_PATH=${CHIA_BLS_PREFIX} \
    -DSTLIB=ON -DSHLIB=OFF -DSTBIN=ON \
    -DCMAKE_BUILD_TYPE=DEBUG \
    -DDEBUG=ON \
    -DOPSYS=LINUX -DCMAKE_SYSTEM_NAME=Linux -DWSIZE=64 \
    -DCMAKE_C_FLAGS_DEBUG="-g -O1" \
    .. \
  && cmake --build . --target install --config Release -- -j6

RUN ls -la ${CHIA_BLS_PREFIX}

# Build stage for Dash
FROM alpine as dash

COPY --from=berkeleydb /opt /opt
COPY --from=chiabls /opt /opt

RUN apk --no-cache add autoconf
RUN apk --no-cache add automake
RUN apk --no-cache add boost-dev
RUN apk --no-cache add build-base
RUN apk --no-cache add chrpath
RUN apk --no-cache add file
RUN apk --no-cache add gnupg
RUN apk --no-cache add libevent-dev
RUN apk --no-cache add libressl
RUN apk --no-cache add libressl-dev
RUN apk --no-cache add libsodium-dev
RUN apk --no-cache add libtool
RUN apk --no-cache add linux-headers
RUN apk --no-cache add protobuf-dev
RUN apk --no-cache add zeromq-dev
RUN apk --no-cache add gmp gmp-dev

ENV DASH_VERSION=0.13.0.0-rc5
ENV DASH_PREFIX=/opt/dash-${DASH_VERSION}
ENV DASH_SHASUM="2c2bd4b91ce68a9752e6d7e8fdf37662a0767a8837d81f9f47dcf14604cf38b6  v${DASH_VERSION}.tar.gz"

RUN wget https://github.com/dashpay/dash/archive/v${DASH_VERSION}.tar.gz
RUN echo "${DASH_SHASUM}" | sha256sum -c
RUN tar -xzf *.tar.gz
RUN ls -la
RUN ls -la /opt/chiabls/lib/.*

WORKDIR /dash-${DASH_VERSION}

RUN sed -i '/AC_PREREQ/a\AR_FLAGS=cr' src/univalue/configure.ac
RUN sed -i '/AX_PROG_CC_FOR_BUILD/a\AR_FLAGS=cr' src/secp256k1/configure.ac
RUN sed -i s:sys/fcntl.h:fcntl.h: src/compat.h
RUN ./autogen.sh
RUN ./configure CFLAGS="-g -O1" \
  LDFLAGS="-L/opt/db-4.8.30.NC/lib/ -L/opt/chiabls/lib/" \
  CPPFLAGS="-I/opt/db-4.8.30.NC/include/ -I/opt/chiabls/include/ -I/opt/chiabls/include/relic/" \
  CXXFLAGS="-g -O2 -Wall -Wextra -Wformat -Wvla -Wformat-security -Wno-unused-parameter" \
  --prefix=${DASH_PREFIX} \
  --mandir=/usr/share/man \
  --disable-tests \
  --disable-bench \
  --disable-ccache \
  --with-gui=no \
  --with-utils \
  --with-libs \
  --with-daemon
RUN make
RUN make install
RUN strip ${DASH_PREFIX}/bin/dash-cli
RUN strip ${DASH_PREFIX}/bin/dash-tx
RUN strip ${DASH_PREFIX}/bin/dashd
RUN strip ${DASH_PREFIX}/lib/libdashconsensus.a
RUN strip ${DASH_PREFIX}/lib/libdashconsensus.so.0.0.0

# Build stage for compiled artifacts
FROM alpine

LABEL maintainer.0="Jeff Hodges (@jhodges10)" \
  maintainer.1="Samuel Prado (@skateonrails)"

RUN adduser -S dash
RUN apk --no-cache add \
  boost \
  boost-program_options \
  curl \
  libevent \
  libressl \
  libzmq \
  su-exec

ENV DASH_DATA=/home/dash/.dashcore
ENV DASH_VERSION=0.13.0.0-rc5
ENV DASH_PREFIX=/opt/dash-${DASH_VERSION}
ENV PATH=${DASH_PREFIX}/bin:$PATH

COPY --from=dash /opt /opt
COPY docker-entrypoint.sh /entrypoint.sh

VOLUME ["/home/dash/.dashcore"]

EXPOSE 9998 9999 18332 19998 19999

ENTRYPOINT ["/entrypoint.sh"]

CMD ["dashd"]
