FROM openjdk:8-jdk-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir -p /usr/share/man/man1 && apt-get update -y && \
  apt-get install --no-install-recommends procps  -y \
  autoconf automake make git xvfb apt locales sudo openssh-client ca-certificates tar gzip expect gcc g++ python-dev python3-dev maven locales unzip zip bzip2 gnupg curl wget \
  build-essential zlib1g-dev libyaml-dev libssl-dev libgdbm-dev libreadline-dev libncurses5-dev libffi-dev bison && \
	rm -rf /var/lib/apt/lists/* && \
	apt-get autoremove -y && \
	apt-get clean

# Use unicode
RUN locale-gen C.UTF-8 || true
ENV LANG=C.UTF-8

ARG sdk_version=sdk-tools-linux-4333796.zip
ARG android_home=/opt/android/sdk

RUN sudo mkdir -p ${android_home} && \
  curl --silent --show-error --location --fail --retry 3 --output /tmp/${sdk_version} https://dl.google.com/android/repository/${sdk_version} && \
  unzip -q /tmp/${sdk_version} -d ${android_home} && \
  rm /tmp/${sdk_version}

ENV ANDROID_HOME ${android_home}
ENV ADB_INSTALL_TIMEOUT 120
ENV PATH=${ANDROID_HOME}/emulator:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-tools:${PATH}

RUN mkdir ~/.android && echo '### User Sources for Android SDK Manager' > ~/.android/repositories.cfg

RUN yes | sdkmanager --licenses && yes | sdkmanager --update

# Update SDK manager and install system image, platform and build tools
RUN sdkmanager \
  "tools" \
  "platform-tools" \
  "emulator"

RUN sdkmanager \
  "build-tools;27.0.0" \
  "build-tools;27.0.1" \
  "build-tools;27.0.2" \
  "build-tools;27.0.3" \
  "build-tools;28.0.0" \
  "build-tools;28.0.1" \
  "build-tools;28.0.2" \
  "build-tools;28.0.3"

# API_LEVEL string gets replaced by m4
RUN sdkmanager "platforms;android-28"

RUN curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
RUN sudo apt-get install -y nodejs && \
	rm -rf /var/lib/apt/lists/* && \
	apt-get autoremove -y && \
	apt-get clean

RUN npm config set spin=false
RUN npm config set progress=false
RUN npm install -g react-native-cli

# Install Ruby
RUN cd /tmp && wget -O ruby-install-0.6.1.tar.gz https://github.com/postmodern/ruby-install/archive/v0.6.1.tar.gz && \
  tar -xzvf ruby-install-0.6.1.tar.gz && \
  cd ruby-install-0.6.1 && \
  sudo make install && \
  ruby-install --cleanup ruby 2.4.3 && \
  rm -r /tmp/ruby-install-*

ENV PATH ${HOME}/.rubies/ruby-2.4.3/bin:${PATH}
RUN apt-get update -y && apt-get install rubygems ruby-dev -y && \
  rm -rf /var/lib/apt/lists/* && \
	apt-get autoremove -y && \
	apt-get clean
  
RUN echo 'gem: --env-shebang --no-rdoc --no-ri' >> ~/.gemrc && gem install bundler fastlane

RUN node --version 
RUN ruby --version
RUN fastlane --version
