# See robcherry/docker-chromedriver:latest
# See https://hub.docker.com/r/justinribeiro/chrome-headless/~/dockerfile/
# See https://github.com/SeleniumHQ/docker-selenium
FROM debian:stretch-slim

# Set timezone
RUN echo "Europe/Berlin" > /etc/timezone && \
    dpkg-reconfigure --frontend noninteractive tzdata

# Update the repositories
# Install utilities and certificates
RUN apt-get -yqq update && \
    DEBIAN_FRONTEND=noninteractive apt-get -yqq install --no-install-recommends apt-transport-https=1.4.9 curl=7.52.1-5+deb9u9 unzip=6.0-21 gnupg2=2.1.18-8~deb9u2 ca-certificates=20161130+nmu1+deb9u1 && \
    rm -rf /var/lib/apt/lists/*

# Install Chrome WebDriver
RUN CHROMEDRIVER_VERSION=2.46 && \
    mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION && \
    rm /tmp/chromedriver_linux64.zip && \
    chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver && \
    ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver

# Install Google Chrome
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get -yqq update && \
    DEBIAN_FRONTEND=noninteractive apt-get -yqq install --no-install-recommends google-chrome-stable=72.0.3626.121-1 && \
    rm -rf /var/lib/apt/lists/*

# Create a default user
RUN groupadd -r chrome && useradd -r -g chrome -G audio,video chrome --shell /bin/bash --create-home

# Run Chrome non-privileged
USER chrome

# Default configuration
ENV CHROMEDRIVER_PORT 4444
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null

# Param --whitelisted-ips is not set it to any value to allow all remote connections.
# It is not possible not to use it to allow all connections. Security concerns are delegated to container service
CMD ["/bin/sh", "-c", "/usr/local/bin/chromedriver --log-level=WARNING --port=$CHROMEDRIVER_PORT --whitelisted-ips"]
