FROM omisegoimages/jenkins-slave:3.19
MAINTAINER Kridsada Thanabulpong <sirn@omise.co>

ENV LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
ENV LANG=C.UTF-8

RUN apt-get update && \
    apt-get install -y \
        autoconf \
        autogen \
        build-essential \
        git \
        libtool \
        openssl

ENV OTP_VERSION="20.3.2"

RUN set -xe && \
    OTP_DOWNLOAD_URL="https://github.com/erlang/otp/archive/OTP-${OTP_VERSION}.tar.gz" && \
    OTP_DOWNLOAD_SHA256="9809be52baa23d6fd18ee70b9a9b7c548e44f586db2f46ff5bfe66719cfab10a" && \
    build_deps="automake autoconf libreadline-dev libncurses-dev libssl-dev libyaml-dev libxslt-dev libffi-dev libtool unixodbc-dev" && \
    apt-get update && \
    apt-get install -y --no-install-recommends $build_deps && \
    curl -fsL -o otp-src.tar.gz "${OTP_DOWNLOAD_URL}" && \
    echo "${OTP_DOWNLOAD_SHA256}  otp-src.tar.gz" |sha256sum -c - && \
    mkdir -p /usr/local/src/otp && \
    tar -xzC /usr/local/src/otp --strip-components=1 -f otp-src.tar.gz && \
    rm otp-src.tar.gz && \
    cd /usr/local/src/otp && \
    ./otp_build autoconf && \
    ./configure --build="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" && \
    make -j$(nproc) && \
    make install && \
    find /usr/local -name examples | xargs rm -rf && \
    apt-get purge -y --auto-remove $build_deps && \
    apt-get clean && \
    rm -rf /usr/local/src/otp

ENV REBAR3_VERSION="3.5.0"

RUN set -xe && \
    REBAR3_DOWNLOAD_URL="https://github.com/erlang/rebar3/archive/${REBAR3_VERSION}.tar.gz" && \
    REBAR3_DOWNLOAD_SHA256="e95e9d1f2ce219f548d4f49ad41409af02069190f19e2b6717585eef6ee77501" && \
    curl -fsL -o rebar3-src.tar.gz "${REBAR3_DOWNLOAD_URL}" && \
    echo "${REBAR3_DOWNLOAD_SHA256}  rebar3-src.tar.gz" |sha256sum -c - && \
    mkdir -p /usr/local/src/rebar3 && \
    tar -xzC /usr/local/src/rebar3 --strip-components=1 -f rebar3-src.tar.gz && \
    rm rebar3-src.tar.gz && \
    cd /usr/local/src/rebar3 && \
    HOME=$PWD ./bootstrap && \
    install -v ./rebar3 /usr/local/bin/ && \
    rm -rf /usr/local/src/rebar3
