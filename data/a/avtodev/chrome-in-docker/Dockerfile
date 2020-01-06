FROM debian:jessie-slim
LABEL Description="Container for running browser tests" Vendor="avto-dev"

RUN \
  apt-get update \
  && apt-get -yq install --no-install-recommends \
    supervisor \
    xvfb gconf2 \
    curl unzip \
    ca-certificates \
    fonts-ipafont-gothic xfonts-cyrillic xfonts-100dpi xfonts-75dpi xfonts-base xfonts-scalable \
  && CHROMEDRIVER_VERSION="`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`" \
  && mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION \
  && curl -sS -o /tmp/chromedriver_linux64.zip \
    http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip \
  && unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION \
  && rm /tmp/chromedriver_linux64.zip \
  && chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver \
  && ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver \
  && curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' > /etc/apt/sources.list.d/google-chrome.list \
  && apt-get update \
  && apt-get -yq install google-chrome-stable x11vnc \
  && apt-get -yq clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY ./etc/xvfb.init.sh /etc/init.d/xvfb
COPY ./configs/supervisord.conf /etc/supervisor/supervisord.conf
COPY ./docker-entrypoint.sh /docker-entrypoint.sh

EXPOSE 9515

ENTRYPOINT ["/docker-entrypoint.sh"]
