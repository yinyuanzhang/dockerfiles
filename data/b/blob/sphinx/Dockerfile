FROM alpine:3.10

RUN apk --update add python3 && \
    apk add -t deps git gcc libjpeg-turbo-dev musl-dev python3-dev zlib-dev && \
    python3 -m pip install -U sphinx==2.2.1 Pygments setuptools \
                   docutils mkdocs mock pillow \
                   git+https://github.com/rtfd/readthedocs-sphinx-ext.git \
                   sphinx-rtd-theme alabaster \
                   commonmark git+https://github.com/rtfd/recommonmark.git \
                   git+https://github.com/mgaitan/sphinxcontrib-mermaid.git && \
    apk del --purge deps && \
    rm -rf /root/.cache /var/cache/apk/*

CMD /bin/sh
