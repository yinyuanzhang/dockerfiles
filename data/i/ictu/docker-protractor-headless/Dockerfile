FROM node:8.16.0-stretch-slim
MAINTAINER frank.niessink@ictu.nl
WORKDIR /tmp
COPY webdriver-versions.js ./
ENV CHROME_PACKAGE="google-chrome-stable_73.0.3683.75-1_amd64.deb" NODE_PATH=/usr/local/lib/node_modules:/protractor/node_modules
RUN npm install -g protractor@5.3.2 minimist@1.2.0 && \
    node ./webdriver-versions.js --chromedriver 2.46 && \
    webdriver-manager update --versions.chrome 2.46 && \
    apt-get update && \
    apt-get install -y xvfb wget sudo && \
    # workaround for correct JAVA installation https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=863199
    mkdir -p /usr/share/man/man1 && \  
    apt-get install -y openjdk-8-jre && \
    wget https://github.com/webnicer/chrome-downloads/raw/master/x64.deb/${CHROME_PACKAGE} && \
    dpkg --unpack ${CHROME_PACKAGE} && \
    apt-get install -f -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* \
    rm ${CHROME_PACKAGE} && \
    mkdir /protractor
COPY protractor.sh /
COPY environment /etc/sudoers.d/
# Fix for the issue with Selenium, as described here:
# https://github.com/SeleniumHQ/docker-selenium/issues/87
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null SCREEN_RES=1280x1024x24
WORKDIR /protractor
ENTRYPOINT ["/protractor.sh"]
