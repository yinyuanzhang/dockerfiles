FROM circleci/ruby:2.3.3-node-browsers
ENV YARN_VERSION 0.27.5
ENV DOCKERFILE_VERSION 20180203

WORKDIR /tmp

## Install latest chrome
RUN \
  sudo apt-get update \
  && sudo apt-get install lsb-release libgtk-3-dev \
  && curl -L -o google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
  && sudo dpkg -i google-chrome.deb \
  && sudo sed -i 's|HERE/chrome"|HERE/chrome" --disable-setuid-sandbox|g' /opt/google/chrome/google-chrome \
  && rm google-chrome.deb

## Install latest chromedriver
RUN \
  wget https://chromedriver.storage.googleapis.com/2.32/chromedriver_linux64.zip \
  && unzip chromedriver_linux64.zip \
  && sudo cp chromedriver /usr/local/bin/chromedriver

## Update yarn
# https://discuss.circleci.com/t/yarn-version-0-27/14451/5
RUN set -ex \
  && for key in \
    6A010C5166006599AA17F08146C2130DFD2497F5 \
  ; do \
    gpg --keyserver pgp.mit.edu --recv-keys "$key" || \
    gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \
    gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \
  done \
  && curl -fSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \
  && curl -fSLO --compressed "https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" \
  && gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz \
  && sudo mkdir -p /opt/yarn \
  && sudo tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/yarn --strip-components=1 \
  && sudo ln -s -f /opt/yarn/bin/yarn /usr/local/bin/yarn \
  && sudo ln -s -f /opt/yarn/bin/yarn /usr/local/bin/yarnpkg \
  && sudo rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz


RUN \
  (echo "DOCKERFILE_VERSION ${DOCKERFILE_VERSION}" \
    && ruby -v \
    && echo "yarn $(yarn --version)" \
    && chromedriver -v \
    && google-chrome --version \
    ) >> /tmp/.versions

