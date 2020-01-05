FROM puyuantech/fof

LABEL name="fof-dev"
LABEL maintainer="chs@puyuan.tech"

COPY ./resource/* /tmp/resource/

RUN echo "$$$$$$$$$$$$$$$$$$$$$$$ FOF DEVEL $$$$$$$$$$$$$$$$$$$$$$$" && \
    echo "$$$$$$$$$$$$$$$$$$$$$$$ GIT CONFIG $$$$$$$$$$$$$$$$$$$$$$$" && \
    git config --global credential.helper 'cache --timeout 86400' && \
    git config --global pull.rebase true && \
    git config --global push.default simple && \
    mkdir -p /shared/code/ && \
    cp /tmp/resource/git_clone.sh /shared/code/ && chmod +x /shared/code/git_clone.sh && \
    echo "$$$$$$$$$$$$$$$$$$$$$$$ PREP. FRONT END $$$$$$$$$$$$$$$$$$$$$$$" && \
    rpm --rebuilddb && yum install npm -y && \
    echo "$$$$$$$$$$$$$$$$$$$$$$$ CLEAN UP $$$$$$$$$$$$$$$$$$$$$$$" && \
    yum clean all -y && rm -rf /tmp/resource
