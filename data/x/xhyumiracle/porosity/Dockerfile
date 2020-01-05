FROM xhyumiracle/alpine-build-base-git
RUN apk --update add boost-dev git && \
    cd /root && git clone https://github.com/comaeio/porosity.git && \
    cd porosity/porosity/porosity && make && \
    cp porosity /usr/bin/porosity
RUN \
    echo -e '#!/bin/sh\ncd /tmp\nporosity "$@"' > /usr/bin/_porosity && \
    chmod +x /usr/bin/_porosity
ENTRYPOINT ["/usr/bin/_porosity"]
