From centos:7

MAINTAINER actanble <actanble@gmail.com>

# TODO Set the time and lang
ENV LANG en_US.UTF-8
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
RUN sed -i -e '/mirrors.cloud.aliyuncs.com/d' -e '/mirrors.aliyuncs.com/d' /etc/yum.repos.d/CentOS-Base.repo
RUN curl -o /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
RUN yum makecache

# All Libs Used Backup In https://github.com/offgithub On 2019-5-28
ENV TENGINE_VERSION=2.3.2
ENV DEPLOY_PATH=/usr/local/src/nginx_waf

RUN mkdir -p ${DEPLOY_PATH}
ADD . ${DEPLOY_PATH}

WORKDIR ${DEPLOY_PATH}

# TODO Install yum-libs Deppends
RUN yum -y install wget curl git
RUN yum install autoconf automake bzip2 \
         flex httpd-devel libaio-devel yajl yajl-devel \
         libass-devel libjpeg-turbo-devel libpng12-devel \
         libtheora-devel libtool libva-devel libvdpau-devel \
         libvorbis-devel libxml2-devel libxslt-devel \
         perl texi2html unzip zip openssl lua lua-devel lmdb lmdb-devel \
         openssl-devel geoip geoip-devel ssdeep ssdeep-devel gcc-c++ \
         gd-devel GeoIP GeoIP-devel GeoIP-data doxygen libxml2 libxml2-dev zlib-devel \
         perl perl-devel perl-ExtUtils-Embed redhat-rpm-config -y

# Install gperftools
RUN git clone https://github.com/gperftools/gperftools && cd gperftools && sh autogen.sh && ./configure && make && make install

# Install Luajit2
RUN git clone https://github.com/openresty/luajit2 && cd luajit2 &&  make && make install

# Download Tengine
RUN wget https://github.com/alibaba/tengine/archive/${TENGINE_VERSION}.zip  && unzip ${TENGINE_VERSION}.zip -d ${DEPLOY_PATH}

# TODO Build Modsecurity
# https://github.com/SpiderLabs/ModSecurity/wiki/Compilation-recipes-for-v3.x#centos-7-minimal-dynamic

RUN git clone https://github.com/SpiderLabs/ModSecurity.git \
        &&  cd ModSecurity  \
        &&  /bin/bash build.sh  \
        && yum install -y https://archives.fedoraproject.org/pub/archive/fedora/linux/updates/23/x86_64/b/bison-3.0.4-3.fc23.x86_64.rpm \
        &&  git submodule init  \
        &&  git submodule update  \
        &&  ./configure \
        && make && make install

ENV MODSECURITY_INC=${DEPLOY_PATH}/ModSecurity/headers/
ENV MODSECURITY_LIB=${DEPLOY_PATH}/ModSecurity/src/.libs/

RUN git clone https://github.com/SpiderLabs/ModSecurity-nginx.git ;

# TODO Main Build tengine+modsecurity
RUN cd tengine-${TENGINE_VERSION} && \
    ./configure --prefix=/usr/share/nginx \
       --with-http_lua_module \
       --with-luajit-lib=/usr/local/lib/ \
       --with-luajit-inc=/usr/local/include/luajit-2.1/ \
       --with-lua-inc=/usr/local/include/luajit-2.1/ --sbin-path=/usr/sbin/nginx  \
       --modules-path=/usr/lib64/nginx/modules  \
       --conf-path=/etc/nginx/nginx.conf  \
       --error-log-path=/var/log/nginx/error.log  \
       --http-log-path=/var/log/nginx/access.log  \
       --http-client-body-temp-path=/var/lib/nginx/tmp/client_body  \
       --http-proxy-temp-path=/var/lib/nginx/tmp/proxy  \
       --http-fastcgi-temp-path=/var/lib/nginx/tmp/fastcgi  \
       --http-uwsgi-temp-path=/var/lib/nginx/tmp/uwsgi  \
       --http-scgi-temp-path=/var/lib/nginx/tmp/scgi  \
       --pid-path=/var/run/nginx.pid  \
       --lock-path=/run/lock/subsys/nginx  \
       --user=nginx  \
       --group=nginx  \
       --with-file-aio  \
       --with-ipv6  \
       --with-http_auth_request_module  \
       --with-http_ssl_module  \
       --with-http_v2_module  \
       --with-http_realip_module  \
       --with-http_addition_module  \
       --with-http_xslt_module=dynamic  \
       --with-http_image_filter_module=dynamic  \
       --with-http_geoip_module=dynamic  \
       --with-http_sub_module  \
       --with-http_dav_module  \
       --with-http_flv_module  \
       --with-http_mp4_module  \
       --with-http_gunzip_module  \
       --with-http_gzip_static_module  \
       --with-http_random_index_module  \
       --with-http_secure_link_module  \
       --with-http_degradation_module  \
       --with-http_slice_module  \
       --with-http_stub_status_module  \
       --with-http_perl_module=dynamic  \
       --with-mail=dynamic  \
       --with-mail_ssl_module  \
       --with-pcre --with-pcre-jit  \
       --with-stream=dynamic  \
       --with-stream_ssl_module  \
       --with-stream_geoip_module=dynamic  \
       --with-google_perftools_module  \
       --with-debug  \
       --with-cc-opt="-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -m64 -mtune=generic "  \
       --with-ld-opt="-Wl,-z,relro -specs=/usr/lib/rpm/redhat/redhat-hardened-ld -Wl,-E"  \
       --add-module=../ModSecurity-nginx && make && make install

RUN wget https://github.com/SpiderLabs/owasp-modsecurity-crs/archive/v3.1.0.zip && unzip v3.1.0.zip -d /opt/ && \
mv /opt/owasp-modsecurity-crs-3.1.0 /opt/owasp-modsecurity-crs

RUN echo -e "\033[46;30m *****Link some Libs****** \033[0m"
# TODO Add Default Conf Log Dir and Temp dir
RUN mkdir -p /var/lib/nginx/tmp/ /spool/log/nginx;
RUN cp ${DEPLOY_PATH}/ModSecurity/unicode.mapping /etc/nginx ;
RUN ln -sv `find / -type f -name "libprofiler.so*" | grep /usr/local/lib` /lib64/libprofiler.so.0
RUN ln -sv `find / -type f -name "libluajit-5.1.so*" | grep /usr/local/lib` /lib64/libluajit-5.1.so.2
RUN ln -sv /usr/local/modsecurity/lib/libmodsecurity.so.3 /lib64/libmodsecurity.so.3

RUN useradd -s /sbin/nologin -M nginx
# TODO Make Local Conf To Nginx Path
RUN cp -R ./nginx.conf.d/*  /etc/nginx/
COPY . /var/www/

# TODO Add Supervisord Replaced tini
RUN yum -y install supervisor
COPY supervisor_ngx.conf /etc/supervisord.conf

RUN rm -rf ${DEPLOY_PATH}
WORKDIR /root/
USER root

# TODO 推荐多主机部署时候，这个使用的是代理管理。 --net
# EXPOSE 80
# EXPOSE 8080
# HEALTHCHECK --interval=5m --timeout=3s CMD nginx || curl -f http://localhost/ || exit 1
CMD ["/usr/bin/supervisord", '-c', '/etc/supervisord.conf']