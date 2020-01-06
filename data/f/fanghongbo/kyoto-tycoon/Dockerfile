FROM docker.io/centos
MAINTAINER fanghongbo

# 1. 安装基本依赖
RUN yum install epel-release -y \
    && yum update -y \
    && yum install -y xz gcc gcc-c++ automake zlib-devel openssl* make lua-devel zlib-devel lzo-devel -y

# 2. 编译kyotocabinet
COPY ./*.gz /opt/
WORKDIR /opt/
RUN tar xf kyotocabinet.tar.gz \
    && cd kyotocabinet \
    && ./configure \
    && make \
    && make install \
    && rm -rf /opt/kyotocabinet/ 

# 3. 编译kyototycoon
WORKDIR /opt/
RUN tar xf kyototycoon.tar.gz \
    && cd kyototycoon \
    && ./configure --prefix=/usr/local \
    --build \
    --enable-static \
    --enable-lua \
    --enable-sec-openssl \
    --with-lua=./dep/lua-5.1.4 \
    && make \
    && make install \
    && rm -rf /opt/kyototycoon/ \
    && grep "/usr/local/lib" /etc/ld.so.conf || echo "/usr/local/lib" >> /etc/ld.so.conf \
    && ldconfig 

# 4. 数据持久化
VOLUME /data

# 5. 准备文件
COPY docker-entrypoint.sh /bin/docker-entrypoint.sh
RUN chmod u+x /bin/docker-entrypoint.sh

# 6、启动命令
EXPOSE 1978
ENTRYPOINT ["docker-entrypoint.sh"]
