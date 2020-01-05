FROM alpine:3.8

MAINTAINER Arsen Arutyunyan <gdarutyunyan@gmail.com>

ENV KEEPASS_DOWNLOAD_URL http://http.debian.net/debian/pool/main/libf/libfile-keepass-perl/libfile-keepass-perl_2.03.orig.tar.gz
ENV SHELLUI_DOWNLOAD_URL http://http.debian.net/debian/pool/main/libt/libterm-shellui-perl/libterm-shellui-perl_0.92.orig.tar.gz
ENV SORTN_DOWNLOAD_URL http://search.cpan.org/CPAN/authors/id/B/BI/BINGOS/Sort-Naturally-1.03.tar.gz
ENV READLINE_DOWNLOAD_URL http://http.debian.net/debian/pool/main/libt/libterm-readline-gnu-perl/libterm-readline-gnu-perl_1.35.orig.tar.gz

ENV KPCLI_VERSION 3.2

RUN set -ex; \
        \
        apk add --no-cache --virtual .build-deps \
                ncurses-dev \
                readline-dev \
                perl-dev \
                build-base \
                ca-certificates \
                wget; \
        \
        apk add --no-cache \
                perl-crypt-rijndael \
                perl-term-readkey \
                perl-sort-key \
                perl-xml-parser \
                perl-clone \
                readline; \
        \
        mkdir -p /usr/src/keepass; cd /usr/src/keepass; \
        wget -qO- $KEEPASS_DOWNLOAD_URL | tar -xvz -C /usr/src/keepass --strip-components 1; \
        perl Makefile.PL; \
        make install; \
        make clean; \
        rm -r /usr/src/keepass; \
        \
        mkdir -p /usr/src/shellui && cd /usr/src/shellui; \
        wget -qO- $SHELLUI_DOWNLOAD_URL | tar -xvz -C /usr/src/shellui --strip-components 1; \
        perl Makefile.PL; \
        make install; \
        make clean; \
        rm -r /usr/src/shellui; \
        \
        mkdir -p /usr/src/sortn && cd /usr/src/sortn; \
        wget -qO- $SORTN_DOWNLOAD_URL | tar -xvz -C /usr/src/sortn --strip-components 1; \
        perl Makefile.PL; \
        make install; \
        make clean; \
        rm -r /usr/src/sortn; \
        \
        mkdir -p /usr/src/readline && cd /usr/src/readline; \
        wget -qO- $READLINE_DOWNLOAD_URL | tar -xvz -C /usr/src/readline --strip-components 1; \
        perl Makefile.PL; \
        make install; \
        make clean; \
        rm -r /usr/src/readline; \
        \
        mkdir -p /opt/keepass/kpcli/bin; \
        wget https://downloads.sourceforge.net/project/kpcli/kpcli-${KPCLI_VERSION}.pl -O /opt/keepass/kpcli/bin/kpcli; \
        chmod +x /opt/keepass/kpcli/bin/kpcli; \
        ln -s /opt/keepass/kpcli/bin/kpcli /usr/bin/kpcli; \
        \
        apk del .build-deps
        
CMD ["kpcli"]
