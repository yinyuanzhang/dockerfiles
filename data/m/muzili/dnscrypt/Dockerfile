#From ubuntu LTS
FROM ubuntu:14.04.1
# Never ask for confirmations
ENV DEBIAN_FRONTEND noninteractive
RUN echo "deb http://mirrors.aliyun.com/ubuntu trusty main universe restricted" > /etc/apt/sources.list
RUN echo "deb http://mirrors.aliyun.com/ubuntu trusty-updates main universe restricted" >> /etc/apt/sources.list
RUN echo "deb http://mirrors.aliyun.com/ubuntu trusty-security main universe restricted" >> /etc/apt/sources.list

# Update
RUN apt-get update -qq

# Install HTTPS support for APT.
RUN apt-get install -y --no-install-recommends apt-transport-https ca-certificates
# Install add-apt-repository
RUN apt-get install -y --no-install-recommends  software-properties-common

# Upgrade all packages.
RUN apt-get dist-upgrade -y --no-install-recommends

# Install some common components
RUN apt-get install -y --no-install-recommends wget git curl unzip zip bzip2 less nano vim

# Install development components.
RUN apt-get install -y --no-install-recommends build-essential make expect

RUN mkdir -p /usr/local/src;\
  cd /usr/local/src;\
  curl https://download.libsodium.org/libsodium/releases/libsodium-0.5.0.tar.gz | tar xz;\
  cd libsodium*;\
  ./configure;\
  make && make check;\
  make install

RUN echo /usr/local/lib > /etc/ld.so.conf.d/usr_local_lib.conf;\
  ldconfig;

RUN mkdir -p /usr/local/src;\
  cd /usr/local/src;\
  curl http://download.dnscrypt.org/dnscrypt-proxy/dnscrypt-proxy-1.4.0.tar.bz2 | tar xj;\
  cd dnscrypt-proxy*;\
  ./configure && make -j2;\
  make install

ADD run.sh /run.sh
RUN chmod +x /run.sh

EXPOSE 53
EXPOSE 53/udp

CMD ["/run.sh"]
