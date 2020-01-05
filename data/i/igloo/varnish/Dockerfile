FROM cooptilleuls/varnish:6.0

RUN set -eux; \
  \
  fetchDeps=' \
  ca-certificates \
  wget \
  '; \
  buildDeps=" \
  automake \
  dpkg-dev \
  pkg-config \
  libvarnishapi-dev \
  libtool \
  python-docutils \
  "; \
  apt-get update; \
  apt-get install -y --no-install-recommends $fetchDeps $buildDeps; \
  rm -rf /var/lib/apt/lists/*; \
  \
  wget -O varnish-modules.tar.gz "https://github.com/varnish/varnish-modules/archive/0.15.0.tar.gz"; \
  mkdir -p /tmp/vmod; \
  tar -zxf varnish-modules.tar.gz -C /tmp/vmod --strip-components=1; \
  rm varnish-modules.tar.gz;

RUN cd /tmp/vmod; \
  ./bootstrap; \
  ./configure; \
  make; \
  make install; \
  \
  cd /; \
  rm -rf /tmp/vmod; \
  \
  apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $fetchDeps $buildDeps

EXPOSE 80
