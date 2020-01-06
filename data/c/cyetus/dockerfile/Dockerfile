ARG ALPINE_VERSION=3.8

FROM alpine:$ALPINE_VERSION as pagespeed

# Check https://github.com/apache/incubator-pagespeed-mod/tags
ARG MOD_PAGESPEED_TAG=v1.13.35.2

# Check https://github.com/apache/incubator-pagespeed-ngx/tags
ARG NGX_PAGESPEED_TAG=v1.13.35.2-stable

RUN apk add --no-cache \
        apache2-dev \
        apr-dev \
        apr-util-dev \
        build-base \
        curl \
        gettext-dev \
        git \
        gperf \
        icu-dev \
        libjpeg-turbo-dev \
        libpng-dev \
        libressl-dev \
        pcre-dev \
        py-setuptools \
        zlib-dev \
    ;

WORKDIR /usr/src
RUN git clone -b ${MOD_PAGESPEED_TAG} \
              --recurse-submodules \
              --depth=1 \
              -c advice.detachedHead=false \
              -j`nproc` \
              https://github.com/apache/incubator-pagespeed-mod.git \
              modpagespeed \
    ;

WORKDIR /usr/src/modpagespeed

COPY patches/modpagespeed/*.patch ./

RUN for i in *.patch; do printf "\r\nApplying patch ${i%%.*}\r\n"; patch -p1 < $i || exit 1; done

WORKDIR /usr/src/modpagespeed/tools/gyp
RUN ./setup.py install

WORKDIR /usr/src/modpagespeed

RUN build/gyp_chromium --depth=. \
                       -D use_system_libs=1 \
    && \
    cd /usr/src/modpagespeed/pagespeed/automatic && \
    make psol BUILDTYPE=Release \
              CFLAGS+="-I/usr/include/apr-1" \
              CXXFLAGS+="-I/usr/include/apr-1 -DUCHAR_TYPE=uint16_t" \
              -j`nproc` \
    ;

RUN mkdir -p /usr/src/ngxpagespeed/psol/lib/Release/linux/x64 && \
    mkdir -p /usr/src/ngxpagespeed/psol/include/out/Release && \
    cp -R out/Release/obj /usr/src/ngxpagespeed/psol/include/out/Release/ && \
    cp -R pagespeed/automatic/pagespeed_automatic.a /usr/src/ngxpagespeed/psol/lib/Release/linux/x64/ && \
    cp -R net \
          pagespeed \
          testing \
          third_party \
          url \
          /usr/src/ngxpagespeed/psol/include/ \
    ;

WORKDIR /tmp
RUN git clone -b ${NGX_PAGESPEED_TAG} \
              --recurse-submodules \
              --shallow-submodules \
              --depth=1 \
              -c advice.detachedHead=false \
              -j`nproc` \
              https://github.com/apache/incubator-pagespeed-ngx.git \
              ngxpagespeed

FROM alpine:$ALPINE_VERSION

ENV UID=991 GID=991

ARG NGINX_VERSION=1.15.8

ARG OPENSSL_VER=3.0.0-dev

ARG NGINX_CT=1.3.2

ARG GPG_NGINX="B0F4 2533 73F8 F6F5 10D4  2178 520A 9993 A1C0 52F8"

ARG NGINX_MODULES=" \
  --with-http_ssl_module \
  --with-http_v2_module \
  --with-http_gzip_static_module \
  --with-http_stub_status_module \
  --with-http_slice_module \
  --with-stream \
  --with-stream_ssl_module \
  --with-ipv6 \
  --with-compat \
  --with-file-aio \
  --with-threads \
  --with-pcre-jit \
  --without-http_ssi_module \
  --without-http_scgi_module \
  --without-http_uwsgi_module \
  --without-http_geo_module \
  --without-http_autoindex_module \
  --without-http_split_clients_module \
  --without-http_empty_gif_module \
  --without-http_browser_module"

ARG NGINX_3RD_PARTY_MODULES=" \
  --add-dynamic-module=/tmp/ngxpagespeed \
  --add-module=/tmp/headers-more-nginx-module \
  --add-module=/tmp/ngx_brotli \
  --add-module=/tmp/nginx-ct"

WORKDIR /tmp

COPY --from=pagespeed /tmp/ngxpagespeed /tmp/ngxpagespeed
COPY --from=pagespeed /usr/src/ngxpagespeed /tmp/ngxpagespeed/


RUN __core=10 && echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \

# Update system
apk -U update && \

# Installing runtime dependencies
apk add --update --no-cache \
  openssl \
  pcre \
  su-exec \
  tzdata && \
#  zlib && \

# Installing build dependencies
apk add --update --no-cache -t build-dependencies \
  apr \
  apr-dev \
  apr-util \
  apr-util-dev \
  automake \
  autoconf \
  bind-tools \
  binutils \
  build-base \
  ca-certificates \
  cmake \
  curl \
  g++ \
  gcc \
  geoip-dev \
  git \
  go \
  gnupg \
  gperf \
  icu \
  icu-dev \
  icu-libs \
  jemalloc-dev \
  libgcc \
  libgd \
  linux-headers \
  libjpeg-turbo \
  libjpeg-turbo-dev \
  libpng-dev \
  libressl-dev \
  libstdc++ \
  libtool \
  libuuid \
  libxml2 \
  libxml2-dev \
  libxslt-dev \
  make \
  musl-dev \
  paxctl \
  pcre-dev \
  python \
  python-dev \
  tar \
  unzip && \
#   zlib-dev && \

# OpenSSL
git clone -b master https://github.com/openssl/openssl.git openssl && \
# wget -q https://www.openssl.org/source/openssl-${OPENSSL_VER}.tar.gz && tar zxvf openssl-${OPENSSL_VER}.tar.gz && mv openssl-${OPENSSL_VER} openssl && \
git clone --single-branch --depth=1 https://github.com/hakasenyang/openssl-patch.git && \
cd openssl && \
git reset --hard 4089b4340701e3c13e07169e67a7d14519c98658 && \
patch -p1 < ../openssl-patch/openssl-equal-${OPENSSL_VER}_ciphers.patch && \
patch -p1 < ../openssl-patch/openssl-${OPENSSL_VER}-chacha_draft.patch && \
# ./config enable-tls1_3 no-async no-shared enable-engine enable-afalgeng && \
# make -j$__core && make install && \
# ./config enable-tls1_3 no-async shared enable-engine enable-dso enable-afalgeng && \
# make -j$__core && make install && \
# cd .. && \
# mkdir -p .openssl/lib/ && cd .openssl && ln -s ../include && \
# cd .. && cp /usr/local/lib/libcrypto.a /usr/local/lib/libssl.a .openssl/lib && \

# nginx-ct
cd /tmp && wget -O nginx-ct.zip -c https://github.com/grahamedgecombe/nginx-ct/archive/v${NGINX_CT}.zip && \
unzip nginx-ct.zip && \
mv nginx-ct-${NGINX_CT} nginx-ct && \

# Brotli
# cd /tmp && git clone --single-branch --depth=1 https://github.com/bagder/libbrotli && \
# cd libbrotli && ./autogen.sh && ./configure && make -j$__core && make install && \
cd /tmp && git clone --single-branch --depth=1 https://github.com/eustas/ngx_brotli && \
cd ngx_brotli && git submodule update --init --recursive && \

# Headers More
cd /tmp && git clone --single-branch --depth=1 https://github.com/openresty/headers-more-nginx-module && \

# zlib for Cloudflare fork
cd /tmp && git clone --single-branch --depth=1 https://github.com/cloudflare/zlib.git && \
cd zlib && make -f Makefile.in distclean && \

# Nginx tarball checking
cd /tmp && NGINX_TARBALL="nginx-${NGINX_VERSION}.tar.gz" && \
wget -q https://nginx.org/download/${NGINX_TARBALL} && \
wget -q https://nginx.org/download/${NGINX_TARBALL}.asc && \
wget -q https://nginx.org/keys/mdounin.key && \
gpg --import mdounin.key && \
FINGERPRINT="$(LANG=C gpg --verify ${NGINX_TARBALL}.asc ${NGINX_TARBALL} 2>&1 \
  | sed -n "s#Primary key fingerprint: \(.*\)#\1#p")" && \
if [ -z "${FINGERPRINT}" ]; then echo "Warning! Invalid GPG signature!" && exit 1; fi && \
if [ "${FINGERPRINT}" != "${GPG_NGINX}" ]; then echo "Warning! Wrong GPG fingerprint!" && exit 1; fi && \
tar xzf ${NGINX_TARBALL} && cd nginx-${NGINX_VERSION} && \

# Nginx patch : dynamic TLS records
# wget -q https://raw.githubusercontent.com/cujanovic/nginx-dynamic-tls-records-patch/master/nginx__dynamic_tls_records_1.13.0%2B.patch -O dynamic_records.patch && \
# patch -p1 < dynamic_records.patch && \

# Nginx HPACK Patch && Remove Server Header Patch
# curl https://raw.githubusercontent.com/hakasenyang/openssl-patch/master/nginx_hpack_push.patch | patch -p1 && \
curl https://raw.githubusercontent.com/hakasenyang/openssl-patch/master/remove_nginx_server_header.patch | patch -p1 && \
curl https://raw.githubusercontent.com/hakasenyang/openssl-patch/master/nginx_strict-sni.patch | patch -p1 && \

# Nginx compilation
./configure \
  --prefix=/usr/local/nginx \
  --sbin-path=/usr/local/nginx/sbin/nginx \
  --modules-path=/usr/local/nginx/modules \
  --http-log-path=/var/log/nginx/access.log \
  --error-log-path=/var/log/nginx/error.log \
  --with-zlib=/tmp/zlib \
  --with-zlib-opt='-g -Ofast -fPIC -m64 -march=native -fstack-protector-strong -D_FORTIFY_SOURCE=2' \
  --with-openssl=/tmp/openssl \
  --with-openssl-opt='enable-tls1_3 no-ssl3 enable-ec_nistp_64_gcc_128 -fPIC -g -Ofast -m64 -march=native -fstack-protector-strong -D_FORTIFY_SOURCE=2 -ljemalloc -Wl,-flto' \
  --with-cc-opt="-g -Ofast -fPIC -march=native -fstack-protector-strong -D_FORTIFY_SOURCE=2 -m64 -O3 -fno-strict-aliasing -DTCP_FASTOPEN=23 -D_GLIBCXX_USE_CXX11_ABI=0 -ffast-math -flto -fuse-linker-plugin --param=ssp-buffer-size=4 -Wformat -Werror=format-security -Wno-deprecated-declarations -gsplit-dwarf" \
  --with-ld-opt="-lapr-1 -laprutil-1 -licudata -licuuc -lrt -lpng -ljemalloc -lturbojpeg -ljpeg -Wl,-Bsymbolic-functions -fPIC -Wl,-z,relro -Wl,-z,now" \
  ${NGINX_MODULES} \
  ${NGINX_3RD_PARTY_MODULES} && \
make -j$__core && make install && make clean && \
strip -s /usr/local/nginx/sbin/nginx \
  /usr/local/nginx/modules/*.so && \

# Clean
apk del --purge build-dependencies && \
rm -rf /tmp/* /var/cache/apk/* /root/.gnupg

COPY --from=pagespeed /usr/bin/envsubst /usr/local/bin
COPY rootfs /

WORKDIR /usr/local/nginx

# Generate ssl_dhparam / ssl_session_ticket_key
RUN chmod +x -R . && \
openssl dhparam -out ./conf/conf.d/dhparam.pem 2048 && \
openssl rand 48 > ./conf/conf.d/ticket-1.key && \
openssl rand 48 > ./conf/conf.d/ticket-2.key && \
apk del --purge openssl

# Mount
VOLUME /var/log/nginx /usr/local/nginx

# Expose port
EXPOSE 8000 4430

LABEL description="Nginx Built From Source" \
  openssl="OpenSSL-${OPENSSL_VER}" \
  nginx="Nginx-${NGINX_VERSION}" \
  maintainer="TangelSaki <tangel@tangel.me>"

CMD ["/usr/local/nginx/sbin/run.sh"]
