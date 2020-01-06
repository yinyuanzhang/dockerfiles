FROM debian:buster-slim
LABEL maintainer "goonnowgit <goonnowgittt@gmail.com>"

ENV DEBIAN_FRONTEND=noninteractive \
  DNSCRYPT_PROXY_VERSION=2.0.35

RUN apt update && apt install -y \
  ca-certificates \
  --no-install-recommends \
  && rm -rf /var/lib/apt/lists/*

RUN buildDeps=' \
    build-essential \
    curl \
    git \
    cmake \
    pkg-config \
    libsodium-dev \
	' \
	&& set -x \
	&& apt-get update && apt-get install -y $buildDeps --no-install-recommends \
	&& rm -rf /var/lib/apt/lists/* \
  && git clone https://github.com/jedisct1/minisign.git \
  && ( \
    cd minisign \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make \
    && make install \
  ) \
  && curl -OL https://github.com/jedisct1/dnscrypt-proxy/releases/download/${DNSCRYPT_PROXY_VERSION}/dnscrypt-proxy-linux_x86_64-${DNSCRYPT_PROXY_VERSION}.tar.gz \
  && curl -OL https://github.com/jedisct1/dnscrypt-proxy/releases/download/${DNSCRYPT_PROXY_VERSION}/dnscrypt-proxy-linux_x86_64-${DNSCRYPT_PROXY_VERSION}.tar.gz.minisig \
  && minisign/build/minisign -Vm dnscrypt-proxy-*.tar.gz -P RWTk1xXqcTODeYttYMCMLo0YJHaFEHn7a3akqHlb/7QvIQXHVPxKbjB5 \
  && tar xvf dnscrypt-proxy-linux_x86_64-${DNSCRYPT_PROXY_VERSION}.tar.gz -C /opt \
  && rm -rf dnscrypt-proxy-linux_x86_64-${DNSCRYPT_PROXY_VERSION}.tar.* \
  && rm -rf minisign \
	&& apt-get purge -y --auto-remove $buildDeps

#WORKDIR /opt/linux-x86_64

#ENV PATH="${PATH}":/opt/linux-x86_64/dnscrypt-proxy

HEALTHCHECK CMD /opt/linux-x86_64/dnscrypt-proxy -resolve www.google.com || exit 1

ENTRYPOINT ["/opt/linux-x86_64/dnscrypt-proxy"]
CMD ["--help"]
