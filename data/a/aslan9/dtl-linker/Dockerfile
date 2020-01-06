FROM aslan9/dtl-base:latest
LABEL name="dtl-linker"
LABEL maintainer="cjiang<jch.cst@gmail.com>"

COPY resource/linker-Linux.rpm /tmp/resource/linker-Linux.rpm

# 时区设置
ENV TZ=Asia/Shanghai LD_LIBRARY_PATH=/opt/linker/lib/:/opt/trader/lib/ PYTHONPATH=/opt/linker/lib/:/opt/trader/lib/
# 初始化 /etc/machine-id
RUN systemd-machine-id-setup && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    echo -e "\\033[45;37m ############### yum local ############### \033[0m" && \
    cd /tmp/resource/ && yum install linker-Linux.rpm -y && \
    yum -y clean all && rm -rf /tmp/resource

WORKDIR /shared/
