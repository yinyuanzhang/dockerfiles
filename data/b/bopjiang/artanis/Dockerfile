FROM        debian:buster
MAINTAINER  Mu Lei
ENV         LANG C.UTF-8
RUN     echo "deb http://mirrors.ustc.edu.cn/debian buster main contrib non-free" > /etc/apt/sources.list \
        && echo "deb-src http://mirrors.ustc.edu.cn/debian buster main contrib non-free" >> /etc/apt/sources.list
RUN     apt-get update \
        && apt-get install -y --no-install-recommends guile-2.2 guile-2.2-dev libmariadbclient-dev mariadb-server git ca-certificates \
        && apt-get build-dep -y --no-install-recommends guile-2.2 \
        && rm -rf /var/lib/apt/lists/*

RUN set -ex \
        && git clone --depth 1 git://github.com/opencog/guile-dbi.git \
        && cd guile-dbi/guile-dbi && ./autogen.sh && ./configure && make -j \
        && make install && ldconfig && cd .. \
        \
        && cd guile-dbd-mysql \
        && ./autogen.sh && ./configure && make -j \
        && make install && ldconfig && cd ../../ && rm -fr guile-dbi \
        \
        && git clone --depth 1 git://git.savannah.gnu.org/artanis.git \
        && cd artanis \
	&& ./autogen.sh \
	&& ./configure \
	&& make -j \
        && make install && cd .. && rm -fr artanis
