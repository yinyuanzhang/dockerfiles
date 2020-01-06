FROM puyuantech/dtl-base:latest
LABEL name="dtl-ci"
LABEL maintainer="puyuan<github@puyuan.tech>"

# 时区设置
ENV TZ=Asia/Shanghai LD_LIBRARY_PATH=/opt/linker/lib/:/opt/trader/lib/ PYTHONPATH=/opt/linker/lib/:/opt/trader/lib/

RUN systemd-machine-id-setup && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    echo -e "\\033[45;37m ############### pip install ############### \033[0m" && \
    pip install twine && \ 
    pip install awscli && \ 
    echo -e "\\033[45;37m ############### yum ############### \033[0m" && \
    rpm --rebuilddb && yum install openssh-clients curl jq -y && yum clean all -y && \
    curl -sL -o /usr/bin/docker 'https://s3-external-1.amazonaws.com/circle-downloads/docker-1.9.0-circleci' && \
    chmod 755 /usr/bin/docker

RUN mkdir -p /root/.ssh && \
    echo -e "Host *\n\tStrictHostKeyChecking no\n" > /root/.ssh/config && \
    git config --global user.name "puyuan-github-bot" && \
    git config --global user.email "github-bot@puyuan.tech" && \
    mkdir -p /root/.aws && \
    echo -e "[default]\nregion = cn-northwest-1\noutput = json" > /root/.aws/config

RUN echo -e "#!/bin/bash\necho -e \$1 | awk 'BEGIN { FS=\".\" } { \$3++;  if (\$3 > 99) { \$3=0; \$2++; if (\$2 > 99) { \$2=0; \$1++ } } } { printf \"%s.%s.%s-pre\", \$1, \$2, \$3 }'" > /root/version_up && chmod 111 /root/version_up && \
    echo -e "#!/bin/bash\necho -e \$1 | sed -e s/-pre//g" > /root/version_release && chmod 111 /root/version_release

WORKDIR /shared/
