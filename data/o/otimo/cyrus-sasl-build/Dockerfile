FROM otimo/buildbase AS sasl-build
LABEL Name="cyrus-sasl-build" Intermediate="yes" \
    Maintainer="Otimo Data AB"

ARG name=cyrus-sasl
ARG version=2.1.26
ARG checksum=8fbc5136512b59bb793657f36fadda6359cae3b08f01fd16b3d406f1345b7bc3
ARG urlbase=https://www.cyrusimap.org/releases

WORKDIR /build

COPY patch/*.patch ./

RUN echo "${checksum}  ${name}-${version}.tar.gz" > CHECKSUM \
        && sha256sum -c CHECKSUM \
        || [ $? == 1 ] && wget ${urlbase}/${name}-${version}.tar.gz \
        && sha256sum -c CHECKSUM \
\
    && apk --no-cache add openldap-dev heimdal-dev \
    && tar -xzf ${name}-${version}.tar.gz \
    && cd ${name}-${version} \
    && patch -p1 -i ../CVE-2013-4122.patch \
    && patch -p1 -i ../cyrus-sasl-2.1.25-avoid_pic_overwrite.patch \
    && patch -p1 -i ../cyrus-sasl-2.1.26-size_t.patch \
    && sed 's/AM_CONFIG_HEADER/AC_CONFIG_HEADERS/' -i configure.in || true \
    && rm -rf config/config.guess config/config.sub config/ltconfig \
        config/ltmain.sh config/libtool.m4 autom4te.cache \
    && libtoolize -c \
    && aclocal -I config -I cmulocal \
    && automake -a -c \
    && autoheader \
    && autoconf \
    && ./configure \
        --prefix=/usr \
        --sysconfdir=/etc/cyrus \
        --enable-ldapdb \
        --enable-sql \
        --enable-plain \
        --enable-digest \
        --enable-ntlm \
        --enable-gssapi \
        --with-ldap \
        --with-devrandom=/dev/urandom \
        --with-saslauthd=/run/saslauthd \
    && make \
    && make install DESTDIR=/build/install \
    && strip /build/install/usr/sbin/* || true \
    && strip /build/install/usr/lib/*.so.* || true \
    && strip /build/install/usr/lib/sasl2/*.so.* || true \
    && cp -a /build/install/* / \
    && rm -rf /build/* 
