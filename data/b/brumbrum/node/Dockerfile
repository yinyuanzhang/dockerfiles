FROM brumbrum/base
MAINTAINER Alessandro Lattao <alessandro.lattao@brumbrum.it>

# Installo i pacchetti base per python
RUN \
  apt-get -y --no-install-recommends install rsyslog curl gnupg2 && \
  curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
  curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
  echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
  apt-get update && \
  apt-get install -y nodejs yarn && \
  apt-get -y purge curl gnupg2 && \
  apt-get -y autoclean && \
  apt-get -y clean && \
  apt-get -y autoremove

# Configuro rsyslog
ADD etc/rsyslog.conf /etc/rsyslog.conf
ADD etc/rsyslog.d/50-default.conf /etc/rsyslog.d/50-default.conf

# riconfiguro l'entrypoint
ADD bin/entrypoint.sh /entrypoint.sh
RUN ["chmod", "+x", "/entrypoint.sh"]
ENTRYPOINT ["/entrypoint.sh"]
