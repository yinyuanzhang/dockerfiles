FROM marmotcai/centos-base AS nginx

MAINTAINER marmotcai "marmotcai@163.com"

RUN yum install -y gcc-c++ pcre pcre-devel zlib zlib-devel openssl openssl-devel

ENV NGINX_NAME=nginx-1.14.2
ENV NGINX_DIR=/root
ENV NGINX_PACKETS=${NGINX_NAME}.tar.gz
ENV NGINX_URL=https://nginx.org/download/${NGINX_PACKETS}
ENV NGINX_INSTALLPATH=/usr/local/nginx

RUN wget -O ${NGINX_PACKETS} ${NGINX_URL} && \
    tar xvf ${NGINX_PACKETS} -C ${NGINX_DIR} && rm ${NGINX_PACKETS}

WORKDIR ${NGINX_DIR}/${NGINX_NAME}
RUN ./configure --prefix=/usr/local/nginx 
RUN make && make install

WORKDIR ${NGINX_INSTALLPATH}

RUN sed -i '1 a\user root;' ./conf/nginx.conf && \
    sed -i '$i include /data/vhost/*.conf;' ./conf/nginx.conf

RUN rm -rf ${NGINX_DIR}/${NGINX_NAME}

EXPOSE 80

ENTRYPOINT ["/usr/local/nginx/sbin/nginx","-g", "daemon off;"]

