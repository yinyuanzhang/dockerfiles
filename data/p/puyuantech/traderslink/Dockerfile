FROM puyuantech/dtl-trader:latest
LABEL name="traderslink"
LABEL maintainer="puyuan<github@puyuan.tech>"

COPY resource/impls-Linux.rpm /tmp/resource/impls-Linux.rpm

RUN echo -e "\\033[45;37m ############### yum local ############### \033[0m" && \
    cd /tmp/resource/ && yum install impls-Linux.rpm -y && \
    yum -y clean all && rm -rf /tmp/resource

WORKDIR /shared/