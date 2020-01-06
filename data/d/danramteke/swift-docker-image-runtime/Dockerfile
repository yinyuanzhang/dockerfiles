FROM ubuntu:18.04

ENV SWIFT_TAR_URL https://swift.org/builds/swift-5.0-release/ubuntu1804/swift-5.0-RELEASE/swift-5.0-RELEASE-ubuntu18.04.tar.gz

ENV WORK_DIR /
WORKDIR ${WORK_DIR}

RUN apt-get update && apt-get dist-upgrade -y && DEBIAN_FRONTEND=noninteractive apt-get install -y \
  curl \
  dirmngr \
  gnupg2 \
  libatomic1 \
  libatomic1 \
  libbsd-dev \
  libbsd-dev \
  libbsd0 \
  libcurl4-openssl-dev \
  libicu-dev \
  libicu60 \
  libsqlite3-dev \
  libxml2 \
  openssl \
  pkg-config \
  tzdata \
  zlib1g-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 

RUN curl -fsSL $SWIFT_TAR_URL -o swift.tar.gz \
  && curl -fsSL $SWIFT_TAR_URL.sig -o swift.tar.gz.sig \
  && export GNUPGHOME="$(mktemp -d)" \
  && echo "disable-ipv6" > $GNUPGHOME/dirmgngr.conf \
  && gpg --keyserver ha.pool.sks-keyservers.net  \
  --recv-keys \
  'A62A E125 BBBF BB96 A6E0  42EC 925C C1CC ED3D 1561' \
  && gpg --keyserver ha.pool.sks-keyservers.net --refresh-keys \
  && gpg --batch --verify swift.tar.gz.sig swift.tar.gz \
  && tar xzf swift.tar.gz --strip-components=1 \
  && rm swift.tar.gz \
  && rm swift.tar.gz.sig \
  && find /usr/lib/swift/linux -type f ! -name '*.so*' -delete \
  && rm -rf /usr/lib/swift/linux/*/ \
  && chmod -R go+r /usr/lib/swift \
  && apt-get remove -y gcc cpp icu-devtools libc6-dev binutils manpages-dev manpages  pkg-config perl \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf "$GNUPGHOME" 

CMD /bin/bash
