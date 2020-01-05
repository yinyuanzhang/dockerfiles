FROM alpine:3.10

LABEL maintainer="PRESSMAN <wp10@pressman.ne.jp>"

ENV NGINX_VERSION 1.17.5
ENV NJS_VERSION   0.3.6
ENV PKG_RELEASE   1
ARG NGX_CACHE_PURGE_VERSION=2.3

RUN set -x \
# create nginx user/group first, to be consistent throughout docker variants
    && addgroup -g 101 -S nginx \
    && adduser -S -D -H -u 101 -h /var/cache/nginx -s /sbin/nologin -G nginx -g nginx nginx \
    && apkArch="$(cat /etc/apk/arch)" \
    && nginxPackages=" \
        nginx=${NGINX_VERSION}-r${PKG_RELEASE} \
        nginx-module-xslt=${NGINX_VERSION}-r${PKG_RELEASE} \
        nginx-module-geoip=${NGINX_VERSION}-r${PKG_RELEASE} \
        nginx-module-image-filter=${NGINX_VERSION}-r${PKG_RELEASE} \
        nginx-module-njs=${NGINX_VERSION}.${NJS_VERSION}-r${PKG_RELEASE} \
    " \
# brotli, ngx_cache_purge
    && apk add --no-cache --virtual .build-add-modules-deps \
        curl \
        autoconf \
        automake \
        cmake \
        git \
        g++ \
        libtool \ 
    && mkdir -p /usr/src \
    && git clone --recursive https://github.com/google/ngx_brotli.git /usr/src/ngx_brotli \
	&& curl -fSL https://github.com/FRiCKLE/ngx_cache_purge/archive/${NGX_CACHE_PURGE_VERSION}.tar.gz -o ngx_cache_purge.tar.gz \
    && tar -zxC /usr/src -f ngx_cache_purge.tar.gz \
    && rm ngx_cache_purge.tar.gz \
    && case "$apkArch" in \
        *) \
            set -x \
            && tempDir="$(mktemp -d)" \
            && chown nobody:nobody $tempDir \
            && apk add --no-cache --virtual .build-deps \
                gcc \
                libc-dev \
                make \
                openssl-dev \
                pcre-dev \
                zlib-dev \
                linux-headers \
                libxslt-dev \
                gd-dev \
                geoip-dev \
                perl-dev \
                libedit-dev \
                mercurial \
                bash \
                alpine-sdk \
                findutils \
            && su - nobody -s /bin/sh -c " \
                export HOME=${tempDir} \
                && cd ${tempDir} \
                && hg clone https://hg.nginx.org/pkg-oss \
                && cd pkg-oss \
                && hg up ${NGINX_VERSION}-${PKG_RELEASE} \
                && cd alpine \
                && sed -i -e 's/BASE_CONFIGURE_ARGS=/BASE_CONFIGURE_ARGS=\\	--add-module=\/usr\/src\/ngx_brotli \\	--add-module=\/usr\/src\/ngx_cache_purge-${NGX_CACHE_PURGE_VERSION} /' Makefile \
                && make all \
                && apk index -o ${tempDir}/packages/alpine/${apkArch}/APKINDEX.tar.gz ${tempDir}/packages/alpine/${apkArch}/*.apk \
                && abuild-sign -k ${tempDir}/.abuild/abuild-key.rsa ${tempDir}/packages/alpine/${apkArch}/APKINDEX.tar.gz \
                " \
            && echo "${tempDir}/packages/alpine/" >> /etc/apk/repositories \
            && cp ${tempDir}/.abuild/abuild-key.rsa.pub /etc/apk/keys/ \
            && apk del .build-deps \
            ;; \
    esac \
    && apk add --no-cache --update $nginxPackages \
# if we have leftovers from building, let's purge them (including extra, unnecessary build deps)
    && if [ -n "$tempDir" ]; then rm -rf "$tempDir"; fi \
    && if [ -n "/etc/apk/keys/abuild-key.rsa.pub" ]; then rm -f /etc/apk/keys/abuild-key.rsa.pub; fi \
    && if [ -n "/etc/apk/keys/nginx_signing.rsa.pub" ]; then rm -f /etc/apk/keys/nginx_signing.rsa.pub; fi \
# remove the last line with the packages repos in the repositories file
    && sed -i '$ d' /etc/apk/repositories \
	&& rm -rf /usr/src/ngx_brotli \
	&& rm -rf /usr/src/ngx_cache_purge-${NGX_CACHE_PURGE_VERSION} \
# Bring in gettext so we can get `envsubst`, then throw
# the rest away. To do this, we need to install `gettext`
# then move `envsubst` out of the way so `gettext` can
# be deleted completely, then move `envsubst` back.
    && apk add --no-cache --virtual .gettext gettext \
    && mv /usr/bin/envsubst /tmp/ \
    \
    && runDeps="$( \
        scanelf --needed --nobanner /tmp/envsubst \
            | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
            | sort -u \
            | xargs -r apk info --installed \
            | sort -u \
    )" \
    && apk add --no-cache $runDeps \
    && apk del .gettext \
    && mv /tmp/envsubst /usr/local/bin/ \
# Bring in tzdata so users could set the timezones through the environment
# variables
    && apk add --no-cache tzdata \
# forward request and error logs to docker log collector
    && ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]
