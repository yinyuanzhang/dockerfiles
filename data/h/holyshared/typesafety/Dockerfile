FROM php:7-cli as composer-env
WORKDIR /tmp
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php -r "if (hash_file('sha384', 'composer-setup.php') === 'a5c698ffe4b8e849a443b120cd5ba38043260d5c4023dbf93e1558871f1f07f58274fc6f4c93bcfd858c6bd0775cd8d1') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
RUN php composer-setup.php --filename=composer
RUN php -r "unlink('composer-setup.php');"

FROM hhvm/hhvm:latest
LABEL maintainer "Noritaka Horio <holy.shared.design@gmail.com>"
ARG DEBIAN_FRONTEND=noninteractive
ARG COMPILER_VERSION=4.08.1
COPY --from=composer-env /tmp/composer /usr/local/bin/composer
RUN apt -y update && \
  apt -y install m4 pkg-config php-cli rsync darcs mercurial bubblewrap libgmp-dev && \
  rm -rf /var/lib/apt/lists/*
RUN curl -sL https://raw.githubusercontent.com/ocaml/opam/master/shell/install.sh > /tmp/install.sh
RUN echo "/usr/local/bin" | sh /tmp/install.sh
RUN opam init -y --root=/tmp/typesafety --disable-sandboxing && opam switch create --root=/tmp/typesafety ${COMPILER_VERSION} 
RUN opam pin add -y --root=/tmp/typesafety typesafety https://github.com/hhpack/typesafety-cli.git
RUN ln -s /tmp/typesafety/${COMPILER_VERSION}/bin/typesafety /usr/local/bin/typesafety
