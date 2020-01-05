FROM docker:git

RUN apk add --no-cache --no-progress \
        musl \
        python3 \
        bash && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache-dir --upgrade pip setuptools && \
    rm -r /root/.cache && rm -rf /tmp/* && \
    cd /usr/bin && \
    ln -sf easy_install-3 easy_install && \
    ln -sf idle3 idle && \
    ln -sf pydoc3 pydoc && \
    ln -sf python3 python && \
    ln -sf python-config3 python-config && \
    ln -sf pip3 pip
