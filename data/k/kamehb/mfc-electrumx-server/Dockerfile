FROM archlinux/base

RUN pacman -Suy --noconfirm && \
    pacman -S --noconfirm git gcc python python-setuptools psmisc && \
    cd / && \
    git clone https://github.com/Exgibichi/electrumx.git && \
    cd electrumx && \
    git checkout mfc && \
    mkdir -p /var/db/electrumx && \
    rm -rf .git && \
    python setup.py install && \
    pacman -R --noconfirm git gcc python-setuptools && \
    rm -rf /var/cache

ENTRYPOINT /electrumx/electrumx_server 2>&1 | sh -c 'while read line; do echo "$line"; echo "$line" | grep "INFO:SessionManager:closing down server" && killall python3; done < "${1:-/dev/stdin}"'
