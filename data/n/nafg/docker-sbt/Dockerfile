FROM adoptopenjdk/openjdk13:slim

RUN \
  curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823 && \
  echo "deb https://dl.bintray.com/sbt/debian /" > /etc/apt/sources.list.d/sbt.list && \
  curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
  echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list && \
  apt-get update && \
  apt-get install -y nodejs build-essential sbt docker.io gcc g++ make yarn wget python-pip && \
  pip install --upgrade pip docker-compose && \
  echo '#!/usr/bin/env sh' > /usr/local/bin/amm && \
  curl -s https://api.github.com/repos/lihaoyi/ammonite/releases/latest \
    | grep browser_download_url \
    | grep -v bootstrap \
    | sort -V \
    | tail -n1 \
    | cut -d '"' -f 4 \
    | wget -i - -O /usr/local/bin/amm && \
  chmod +x /usr/local/bin/amm
