FROM atlassian/default-image
MAINTAINER "Intelerad Medical Systems"

ARG BUILD_DATE
ARG SOURCE_COMMIT
ARG DOCKERFILE_PATH
ARG SOURCE_TYPE

ENV DEBIAN_FRONTEND=noninteractive LANG=en_US.UTF-8 LC_ALL=C.UTF-8 LANGUAGE=en_US.UTF-8 TERM=dumb DBUS_SESSION_BUS_ADDRESS=/dev/null \
    JAVA_HOME=/usr/lib/jvm/java-8-oracle \
    FIREFOX_VERSION=59.0.2 PHANTOMJS_VERSION=2.1.1 \
    SCREEN_WIDTH=1360 SCREEN_HEIGHT=1020 SCREEN_DEPTH=24

RUN rm -rf /var/lib/apt/lists/* && apt-get -q update &&\
  apt-get install -qy --force-yes xvfb fontconfig bzip2 curl \
    libxss1 libappindicator1 libindicator7 libpango1.0-0 fonts-liberation xdg-utils gconf-service \
  &&\
  apt-get clean &&\
  rm -rf /var/lib/apt/lists/* &&\
  rm -rf /tmp/*

RUN curl --silent --show-error --location --fail --retry 3 https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOMJS_VERSION}-linux-x86_64.tar.bz2 | tar xjfO - phantomjs-${PHANTOMJS_VERSION}-linux-x86_64/bin/phantomjs > /usr/bin/phantomjs && chmod +x /usr/bin/phantomjs

RUN curl --silent --show-error --location --fail --retry 3 http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/${FIREFOX_VERSION}/linux-x86_64/en-US/firefox-${FIREFOX_VERSION}.tar.bz2 > /tmp/firefox-${FIREFOX_VERSION}.tar.bz2 && mkdir /opt/firefox-${FIREFOX_VERSION} && tar xjf /tmp/firefox-${FIREFOX_VERSION}.tar.bz2 -C /opt/firefox-${FIREFOX_VERSION} && rm /tmp/firefox-${FIREFOX_VERSION}.tar.bz2

RUN echo '#!/bin/bash' > /usr/bin/firefox &&\
    echo 'export $(dbus-launch) && set | grep -i dbus && exec xvfb-run -a -s "-screen 0 ${SCREEN_WIDTH}x${SCREEN_HEIGHT}x${SCREEN_DEPTH} -ac +extension RANDR" /opt/firefox-${FIREFOX_VERSION}/firefox/firefox "$@"' >> /usr/bin/firefox &&\
    chmod +x /usr/bin/firefox

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
RUN sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN sudo apt-get update
RUN sudo apt-get install google-chrome-stable
RUN sudo apt-get install jq
RUN mv /opt/google/chrome/google-chrome /opt/google/chrome/google-chrome.orig &&\
    echo '#!/bin/bash' > /opt/google/chrome/google-chrome &&\
    echo 'exec xvfb-run -a -s "-screen 0 ${SCREEN_WIDTH}x${SCREEN_HEIGHT}x${SCREEN_DEPTH} -ac +extension RANDR" /opt/google/chrome/google-chrome.orig --no-sandbox "$@"' >> /opt/google/chrome/google-chrome &&\
    chmod +x /opt/google/chrome/google-chrome

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.docker.dockerfile="$DOCKERFILE_PATH/Dockerfile" \
      org.label-schema.license="GPLv2" \
      org.label-schema.url="https://bitbucket.org/double16/bitbucket-pipeline-browsers" \
      org.label-schema.vcs-ref=$SOURCE_COMMIT \
      org.label-schema.vcs-type="$SOURCE_TYPE" \
      org.label-schema.vcs-url="https://bitbucket.org/double16/bitbucket-pipeline-browsers.git"



ENV NVM_DIR /usr/local/nvm
RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash
ENV NODE_VERSION v9.3.0
RUN /bin/bash -c "source $NVM_DIR/nvm.sh && nvm install $NODE_VERSION && nvm use --delete-prefix $NODE_VERSION"

ENV NODE_PATH $NVM_DIR/versions/node/$NODE_VERSION/lib/node_modules
ENV PATH      $NVM_DIR/versions/node/$NODE_VERSION/bin:$PATH

RUN npm install -g protractor@5.4.2 jasmine@2.8.0 jasmine-spec-reporter@4.2.1 && webdriver-manager update
RUN npm install github-release-notes -g

RUN add-apt-repository ppa:mc3man/trusty-media && \
    apt-get update && \
    apt-get install -y zip ffmpeg python-pip && \
    apt-get clean

RUN pip install --upgrade awscli==1.16.117 s3cmd==2.0.1 python-magic

RUN apt-get install unzip
RUN mkdir -p /tmp/chrome_drivers
RUN wget https://chromedriver.storage.googleapis.com/75.0.3770.140/chromedriver_linux64.zip
RUN mkdir -p /tmp/chrome_drivers/v75
RUN unzip chromedriver_linux64.zip -d /tmp/chrome_drivers/v75/

RUN rm -f chromedriver_linux64.zip
RUN wget https://chromedriver.storage.googleapis.com/77.0.3865.40/chromedriver_linux64.zip
RUN mkdir -p /tmp/chrome_drivers/v77
RUN unzip chromedriver_linux64.zip -d /tmp/chrome_drivers/v77/

RUN rm -f chromedriver_linux64.zip
RUN wget https://chromedriver.storage.googleapis.com/78.0.3904.105/chromedriver_linux64.zip
RUN mkdir -p /tmp/chrome_drivers/v78
RUN unzip chromedriver_linux64.zip -d /tmp/chrome_drivers/v78/

RUN rm -f chromedriver_linux64.zip
RUN wget https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_linux64.zip
RUN mkdir -p /tmp/chrome_drivers/v79
RUN unzip chromedriver_linux64.zip -d /tmp/chrome_drivers/v79/
