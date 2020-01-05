#
# Chromedriver Dockerfile
#

FROM blueimp/basedriver


RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install --no-install-recommends --no-install-suggests -y unzip chromium \
      # Start chromium via wrapper script with --no-sandbox argument:
      && mv /usr/lib/chromium/chromium /usr/lib/chromium/chromium-original \
      && printf '%s\n' '#!/bin/sh' \
        'exec /usr/lib/chromium/chromium-original --no-sandbox "$@"' \
        > /usr/lib/chromium/chromium && chmod +x /usr/lib/chromium/chromium \
      # Remove obsolete files:
      && apt-get clean \
      && rm -rf \
        /tmp/* \
        /usr/share/doc/* \
        /var/cache/* \
        /var/lib/apt/lists/* \
        /var/tmp/* && \
    CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
       mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \
       curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
       unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION && \
       rm /tmp/chromedriver_linux64.zip && \
       chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \
       ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver

USER webdriver

CMD ["chromedriver", "--url-base=/wd/hub", "--port=4444", "--whitelisted-ips="]
