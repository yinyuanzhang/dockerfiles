FROM centos:7.3.1611
# 声明此Dockerfile维护者的邮箱,有什么问题可以发到此邮件寻问
LABEL maintainer "wangyang2@cmstop.com"

# 定义软件版本及编译工具变量
ENV TENGINE_VER 2.1.1
ENV LUAJIT_VER 2.0.4
ENV LUA_NGINX_VER 0.9.19
ENV NGX_DEVEL_KIT_VER 0.2.19
ENV NGINX_RTMP_VER 1.1.7
ENV REDIS_NGX_VER 0.12
ENV BUILD_TOOLS gcc gcc-c++ autoconf automake make pcre pcre-devel openssl openssl-devel ibsemanage-devel wget tar gzip
ENV SRC_DIR /usr/local/src

# 切换到工作目录
WORKDIR ${SRC_DIR}

# 开始编译nginx，我们这里使用编译安装nginx而不是使用官方提供的nginx镜像是因为这里使用到了第三方的concat模块，只能编译了。
# 把所有的安装命令都写在一个RUN指令中是因为这样可以减小镜像层数，缩减镜像大小。推荐使用反斜杠和&&把所有的安装命令放置到一行中。
RUN yum -y --noplugins install ${BUILD_TOOLS}\
    && wget http://tengine.taobao.org/download/tengine-${TENGINE_VER}.tar.gz\
    && wget http://luajit.org/download/LuaJIT-${LUAJIT_VER}.tar.gz  \
    && wget https://github.com/openresty/lua-nginx-module/archive/v${LUA_NGINX_VER}.tar.gz  \
    && wget https://github.com/simpl/ngx_devel_kit/archive/v${NGX_DEVEL_KIT_VER}.tar.gz  \
    && wget https://github.com/arut/nginx-rtmp-module/archive/v${NGINX_RTMP_VER}.tar.gz  \
    && wget https://github.com/openresty/redis2-nginx-module/archive/v${REDIS_NGX_VER}.tar.gz  \
    && tar xf tengine-${TENGINE_VER}.tar.gz  \
    && tar xf LuaJIT-${LUAJIT_VER}.tar.gz  \
    && tar xf v${LUA_NGINX_VER}.tar.gz  \
    && tar xf v${NGX_DEVEL_KIT_VER}.tar.gz  \
    && tar xf v${NGINX_RTMP_VER}.tar.gz  \
    && tar xf v${REDIS_NGX_VER}.tar.gz \
    && cd tengine-${TENGINE_VER}  \
    && groupadd -g 10001 nginx \
    && useradd -u 10001 -g nginx nginx \
    && groupmod -g 10001 nginx \
    && usermod -u 10001 nginx \
    && cd ${SRC_DIR}/LuaJIT-${LUAJIT_VER} \
    && make \
    && make install \
    && echo "/usr/local/lib" > /etc/ld.so.conf.d/lua_lib.conf \
    && ldconfig \
    && cd ${SRC_DIR}/tengine-${TENGINE_VER} \
    &&   ./configure --user=nginx --group=nginx --prefix=/usr/local/server/tengine \
                --conf-path=$TENGINE_DIR/conf/nginx.conf \
                --with-http_stub_status_module \
                --with-http_realip_module \
                --with-http_ssl_module \
                --with-http_mp4_module \
                --with-http_flv_module \
                --add-module=$SRC/lua-nginx-module-${LUA_NGINX_VER} \
                --add-module=$SRC/ngx_devel_kit-${NGX_DEVEL_KIT_VER} \
                --add-module=$SRC/nginx-rtmp-module-${NGINX_RTMP_VER} \
                --add-module=$SRC/redis2-nginx-module-${REDIS_NGX_VER}
    && make -j$(nproc) \
    && make install \
    && rm -rf ${SRC_DIR} \
    && yum clean all \

COPY conf/ /usr/local/server/tengine/conf/

# 定义启动容器时运行的命令
#ENTRYPOINT ["/usr/local/server/tengine/sbin/nginx"]
CMD ["/usr/local/server/tengine/sbin/nginx", "-g", "daemon off;"] 

EXPOSE 80 443
