# Based on Sebastian Tschan <mail@blueimp.net> work

FROM ubuntu:latest

#Workaround to enable nano
ENV	TERM xterm

ENV	DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install --no-install-recommends --no-install-suggests -y \
    nano \
    xvfb \
    xauth \
    ca-certificates \
    fluxbox \
    xvt \
    curl \
    gnupg \
    unzip \
  && apt-get clean \
  && rm -rf \
    /tmp/* \
    /usr/share/doc/* \
    /var/cache/* \
    /var/lib/apt/lists/* \
    /var/tmp/*

# Install Chrome WebDriver latest version
RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    rm /tmp/chromedriver_linux64.zip && \
    chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \
    ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver

# Install Google Chrome
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get -yqq update && \
    apt-get -yqq install google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Start chrome via wrapper script with --no-sandbox argument:
RUN mv /opt/google/chrome/chrome /opt/google/chrome/chrome-original \
&& printf '%s\n' '#!/bin/sh' \
 'exec /opt/google/chrome/chrome-original --no-sandbox "$@"' \
 > /opt/google/chrome/chrome && chmod +x /opt/google/chrome/chrome

# Patch xvfb-run to support TCP port listening (disabled by default in X:
RUN sed -i 's/LISTENTCP=""/LISTENTCP="-listen tcp"/' /usr/bin/xvfb-run

# Add webdriver user+group as a workaround for
# https://github.com/boot2docker/boot2docker/issues/581
RUN useradd -u 1000 -m -U webdriver

RUN export TINI_VERSION=v0.14.0 && curl -sL \
    https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini \
    > /sbin/tini && chmod +x /sbin/tini

WORKDIR /home/webdriver

COPY entrypoint.sh /usr/local/bin/entrypoint
RUN chmod +x /usr/local/bin/entrypoint

# Configure Xvfb via environment variables:
ENV SCREEN_WIDTH 1440
ENV SCREEN_HEIGHT 900
ENV SCREEN_DEPTH 24
ENV DISPLAY :60

# Expose the default webdriver port:
EXPOSE 4444

ENTRYPOINT ["entrypoint"]

CMD ["chromedriver", "--url-base=/wd/hub", "--port=4444", "--whitelisted-ips="]
