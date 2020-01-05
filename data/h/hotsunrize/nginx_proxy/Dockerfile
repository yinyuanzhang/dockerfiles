
FROM centos:7
MAINTAINER hotsunrize http://uzi.cool

#yum install
RUN yum -y update && \
    yum -y install gcc gcc-c++ autoconf automake wget git && \
    yum -y install zlib zlib-devel openssl openssl-devel pcre-devel && \
    yum clean all

#config
RUN groupadd -r www && useradd -s /sbin/nologin -g www -r www && \
    git clone https://github.com/cuber/ngx_http_google_filter_module && \
    git clone https://github.com/yaoweibin/ngx_http_substitutions_filter_module && \
    wget http://nginx.org/download/nginx-1.10.0.tar.gz && tar xf nginx-1.10.0.tar.gz && cd nginx-1.10.0 && \
    ./configure --user=www --group=www --prefix=/usr/local/nginx --with-http_stub_status_module --with-http_ssl_module --with-http_v2_module --with-http_gzip_static_module --with-ipv6 --with-http_sub_module --add-module=../ngx_http_google_filter_module --add-module=../ngx_http_substitutions_filter_module && \
    make && \
    make install
    
#dir
RUN mkdir -p /data0/cache_tmp /data0/cache /usr/local/nginx/conf/vhost /usr/local/nginx/conf/cert /var/log/nginx/ && \
    mv /usr/local/nginx/conf/nginx.conf /usr/local/nginx/conf/nginx.conf.bak

#last
ADD nginx.conf /usr/local/nginx/conf/nginx.conf
ADD proxy.conf /usr/local/nginx/conf/vhost/proxy.conf
ADD ssl.tar.gz /usr/local/nginx/conf/cert/


EXPOSE 80 443

#start
ENTRYPOINT ["/usr/local/nginx/sbin/nginx", "-g", "daemon off;"]
