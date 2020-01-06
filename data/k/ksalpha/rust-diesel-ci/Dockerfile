FROM rust:stretch

ENV DEBIAN_FRONTEND=noninteractive

RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main' > /etc/apt/sources.list.d/pgdg.list \
  && wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

# man directory is missing in some base images
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=863199
RUN apt-get update -qq \
  && mkdir -p /usr/share/man/man1 \
  && apt-get upgrade -yqq \
  && apt-get install -yqq \
  parallel net-tools netcat unzip zip cmake libpq-dev postgresql-client-10

# Set timezone to UTC by default
RUN ln -sf /usr/share/zoneinfo/Etc/UTC /etc/localtime

# Install dockerize
RUN DOCKERIZE_URL="https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz" \
  && curl --silent --show-error --location --fail --retry 3 --output /tmp/dockerize-linux-amd64.tar.gz $DOCKERIZE_URL \
  && tar -C /usr/local/bin -xzvf /tmp/dockerize-linux-amd64.tar.gz \
  && rm -rf /tmp/dockerize-linux-amd64.tar.gz \
  && dockerize --version

# Install nightly toolchain 2018-07-07
RUN rustup install nightly-2018-07-07

# Install diesel-cli, cargo-install-update
RUN cargo install cargo-update && cargo install diesel_cli --no-default-features --features=postgres
