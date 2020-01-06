FROM centos:7
MAINTAINER Anthony Robinson

# Global gem pathing taken from:
# https://github.com/docker-library/ruby/blob/a6202f065bc6d5562703eed454e3479359234750/2.3/Dockerfile

ENV GEM_HOME=/usr/local/bundle
ENV BUNDLE_PATH="$GEM_HOME" \
    BUNDLE_BIN="$GEM_HOME/bin" \
    BUNDLE_SILENCE_ROOT_WARNING=1 \
    BUNDLE_APP_CONFIG="$GEM_HOME"
ENV PATH=$BUNDLE_BIN:$PATH
RUN yum install -y http://yum.postgresql.org/9.4/redhat/rhel-7-x86_64/pgdg-centos94-9.4-2.noarch.rpm \
    && curl --fail -sSLo /etc/yum.repos.d/passenger.repo https://oss-binaries.phusionpassenger.com/yum/definitions/el-passenger.repo \
    && yum -y makecache fast \
    && yum -y update \
    && yum -y install postgresql94-devel wget ImageMagick git make gcc-c++ bzip2 openssl-devel libyaml-devel \
      readline-devel zlib-devel gdbm-devel epel-release \
    && mkdir -p /user/local/etc/gemrc \
      && { \
        echo 'install: --no-document'; \
        echo 'update: --no-document'; \
      } >> /usr/local/etc/gemrc \
    && wget -O /tmp/ruby-2.4.1.tar.gz https://cache.ruby-lang.org/pub/ruby/2.4/ruby-2.4.1.tar.gz \
    && cd /tmp \
    && tar -zxf /tmp/ruby-2.4.1.tar.gz \
    && cd /tmp/ruby-2.4.1 \
    && ./configure --disable-install-doc \
    && make -j"$(nproc)" \
    && make install \
    && cd / \
    && rm -rf /tmp/ruby* \
    && mkdir -p "$GEM_HOME" "$BUNDLE_BIN" \
    && chmod 777 "$GEM_HOME" "$BUNDLE_BIN" \
    && gem install bundler \
    && bundle config build.pg --with-pg-config=/usr/pgsql-9.4/bin/pg_config \
    && yum -y install nginx passenger passenger-devel \
    && yum clean all \
    && ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log
