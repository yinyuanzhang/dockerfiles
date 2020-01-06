FROM alpine:latest AS builder

# We install dev dependencies
RUN apk add --no-cache \
    acl-dev \
    attr-dev \
    autoconf \
    automake \
    coreutils \
    g++ \
    gcc \
    git \
    libacl \
    libgcc \
    librsync \
    librsync-dev \
    libstdc++ \
    libtool \
    make \
    ncurses \
    ncurses-dev \
    openssl \
    openssl-dev \
    rsync \
    unzip \
    uthash-dev \
    zlib \
    zlib-dev \
    acl-dev \
    acl \
    attr-dev \
    attr

COPY burp-2.2.18 /tmp/burp-2.2.18

WORKDIR /tmp/burp-2.2.18

# We compile burp
# We remove dev dependencies to decrease image size (also cache and tmp)
RUN autoreconf -vif && \
  ./configure --prefix=/usr --sysconfdir=/etc/burp --localstatedir=/var && \
  make && make install


FROM alpine:latest
COPY --from=builder /var/spool/burp /var/spool/burp
COPY --from=builder /usr/sbin/burp_ca /usr/sbin/burp_ca
COPY --from=builder /usr/sbin/burp /usr/sbin/burp
COPY --from=builder /usr/share/burp /usr/share/burp
WORKDIR /
RUN apk add --no-cache \
    libacl \
    librsync \
    libstdc++ \
    ncurses \
    openssl \
    rsync \
    unzip \
    zlib \
    attr \
    acl \
    bash

CMD [ "burp", "-a","t" ]
