FROM coturiv/ci-android:latest
LABEL maintainer="coturiv@gmail.com"

ENV NODE_VERSION=10.x

# Install Nodejs
RUN curl -sL https://deb.nodesource.com/setup_${NODE_VERSION} | sudo -E bash - && \
    apt-get install -y nodejs && \
    apt-get clean;

RUN apt-get install -y bzip2 libgconf-2-4 # for extracting firefox and running chrome, respectively


# https://github.com/CircleCI-Public/circleci-dockerfiles/blob/master/node/images/10.2.0/browsers/Dockerfile

# install chrome

RUN curl --silent --show-error --location --fail --retry 3 --output /tmp/google-chrome-stable_current_amd64.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
      && (sudo dpkg -i /tmp/google-chrome-stable_current_amd64.deb || sudo apt-get -fy install)  \
      && rm -rf /tmp/google-chrome-stable_current_amd64.deb \
      && sudo sed -i 's|HERE/chrome"|HERE/chrome" --disable-setuid-sandbox --no-sandbox|g' \
           "/opt/google/chrome/google-chrome" \
      && google-chrome --version

RUN export CHROMEDRIVER_RELEASE=$(curl --location --fail --retry 3 http://chromedriver.storage.googleapis.com/LATEST_RELEASE) \
      && curl --silent --show-error --location --fail --retry 3 --output /tmp/chromedriver_linux64.zip "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_RELEASE/chromedriver_linux64.zip" \
      && cd /tmp \
      && unzip chromedriver_linux64.zip \
      && rm -rf chromedriver_linux64.zip \
      && sudo mv chromedriver /usr/local/bin/chromedriver \
      && sudo chmod +x /usr/local/bin/chromedriver \
      && chromedriver --version

# Install ionic, cordova, angular-cli and firebase-tools
RUN npm install -g ionic cordova @angular/cli firebase-tools
