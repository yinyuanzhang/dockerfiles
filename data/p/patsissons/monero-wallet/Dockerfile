ARG DISTRO_NAME=ubuntu
ARG DISTRO_VERSION=latest

FROM ${DISTRO_NAME}:${DISTRO_VERSION}

ENV DEBIAN_FRONTEND=noninteractive \
    DISPLAY=:100 \
    DOWNLOAD_URI=https://downloads.getmonero.org/gui/linux64 \
    UID=1001 \
    XPRA_SCALING=0

COPY entrypoint.sh /config/

WORKDIR /tmp

RUN  set -x \
  && adduser --gecos '' --uid $UID --disabled-password --shell /bin/bash --home /config user \
  && apt-get update \
  && apt-get install -qq --no-install-recommends -y gnupg2 software-properties-common wget \
  && wget -q -O - http://winswitch.org/gpg.asc | apt-key add - \
  && echo "deb http://winswitch.org/ bionic main" > /etc/apt/sources.list.d/xpra.list \
  && apt-get update \
  && apt-get install -qq --no-install-recommends -y \
      libegl1-mesa libgl1-mesa-glx libjs-jquery libqt5core5a libqt5qml5 libx11-6 libx11-xcb1 \
      libxcb1 libxcb-glx0 python-websockify qml-module-qtquick-controls \
      qml-module-qtquick-dialogs qml-module-qtquick-xmllistmodel qt5-default qttools5-dev-tools \
      xpra xpra-html5 xvfb \
  && wget -q --show-progress --progress=bar:force:noscroll -O monero-gui-linux.tar.bz2 ${DOWNLOAD_URI} \
  && mkdir -p monero-gui-linux \
  && tar -xojf monero-gui-linux.tar.bz2 -C monero-gui-linux --strip-components=2 \
  && rm -f monero-gui-linux.tar.bz2 \
  && chmod -R a+rX monero-gui-linux \
  && mv monero-gui-linux /opt \
  && mkdir -p /run/user/$UID /run/xpra \
  && chmod 755 /config/entrypoint.sh \
  && chown -R user:user  /config /run/user/$UID /run/xpra \
  && apt-get -y autoremove \
  && apt-get clean autoclean \
  && rm -rf /var/lib/{apt,dpkg,cache,log}

USER user

WORKDIR /config
VOLUME /config

EXPOSE 10000

ENTRYPOINT ["/config/entrypoint.sh"]
