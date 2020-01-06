FROM ruby:2.5.1-slim

LABEL maintainer="Gimi Liang <zliang@splunk.com>"

# skip runtime bundler installation
ENV FLUENTD_DISABLE_BUNDLER_INJECTION 1

RUN set -e \
 && apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y --no-install-recommends libjemalloc1 jq \
 && buildDeps="make gcc wget g++" \
 && apt-get install -y --no-install-recommends $buildDeps \
 && apt-get install -y --no-install-recommends git \
 && gem install -N fluentd -v "1.2.0" \
 && gem install -N fluent-plugin-systemd -v "0.3.1" \
 && gem install -N fluent-plugin-concat -v "2.2.2" \
 && gem install -N fluent-plugin-prometheus -v "1.0.1" \
 && gem install -N fluent-plugin-jq -v "0.5.1" \
 && git clone -b test https://github.com/hovu96/fluent-plugin-splunk-hec.git \
 && cd fluent-plugin-splunk-hec \
 && rake build \
 && gem install pkg/fluent-plugin-splunk-hec-1.1.1.gem \
 && cd .. \
 && gem install -N oj -v "3.5.1" \
 && dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \
 && wget -O /usr/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-init_1.2.1_$dpkgArch \
 && chmod +x /usr/bin/dumb-init \
 && apt-get purge -y --auto-remove \
                  -o APT::AutoRemove::RecommendsImportant=false \
                  $buildDeps \
 && rm -rf /var/lib/apt/lists/* \
 && rm -rf /tmp/* /var/tmp/* $GEM_HOME/cache/*.gem \
 && mkdir -p /fluentd/etc

 # See https://packages.debian.org/stretch/amd64/libjemalloc1/filelist
ENV LD_PRELOAD "/usr/lib/x86_64-linux-gnu/libjemalloc.so.1"
COPY entrypoint.sh /fluentd/entrypoint.sh

ENTRYPOINT ["/fluentd/entrypoint.sh"]
CMD ["-h"]
