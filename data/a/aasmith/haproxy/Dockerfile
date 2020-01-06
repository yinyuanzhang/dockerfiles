ARG OS=debian:buster-slim

ARG OPENSSL_VERSION=1.1.1c
ARG OPENSSL_SHA256=f6fb3079ad15076154eda9413fed42877d668e7069d9b87396d0804fdb3f4c90

ARG PCRE2_VERSION=10.33
ARG PCRE2_SHA256=e2e2899a97489fc6ad1b0cc3da7952c7cca991b4a0f7db6649b75d9721025d31

ARG LIBSLZ_VERSION=1.1.0
# No md5 for libslz yet -- the tarball is dynamically
# generated and it differs every time.

ARG HAPROXY_MAJOR=2.0
ARG HAPROXY_VERSION=2.0.5
ARG HAPROXY_MD5=497c716adf4b056484601a887f34d152


### Runtime -- the base image for all others

FROM $OS as runtime

RUN apt-get update && \
    apt-get install --no-install-recommends -y curl ca-certificates


### Builder -- adds common utils needed for all build images

FROM runtime as builder

RUN apt-get update && \
    apt-get install --no-install-recommends -y gcc make file libc6-dev perl libtext-template-perl


### OpenSSL

FROM builder as ssl

ARG OPENSSL_VERSION
ARG OPENSSL_SHA256

RUN curl -OJ https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz && \
    echo ${OPENSSL_SHA256} openssl-${OPENSSL_VERSION}.tar.gz | sha256sum -c && \
    tar zxvf openssl-${OPENSSL_VERSION}.tar.gz && \
    cd openssl-${OPENSSL_VERSION} && \
    ./config no-shared --prefix=/tmp/openssl && \
    make && \
    make TESTS='-40' test && \
    make install_sw


### PCRE2

FROM builder as pcre2

ARG PCRE2_VERSION
ARG PCRE2_SHA256

RUN curl -OJ "https://ftp.pcre.org/pub/pcre/pcre2-${PCRE2_VERSION}.tar.gz" && \
    echo ${PCRE2_SHA256} pcre2-${PCRE2_VERSION}.tar.gz | sha256sum -c && \
    tar zxvf pcre2-${PCRE2_VERSION}.tar.gz && \
    cd pcre2-${PCRE2_VERSION} && \
    LDFLAGS="-fPIE -pie -Wl,-z,relro -Wl,-z,now" \
    CFLAGS="-pthread -g -O2 -fPIE -fstack-protector-strong -Wformat -Werror=format-security -Wall -fvisibility=hidden" \
    ./configure --prefix=/tmp/pcre2 --disable-shared --enable-utf8 --enable-jit --enable-unicode-properties --disable-cpp && \
    make check && \
    make install


### libslz

FROM builder as slz

ARG LIBSLZ_VERSION

RUN curl -OJ "http://git.1wt.eu/web?p=libslz.git;a=snapshot;h=v${LIBSLZ_VERSION};sf=tgz" && \
    tar zxvf libslz-v${LIBSLZ_VERSION}.tar.gz && \
    make -C libslz static


### HAProxy

FROM builder as haproxy

COPY --from=ssl   /tmp/openssl /tmp/openssl
COPY --from=pcre2 /tmp/pcre2   /tmp/pcre2
COPY --from=slz   /libslz      /libslz

ARG HAPROXY_MAJOR
ARG HAPROXY_VERSION
ARG HAPROXY_MD5

RUN curl -OJL "http://www.haproxy.org/download/${HAPROXY_MAJOR}/src/haproxy-${HAPROXY_VERSION}.tar.gz" && \
    echo "${HAPROXY_MD5} haproxy-${HAPROXY_VERSION}.tar.gz" | md5sum -c && \
    tar zxvf haproxy-${HAPROXY_VERSION}.tar.gz && \
    make -C haproxy-${HAPROXY_VERSION} \
      TARGET=linux-glibc \
      USE_SLZ=1 SLZ_INC=../libslz/src SLZ_LIB=../libslz \
      USE_STATIC_PCRE2=1 USE_PCRE2_JIT=1 PCRE2DIR=/tmp/pcre2 \
      USE_OPENSSL=1 SSL_INC=/tmp/openssl/include SSL_LIB=/tmp/openssl/lib \
      EXTRA_OBJS="contrib/prometheus-exporter/service-prometheus.o" \
      DESTDIR=/tmp/haproxy PREFIX= \
      all \
      install-bin && \
    mkdir -p /tmp/haproxy/etc/haproxy && \
    cp -R haproxy-${HAPROXY_VERSION}/examples/errorfiles /tmp/haproxy/etc/haproxy/errors


### HAProxy runtime image

FROM runtime

COPY --from=haproxy /tmp/haproxy /usr/local/

RUN rm -rf /var/lib/apt/lists/*

CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]
