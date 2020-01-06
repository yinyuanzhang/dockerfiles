FROM puyuantech/dtl-base:latest
LABEL name="dtl-linker"
LABEL maintainer="puyuan<github@puyuan.tech>"

COPY resource/linker-Linux.rpm /tmp/resource/linker-Linux.rpm

RUN echo -e "\\033[45;37m ############### install linker ############### \033[0m" && \
    cd /tmp/resource/ && yum install linker-Linux.rpm -y && \
    yum -y clean all && rm -rf /tmp/resource

WORKDIR /shared/
