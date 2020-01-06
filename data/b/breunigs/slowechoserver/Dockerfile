FROM debian:stretch

RUN apt-get update \
  && apt-get -y install \
    wget \
    build-essential \
    libncurses5-dev \
    libpcre3-dev \
    libreadline-dev \
    libssl1.0-dev \
    zlib1g-dev \
  && apt-get clean -q -y

ARG OPENRESTY_VERSION=1.11.2.5
RUN wget https://github.com/openresty/openresty/releases/download/v${OPENRESTY_VERSION}/openresty-${OPENRESTY_VERSION}.tar.gz \
  && tar xvfz openresty-${OPENRESTY_VERSION}.tar.gz \
  && cd openresty-${OPENRESTY_VERSION} \
  && ./configure \
  && make -j4 \
  && make install \
  && rm -rf /openresty*

EXPOSE 8080
ENTRYPOINT ["/usr/local/openresty/nginx/sbin/nginx"]

ADD nginx.conf /usr/local/openresty/nginx/conf/nginx.conf

