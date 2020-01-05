FROM ubuntu:14.04
MAINTAINER Zhanwei Wang <wangzw@wangzw.org>

RUN apt-get install -y curl python || exit 1;\
    cd ~ && curl -L "https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf - || exit 1;\
    cd /usr/bin/ && curl -L https://www.dropbox.com/download?dl=packages/dropbox.py -o dropbox.py && chmod a+x dropbox.py || exit 1;\
    ln -s  ${HOME}/.dropbox-dist/dropboxd /usr/bin/dropboxd || exit 1; \
    cd ~ && apt-get upgrade -y || exit 1

ENTRYPOINT dropboxd

