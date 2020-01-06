FROM dperson/moinmoin
MAINTAINER Andreas Heil <ah@linux-hq.de>

RUN apk --no-cache --no-progress upgrade && \
    apk --no-cache --no-progress add graphviz ttf-freefont

RUN file=GraphvizParser-0.2.3.tar.bz2 && \
    sha256sum=120055909573e392c5c6c0e2638c0075e9d32b8e6e8f351e01d4b4b5b0fdb9d2 && \
    echo "downloading $file ..." && \
    curl -LSs -o "$file" "https://moinmo.in/ParserMarket/graphviz?action=AttachFile&do=get&target=$file" && \
    sha256sum $file | grep -q "$sha256sum" || \
    { echo "expected $sha256sum, got $(sha256sum $file)"; exit 13; } && \
    mkdir graphviz && \
    tar -xf $file -C graphviz --strip-components=1 && \
    cp graphviz/parsers/graphviz.py /usr/local/lib/python2.7/site-packages/MoinMoin/parser/ && \
    python -m py_compile /usr/local/lib/python2.7/site-packages/MoinMoin/parser/graphviz.py && \
    chown root:root /usr/local/lib/python2.7/site-packages/MoinMoin/parser/graphviz.* && \
    chmod 0644 /usr/local/lib/python2.7/site-packages/MoinMoin/parser/graphviz.* && \
    rm -rf graphviz $file

COPY mandarin /usr/local/lib/python2.7/site-packages/MoinMoin/web/static/htdocs/mandarin
COPY mandarin.py /usr/local/share/moin/data/plugin/theme/
COPY PageActions.py /usr/local/share/moin/data/plugin/action/
