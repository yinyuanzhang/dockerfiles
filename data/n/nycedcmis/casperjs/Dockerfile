FROM nycedcmis/phantomjs:latest
LABEL maintainer.1="alehman@edc.nyc"
LABEL maintainer.2="aho@edc.nyc"

RUN mkdir -p /bin/casperjs && \
    curl -L https://github.com/casperjs/casperjs/archive/1.1.4.tar.gz > 1.1.4.tar.gz && \
    tar -xvzf 1.1.4.tar.gz -C /bin/casperjs && \
    rm -f 1.1.4.tar.gz && \
    ln -sf /bin/casperjs/casperjs-1.1.4/bin/casperjs /usr/bin/casperjs

ENTRYPOINT ["/usr/bin/python", "/usr/bin/casperjs"]