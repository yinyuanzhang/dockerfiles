FROM puyuantech/dtl-linker:latest
LABEL name="dtl-trader"
LABEL maintainer="puyuan<github@puyuan.tech>"

COPY resource/trader-Linux.rpm /tmp/resource/trader-Linux.rpm

RUN echo -e "\\033[45;37m ############### yum local ############### \033[0m" && \
    cd /tmp/resource/ && yum install trader-Linux.rpm -y && \
    yum -y clean all && rm -rf /tmp/resource

WORKDIR /shared/