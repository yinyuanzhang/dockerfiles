FROM dyne/devuan:ascii
LABEL maintainer="Denis Roio <jaromil@dyne.org>" \
homepage="https://github.com/dyne/docker-base-builds"

RUN echo "deb-src http://deb.devuan.org/merged ascii main" >> /etc/apt/sources.list
RUN mkdir -p /usr/share/man/man1/ \
&& apt-get update \
&& apt-get upgrade -y -q \
&& apt-get install -y -q --allow-downgrades --no-install-recommends \
   build-essential curl devscripts equivs git-buildpackage git \
   lsb-release make autoconf automake libtool zsh \
&& apt-get clean

WORKDIR /root
ENTRYPOINT ["/tini", "--"]

CMD /bin/bash
