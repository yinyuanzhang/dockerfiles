FROM cooptilleuls/varnish:6.2.0-alpine
LABEL maintainer="Aplyca" description="Varnish image with VMOD dynamic"

# Define env vars for VMOD build
ENV PKG_CONFIG_PATH /usr/local/lib/pkgconfig
ENV ACLOCAL_PATH /usr/local/share/aclocal

# Install build dependencies; download, build and install the VMOD;
# then remove build dependencies to keep the docker layer as small as possible.
RUN set -eux; \
    apk add --quiet --progress --update --no-cache --virtual .vmod-build-deps autoconf automake libexecinfo-dev libtool make pcre-dev pkgconf py-docutils python3 && \
    wget "https://github.com/nigoroll/libvmod-dynamic/archive/6.2.zip" -O /tmp/libvmod-dynamic.zip && \
    unzip -d /tmp /tmp/libvmod-dynamic.zip && \
    cd "/tmp/libvmod-dynamic-6.2" && \
    chmod +x ./autogen.sh && \
    ./autogen.sh && \
    ./configure --prefix=/usr/local && \
    make -j "$(nproc)" && \
    make install && \
    cd / && \
    rm -rf /tmp/libvmod-dynamic* && \
    apk del --purge .vmod-build-deps autoconf automake make libexecinfo-dev pcre-dev

# Run varnish and also print logs on stdout
CMD ["/bin/sh", "-o", "pipefail", "-c", "varnishd -F -f /usr/local/share/varnish/vcl/default.vcl -s malloc,${VARNISH_MEMORY:-80M} ${VARNISH_PARAMS} | varnishncsa -F '%h %l %u %t \"%r\" %s %b \"%{Referer}i\" \"%{User-agent}i\" \"%{Varnish:handling}x\"'"]