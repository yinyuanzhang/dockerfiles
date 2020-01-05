FROM ubuntu:xenial-20180525

RUN apt update \
  && apt-get install -y software-properties-common \
  && apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8 \
  && add-apt-repository 'deb [arch=amd64,i386,ppc64el] http://nyc2.mirrors.digitalocean.com/mariadb/repo/10.3/ubuntu xenial main' \
  && apt update \
  && apt install -y libmariadbclient-dev mariadb-client \
  && ln -s /usr/bin/mariadb_config /usr/bin/mysql_config \
  && apt-get install -y libusb-dev curl perl-modules build-essential cpanminus \
    uuid-dev libssl-dev libgd-dev libxml2-dev libpng-dev \
  && cpanm local::lib \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /home/twst/tools/repo
COPY repo /home/twst/tools/repo/

ONBUILD ARG CPANM_OPTS
ONBUILD ENV CPANM_OPTS $CPANM_OPTS

ONBUILD COPY ./cpanfile ./tools/

ONBUILD RUN export BUNDLE=0 NOLIMITS=1 \
  && echo $CPANM_OPTS \
  && cpanm $CPANM_OPTS --notest --quiet --mirror file:///home/twst/tools/repo --mirror-only --installdeps /home/twst/tools \
  && rm -Rf ~/.cpan*

WORKDIR /home/twst/

CMD ["/bin/bash"]
