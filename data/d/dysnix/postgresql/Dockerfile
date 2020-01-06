ARG TIMESCALE_VERSION="1.5.1"
FROM bitnami/postgresql:11.6.0 AS build

USER 0
ARG TIMESCALE_VERSION
RUN \
  ## compile timescaledb plugin \
  apt-get -y update && apt-get -y install build-essential libssl-dev git dpkg-dev gcc libc-dev make cmake && \
  git clone https://github.com/timescale/timescaledb && \
  cd /timescaledb && git checkout ${TIMESCALE_VERSION} && \
  ./bootstrap -DREGRESS_CHECKS=OFF -DPROJECT_INSTALL_METHOD="docker-bitnami" && \
  cd build && make install DESTDIR=/dist

FROM bitnami/postgresql:11.6.0
USER 0

# Copy to /opt/bitnami/postgresql/{lib,share}
COPY --from=build /dist /
RUN sed -r -i "s/[#]*\s*(shared_preload_libraries)\s*=\s*'(.*)'/\1 = 'timescaledb,\2'/;s/,'/'/" /opt/bitnami/postgresql/share/postgresql.conf.sample
USER 1001
