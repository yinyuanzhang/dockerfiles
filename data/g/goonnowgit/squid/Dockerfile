# docker run -d \
#  -p 3128:3128 \
#  -v $HOME/squid/acls:/etc/squid/acls \
#  -v $HOME/squid/squidssl.conf:/etc/squid/squid.conf \
#  -v $HOME/squid/cache:/var/spool/squid \
#  -v $HOME/squid/ssl_cert:/etc/squid/ssl_cert \
#   goonnowgit/squid

FROM debian:buster-slim
LABEL maintainer "goonnowgit <goonnowgittt@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive \
  SQUID_CACHE_DIR=/var/spool/squid \
  SQUID_LOG_DIR=/var/log/squid \
  SQUID_USER=proxy \
  SQUID_FINGERPRINT=CD6DBF8EF3B17D3E \
  SQUID_VERSION=4.9 \
  SQUID_ERROR_LANG=English \
  SQUID_PREFIX=/usr/local/squid

RUN apt update && apt install -y \
  libnetfilter-conntrack3 \
  libxml2 \
  libecap3 \
  libexpat1 \
  libssl1.1 \
  libgssapi-krb5-2 \
  libltdl7 \
  ca-certificates \
  --no-install-recommends \
  && rm -rf /var/lib/apt/lists/*

RUN buildDeps=' \
    gnupg \
    curl \
    dirmngr \
	' \
	&& set -x \
	&& apt-get update && apt-get install -y $buildDeps --no-install-recommends \
	&& rm -rf /var/lib/apt/lists/* \
  && curl -OL http://www.squid-cache.org/Versions/v4/squid-${SQUID_VERSION}.tar.gz \
  && curl -OL http://www.squid-cache.org/Versions/v4/squid-${SQUID_VERSION}.tar.gz.asc \
  && export GNUPGHOME="$(mktemp -d)" \
  && gpg --no-tty --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys ${SQUID_FINGERPRINT} \
  && gpg --verify squid-${SQUID_VERSION}.tar.gz.asc \
  && rm -rf "$GNUPGHOME" \
  && tar xf squid-${SQUID_VERSION}.tar.gz \
  && rm -rf squid-${SQUID_VERSION}.tar.* \
	&& apt-get purge -y --auto-remove $buildDeps

RUN buildDeps=' \
    build-essential \
    libcppunit-dev \
    libssl-dev \
    libltdl-dev \
    libcap2-dev \
    libdb-dev \
    libecap3-dev \
    libexpat1-dev \
    libgnutls28-dev \
    libkrb5-dev \
    comerr-dev \
    libldap2-dev \
    libnetfilter-conntrack-dev \
    libpam0g-dev \
    libsasl2-dev \
    libxml2-dev \
    nettle-dev \
    pkg-config \
    cdbs \
    debhelper \
    lsb-release \
    ed \
	' \
	&& set -x \
	&& apt-get update && apt-get install -y $buildDeps --no-install-recommends \
	&& rm -rf /var/lib/apt/lists/* \
  && ( \
        cd squid-${SQUID_VERSION} \
        && ./configure \
        --prefix=/usr/local/squid \
        --datadir=/usr/share/squid \
        --sysconfdir=/etc/squid \
        --libexecdir=/usr/lib/squid \
        --mandir=/usr/share/man \
        --enable-inline \
        --disable-arch-native \
        --enable-async-io=8 \
        --enable-storeio="ufs,aufs,diskd,rock" \
        --enable-removal-policies="lru,heap" \
        --enable-delay-pools \
        --enable-cache-digests \
        --enable-icap-client \
        --enable-follow-x-forwarded-for \
        --enable-auth-basic="DB,fake,getpwnam,LDAP,NCSA,NIS,PAM,POP3,RADIUS,SASL" \
        --enable-auth-digest="file,LDAP" \
        --enable-auth-negotiate="kerberos,wrapper" \
        --enable-external-acl-helpers="file_userip,kerberos_ldap_group,LDAP_group,session,SQL_session,time_quota,unix_group,wbinfo_group" \
        --enable-security-cert-validators="fake" \
        --enable-storeid-rewrite-helpers="file" \
        --enable-url-rewrite-helpers="fake" \
        --enable-eui \
        --enable-esi \
        --enable-icmp \
        --enable-zph-qos \
        --enable-ecap \
        --disable-translation \
        --with-swapdir=${SQUID_CACHE_DIR} \
        --with-logdir=${SQUID_LOG_DIR} \
        --with-pidfile=/var/run/squid.pid \
        --with-filedescriptors=65536 \
        --with-large-files \
        --with-default-user=${SQUID_USER} \
        --with-gnutls \
        --with-openssl \
        --enable-ssl-crtd \
        --enable-linux-netfilter \
        --enable-err-language=${SQUID_ERROR_LANG} \
        && make -j $(grep -c 'processor' /proc/cpuinfo) \
        && make install \
       ) \
    && apt-get purge -y --auto-remove $buildDeps \
    && rm -rf squid*

COPY entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh

EXPOSE 3128/tcp
ENTRYPOINT ["/sbin/entrypoint.sh"]
