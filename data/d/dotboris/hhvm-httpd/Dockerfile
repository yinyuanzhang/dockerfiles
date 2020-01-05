FROM httpd:2.4

MAINTAINER Boris Bera <bera.bors@gmail.com>

RUN \
  # hhvm keys & repo
  apt-key adv --recv-keys --keyserver \
    hkp://keyserver.ubuntu.com:80 0x5a16e7281be7a449 \
  && echo deb http://dl.hhvm.com/debian jessie main \
    > /etc/apt/sources.list.d/hhvm.list \

  && apt-get update \

  # Supervisor (init process) & curl (for installing hhvm)
  && apt-get install -y curl supervisor \

  # hhvm from .deb in hhvm repo
  # Old versions of hhvm package are not referenced in the repo, but the .deb
  # files are present. See: https://github.com/facebook/hhvm/issues/7332`
  && curl -sL http://dl.hhvm.com/debian/pool/main/h/hhvm/hhvm_3.14.5~jessie_amd64.deb \
    > /tmp/hhvm_3.14.5~jessie_amd64.deb \
  && echo '594e06fa3e69eecba6f762c330c75fa821781d76  /tmp/hhvm_3.14.5~jessie_amd64.deb' \
    | sha1sum --check - --status \
  && dpkg --force-depends -i /tmp/hhvm_3.14.5~jessie_amd64.deb \
  && apt-get -f install -y \

  # Cleanup hhvm build deps
  && rm -f /tmp/hhvm_3.14.5~jessie_amd64.deb \
  && apt-get remove --purge -y curl \

  # cleanup apt cache
  && rm -rf /var/lib/apt/lists/* \

  # app dir
  && mkdir /app

WORKDIR /app

COPY httpd*.conf /usr/local/apache2/conf/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord"]
