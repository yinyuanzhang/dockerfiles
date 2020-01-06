FROM alpine:edge

MAINTAINER goofts loking.zhao.moshang@icloud.com
# jupyterlab安装的其他内核存于 ~/.local/share/jupyter/kernels 文件夹
ENV HUMMINGBIRDS_VERSION 8.13.21

WORKDIR /root

RUN apk update && apk upgrade && apk add --no-cache git python3-dev    && \
    git clone https://github.com/goofts/hummingbirds.git /hummingbirds && \
    chmod +x /hummingbirds/setup.sh && sh /hummingbirds/setup.sh       && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime                && \
    rm /usr/bin/vi && ln -snf /usr/bin/vim /usr/bin/vi                 && \
    rm /bin/sh     && ln -snf /bin/bash    /bin/sh                     && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf             && \
    rm -rf ~/* ~/.[0-9a-zA-Z]* /tmp/* /var/tmp/* /var/cache/apk/*      && \
    rm -rf /usr/local/share/.[0-9a-zA-Z]* /usr/local/share/*           && \
    rm -rf /usr/share/jupyter/lab/staging/build/* /usr/share/jupyter/kernels/*

RUN mkdir ~/.pip && mv /hummingbirds/pip.conf ~/.pip                     && \
    awk '{cmd="pip3 install "$1;system(cmd)}' /hummingbirds/requirements && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf               && \
    rm -rf ~/* ~/.[^jvp\.]* /tmp/* /var/tmp/* /var/cache/apk/*           && \
    rm -rf /usr/local/share/.[0-9a-zA-Z]* /usr/local/share/*             && \
    rm -rf /usr/share/jupyter/lab/staging/build/* /usr/share/jupyter/kernels/*

RUN jupyter labextension install @jupyterlab/hub-extension       && \
    jupyter labextension install @fissio/hub-topbar-buttons      && \
    jupyter labextension install jupyterlab-drawio               && \
    jupyter labextension install jupyterlab-dash@0.1.0-alpha.3   && \
    npm install -g configurable-http-proxy && npm cache clean -f && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf       && \
    rm -rf ~/* ~/.[^jvp\.]* /tmp/* /var/tmp/* /var/cache/apk/*   && \
    rm -rf /usr/local/share/.[0-9a-zA-Z]* /usr/local/share/*     && \
    rm -rf /usr/share/jupyter/lab/staging/build/* /usr/share/jupyter/kernels/*

RUN mkdir -p ~/.vim/UltiSnips ~/.vim/bundle /home/goofts/.jupyter                  && \
    git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim && \
    cp -rf /hummingbirds/settings         ~/.jupyter                               && \
    cp -rf /hummingbirds/vimrc            ~/.vimrc                                 && \
    cp -rf ~/.jupyter/lab                 /home/goofts/.jupyter                    && \
    cp -rf ~/.vim                         /home/goofts/.vim                        && \
    cp -rf ~/.vimrc                       /home/goofts/.vimrc                      && \
    cp -rf /hummingbirds/supervisor       /supervisor                              && \
    cp -rf /hummingbirds/startup.sh       /startup.sh                              && \
    chown -R goofts:jupyter /home/goofts && chmod +x /startup.sh                   && \
    chgrp -R jupyter /supervisor && chmod -R 2775 /supervisor                      && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf                         && \
    rm -rf ~/* ~/.[^jvp\.]* /tmp/* /var/tmp/* /var/cache/apk/*                     && \
    rm -rf /usr/local/share/.[0-9a-zA-Z]* /usr/local/share/*                       && \
    rm -rf /usr/share/jupyter/lab/staging/build/* /usr/share/jupyter/kernels/*

EXPOSE 443

CMD sh /startup.sh