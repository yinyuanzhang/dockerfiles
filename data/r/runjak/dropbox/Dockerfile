FROM debian:sid

MAINTAINER Jakob Runge <sicarius@g4t3.de>

RUN apt-get update \
 && apt-get install -y \
    wget \
    procps \
    python-gtk2 \
    python \
    libatk1.0-0 \
    libcairo2 \
    libglib2.0-0 \
    libgtk2.0-0 \
    libpango1.0-0 \
    lsb-release \
    python-gpgme \
 && wget -O dropbox.deb "https://www.dropbox.com/download?dl=packages/debian/dropbox_2015.10.28_amd64.deb" \
 && dpkg -i dropbox.deb \
 && useradd --home-dir=/home/u --create-home --uid=1000 --gid=100 --shell=/bin/bash u

COPY entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

WORKDIR /home/u

ENTRYPOINT ["/entrypoint.sh"]
