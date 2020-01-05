FROM alpine:edge

MAINTAINER goofts loking.zhao.moshang@icloud.com
# jupyterlab安装的其他内核存于 ~/.local/share/jupyter/kernels 文件夹
ENV HUMMINGBIRDS_VERSION 2.3.5

WORKDIR /root

RUN echo -e 'http://dl-cdn.alpinelinux.org/alpine/edge/testing' | tee -a /etc/apk/repositories && \
    sed  -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g'              /etc/apk/repositories

RUN apk add --no-cache texlive-xetex texmf-dist-langchinese texmf-dist-most && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf                  && \
    rm -rf ~/* ~/.[^jvp\.]* /tmp/* /var/tmp/* /var/cache/apk/*              && \
    rm -rf /usr/local/share/.[0-9a-zA-Z]* /usr/local/share/*                && \
    rm -rf /usr/share/jupyter/lab/staging/build/* /usr/share/jupyter/kernels/*

RUN apk update && apk upgrade && apk add --no-cache git          && \
    git clone https://github.com/goofts/skylarks ~/skylarks      && \
    chmod +x ~/skylarks/setup.sh && sh ~/skylarks/setup.sh       && \
    cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime          && \
    rm /usr/bin/vi && ln -snf /usr/bin/vim /usr/bin/vi           && \
    rm /bin/sh && ln -snf /bin/bash /bin/sh                      && \
    chown root:root /usr/sbin/nginx && chmod u+s /usr/sbin/nginx && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf       && \
    rm -rf ~/* ~/.[^jvp\.]* /tmp/* /var/tmp/* /var/cache/apk/*   && \
    rm -rf /usr/local/share/.[0-9a-zA-Z]* /usr/local/share/*     && \
    rm -rf /usr/share/jupyter/lab/staging/build/* /usr/share/jupyter/kernels/*

RUN git clone https://github.com/goofts/skylarks ~/skylarks           && \
    mkdir ~/.pip && mv ~/skylarks/pip.conf ~/.pip                     && \
    awk '{cmd="pip3 install "$1;system(cmd)}' ~/skylarks/requirements && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf            && \
    rm -rf ~/* ~/.[^jvp\.]* /tmp/* /var/tmp/* /var/cache/apk/*        && \
    rm -rf /usr/local/share/.[0-9a-zA-Z]* /usr/local/share/*          && \
    rm -rf /usr/share/jupyter/lab/staging/build/* /usr/share/jupyter/kernels/*

RUN jupyter labextension install jupyterlab-dash@0.1.0-alpha.3           && \
    jupyter labextension install jupyterlab-drawio && npm cache clean -f && \
    find /usr/lib/python* -name __pycache__ | xargs rm -rf               && \
    rm -rf ~/* ~/.[^jvp\.]* /tmp/* /var/tmp/* /var/cache/apk/*           && \
    rm -rf /usr/local/share/.[0-9a-zA-Z]* /usr/local/share/*             && \
    rm -rf /usr/share/jupyter/lab/staging/build/* /usr/share/jupyter/kernels/*

RUN git clone https://github.com/goofts/hummingbirds.git /hummingbirds

ENV USER postgres
RUN echo -e "\nexport USER=postgres" | tee -a /etc/profile

USER postgres
WORKDIR /var/lib/postgresql

RUN go get -u github.com/goofts/skylarks

RUN ln -snf /var/lib/postgresql/go/src/github.com/goofts/skylarks ~/skylarks

WORKDIR /var/lib/postgresql/go/src/github.com/goofts/skylarks

RUN mkdir -p ~/.jupyter ~/.vim/UltiSnips ~/.vim/bundle && cp vimrc ~/.vimrc             && \
    cp latexmkrc ~/.latexmkrc && go build && initdb -D /var/lib/postgresql/data         && \
    git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim      && \
    git clone https://github.com/honza/vim-snippets.git   ~/.vim/bundle/vim-snippets    && \
    git clone https://github.com/SirVer/ultisnips.git     ~/.vim/bundle/ultisnips       && \
    git clone https://github.com/baskerville/bspwm.git    ~/.vim/bundle/bspwm           && \
    supervisord -c /var/lib/postgresql/go/src/github.com/goofts/skylarks/databases.conf && \
    cp /var/lib/postgresql/go/src/github.com/goofts/skylarks/skylarks.conf                 \
    /var/lib/postgresql/.jupyter/jupyter_notebook_config.py                             && \
    sleep 16 && createdb skylarks && psql -U postgres -d skylarks -f                       \
    /var/lib/postgresql/go/src/github.com/goofts/skylarks/skylarks.sql

EXPOSE 443

CMD sh /var/lib/postgresql/go/src/github.com/goofts/skylarks/skylarks.sh
