FROM  alpine:3.9
LABEL maintainer="Djerfy <djerfy@gmail.com>"

ENV VERSION=1.1.0

RUN apk -U add bash curl openssl coreutils bind-tools bc git wget
RUN wget -O htrace.tar.gz https://github.com/trimstray/htrace.sh/archive/v${VERSION}.tar.gz && \
    tar xvzf htrace.tar.gz && \
    rm -f htrace.tar.gz && \
    cd htrace.sh-*/ && \
    bash setup.sh install

RUN apk del git wget

CMD ["/usr/local/bin/htrace.sh"]
