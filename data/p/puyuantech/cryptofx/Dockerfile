FROM puyuantech/dtl-trader:latest
LABEL name="cryptofx"
LABEL maintainer="puyuan<github@puyuan.tech>"

ENV KDB_PORT=8000 NGINX_PORT=8999
COPY resource/cryptofx-Linux.rpm /tmp/resource/cryptofx-Linux.rpm
COPY resource/linuxx86.zip /tmp/resource/kdb.zip

RUN echo -e "\\033[45;37m ############### yum local ############### \033[0m" && \
    cd /tmp/resource/ && yum install cryptofx-Linux.rpm -y && \
    yum install nginx -y && \
    yum install glibc.i686 -y && \
    unzip kdb.zip && mv q /root/ && \ 
    echo '/root/q/l32/q "$@"' > /usr/bin/q && chmod +x /usr/bin/q && \
    yum -y clean all && rm -rf /tmp/resource

WORKDIR /shared/
