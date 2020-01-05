FROM ruby:latest

# Dependencies
RUN apt-get update \
  && apt-get -y install --no-install-recommends \
    ntp \
    curl \
    tar \
    bzip2 \
    openssl \
    build-essential \
    libyaml-dev \
    libevent-dev \
    zlib1g \
    zlib1g-dev \
    libssl-dev \
    libxml2 \
    libreadline-gplv2-dev \
  && gem install bundler

# OTS
RUN mkdir -p /var/log/onetime /var/run/onetime /var/lib/onetime /etc/onetime /source/onetime
COPY . /source/onetime
RUN cd /source/onetime \
  && bundle install --frozen --deployment --without=dev \
  && gem update \
  && bin/ots init \
  && cp -R etc/* /etc/onetime

# Entrypoint
COPY entrypoint.sh /entrypoint.sh

# Permissions
RUN chown -R 0 /entrypoint.sh /var/log/onetime /var/run/onetime /var/lib/onetime /etc/onetime /source/onetime \
  && chmod -R g=u /entrypoint.sh /var/log/onetime /var/run/onetime /var/lib/onetime /etc/onetime /source/onetime \
  && chmod -R 770 /entrypoint.sh /source/onetime/bin

EXPOSE 7143
USER 1001
WORKDIR /source/onetime

ENTRYPOINT ["/entrypoint.sh"]
