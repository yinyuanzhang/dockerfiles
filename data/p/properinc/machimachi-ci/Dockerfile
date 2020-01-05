FROM circleci/ruby:2.4.6-jessie-node-browsers

ENV RUBY_MAJOR 2.6
ENV RUBY_VERSION 2.6.3

RUN \
  (set -x; node --version; yarn --version) && \
  case $(node --version) in \
  v10.*) ;; \
  *) false; \
  esac

RUN \
  sudo sed -i -E '/backports|updates/d' /etc/apt/sources.list && \
  sudo apt-get clean && \
  sudo apt-get update && \
  sudo apt-get install -y apt-transport-https && \
  curl -sL https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add - && \
  echo "deb http://apt.postgresql.org/pub/repos/apt jessie-pgdg main" | sudo tee /etc/apt/sources.list.d/pgdg.list && \
  sudo apt-get update && \
  buildDeps='bison dpkg-dev libgdbm-dev' && \
  sudo apt-get install -y --no-install-recommends \
    libjemalloc1 libjemalloc-dev \
    $buildDeps \
    cmake \
    postgresql-client-9.6 \
    locales-all fonts-takao-gothic fonts-takao-mincho && \
  mkdir -p /tmp/ruby && \
  cd /tmp/ruby && \
  wget -O ruby.tar.xz "https://cache.ruby-lang.org/pub/ruby/${RUBY_VERSION%.*}/ruby-$RUBY_VERSION.tar.xz" && \
  tar -xJf ruby.tar.xz --strip-components=1 && \
  { echo '#define ENABLE_PATH_CHECK 0'; echo; cat file.c; } > file.c.new && mv file.c.new file.c && \
  autoconf && \
  gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" && \
  ./configure --build="$gnuArch" --disable-install-doc --enable-shared --with-jemalloc && \
  make -j4 && \
  sudo make install && \
  cd && \
  sudo apt-get purge -y --auto-remove $buildDeps && \
  sudo apt-get clean && \
  sudo rm -rf /tmp/ruby /var/lib/apt/lists/*

RUN \
  sudo locale-gen ja_JP.UTF-8 && \
  sudo update-locale LANG=ja_JP.UTF-8 LANGUAGE=ja_JP:ja && \
  sudo dpkg-reconfigure --frontend noninteractive locales

RUN \
  sudo fc-cache -fv
