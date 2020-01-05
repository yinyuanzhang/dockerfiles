# a fork of https://hub.docker.com/r/tchabaud/amule
FROM alpine:3.9 as builder

ENV AMULE_VERSION 2.3.2
ENV UPNP_VERSION 1.6.22
ENV CRYPTOPP_VERSION CRYPTOPP_5_6_5

RUN apk --update add gd geoip libpng libwebp pwgen sudo wxgtk2.8 zlib bash && \
    apk --update add --virtual build-dependencies alpine-sdk automake \
                               autoconf bison g++ gcc gd-dev geoip-dev \
                               gettext gettext-dev git libpng-dev libwebp-dev \
                               libtool libsm-dev make musl-dev wget \
                               wxgtk2.8-dev zlib-dev

# Build libupnp
RUN mkdir -p /opt \
    && cd /opt \
    && wget "http://downloads.sourceforge.net/sourceforge/pupnp/libupnp-${UPNP_VERSION}.tar.bz2" \
    && tar xvfj libupnp*.tar.bz2 \
    && cd libupnp* \
    && ./configure --prefix=/usr \
    && make \
    && make install

# Build crypto++
RUN mkdir -p /opt && cd /opt \
    && git clone --depth 1 --branch ${CRYPTOPP_VERSION} --single-branch "https://github.com/weidai11/cryptopp" /opt/cryptopp \
    && cd /opt/cryptopp \
    && sed -i -e 's/^CXXFLAGS/#CXXFLAGS/' GNUmakefile \
    && export CXXFLAGS="${CXXFLAGS} -DNDEBUG -fPIC" \
    && make -f GNUmakefile \
    && make libcryptopp.so \
    && install -Dm644 libcryptopp.so* /usr/lib/ \
    && mkdir -p /usr/include/cryptopp \
    && install -m644 *.h /usr/include/cryptopp/

# Build amule from source
RUN mkdir -p /opt/amule \
    && git clone --depth 1 --branch ${AMULE_VERSION} --single-branch "https://github.com/amule-project/amule" /opt/amule \
    && cd /opt/amule \
    && ./autogen.sh \
    && ./configure \
        --disable-gui \
        --disable-amule-gui \
        --disable-wxcas \
        --disable-alc \
        --disable-plasmamule \
        --disable-kde-in-home \
        --prefix=/usr \
        --mandir=/usr/share/man \
        --enable-unicode \
        --without-subdirs \
        --without-expat \
        --enable-amule-daemon \
        --enable-amulecmd \
        --enable-webserver \
        --enable-cas \
        --enable-alcc \
        --enable-fileview \
        --enable-geoip \
        --enable-mmap \
        --enable-optimize \
        --enable-upnp \
        --disable-debug \
    && make \
    && make install

# Install a nicer web ui
RUN cd /usr/share/amule/webserver \
    && git clone --depth 1 https://github.com/MatteoRagni/AmuleWebUI-Reloaded \
    && rm -rf AmuleWebUI-Reloaded/.git AmuleWebUI-Reloaded/doc-images


FROM alpine:3.9
MAINTAINER hh
RUN apk --update add bash pwgen sudo
#RUN apk --update add gd
#RUN apk --update add zlib 

#copy binaries
COPY --from=builder /usr/bin/amule /usr/bin/amule
COPY --from=builder /usr/bin/amulecmd /usr/bin/amulecmd
COPY --from=builder /usr/bin/amuled /usr/bin/amuled
COPY --from=builder /usr/bin/amuleweb /usr/bin/amuleweb

#copy libs
COPY --from=builder /usr/lib/libgcc_s.so /usr/lib/libgcc_s.so 
COPY --from=builder /usr/lib/libgcc_s.so.1 /usr/lib/libgcc_s.so.1
COPY --from=builder /usr/lib/libstdc++.so /usr/lib/libstdc++.so
COPY --from=builder /usr/lib/libstdc++.so.6 /usr/lib/libstdc++.so.6
COPY --from=builder /usr/lib/libstdc++.so.6.0.25 /usr/lib/libstdc++.so.6.0.25
COPY --from=builder /usr/lib/libthreadutil.so.6 /usr/lib/libthreadutil.so.6
COPY --from=builder /usr/lib/libthreadutil.so.6.0.4 /usr/lib/libthreadutil.so.6.0.4
COPY --from=builder /usr/lib/libcryptopp.so.5.6 /usr/lib/libcryptopp.so.5.6
COPY --from=builder /usr/lib/libupnp.so.6 /usr/lib/libupnp.so.6
COPY --from=builder /usr/lib/libupnp.so.6.3.6 /usr/lib/libupnp.so.6.3.6
COPY --from=builder /usr/lib/libixml.so.2 /usr/lib/libixml.so.2
COPY --from=builder /usr/lib/libixml.so.2.0.8 /usr/lib/libixml.so.2.0.8
COPY --from=builder /usr/lib/libwx_baseu_net-2.8.so.0 /usr/lib/libwx_baseu_net-2.8.so.0
COPY --from=builder /usr/lib/libwx_baseu_net-2.8.so.0.8.0 /usr/lib/libwx_baseu_net-2.8.so.0.8.0
COPY --from=builder /usr/lib/libwx_baseu-2.8.so.0 /usr/lib/libwx_baseu-2.8.so.0
COPY --from=builder /usr/lib/libwx_baseu-2.8.so.0.8.0 /usr/lib/libwx_baseu-2.8.so.0.8.0
COPY --from=builder /usr/lib/libpng16.so.16 /usr/lib/libpng16.so.16 
COPY --from=builder /usr/lib/libintl.so.8 /usr/lib/libintl.so.8
COPY --from=builder /usr/share/amule /usr/share/amule

# Add startup script
ADD amule.sh /home/amule/amule.sh
RUN chmod a+x /home/amule/amule.sh


EXPOSE 4711/tcp 4712/tcp 4672/udp 4665/udp 4662/tcp 4661/tcp

ENTRYPOINT ["/home/amule/amule.sh"]
