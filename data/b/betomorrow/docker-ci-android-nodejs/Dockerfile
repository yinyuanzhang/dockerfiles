# Base on beevelop/android-nodejs
FROM ubuntu:xenial

ENV DEBIAN_FRONTEND=noninteractive \
    TERM=xterm

RUN buildDeps='software-properties-common'; \
    set -x && \
    apt-get update && apt-get install -y $buildDeps --no-install-recommends && \

    # use WebUpd8 PPA
    add-apt-repository ppa:webupd8team/java -y && \
    apt-get update -y && \

    # automatically accept the Oracle license
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y oracle-java8-installer && \
    apt-get install -y oracle-java8-set-default && \

    # clean up
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    apt-get purge -y --auto-remove $buildDeps && \
    apt-get autoremove -y && apt-get clean

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

ENV ANDROID_SDK_URL="https://dl.google.com/android/repository/tools_r25.2.5-linux.zip" \
    ANDROID_BUILD_TOOLS_VERSION=28.0.0 \
    ANDROID_APIS="android-10,android-15,android-16,android-17,android-18,android-19,android-20,android-21,android-22,android-23,android-24,android-25,android-26" \
    ANT_HOME="/usr/share/ant" \
    MAVEN_HOME="/usr/share/maven" \
    GRADLE_HOME="/usr/share/gradle" \
    ANDROID_HOME="/opt/android"

ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$ANDROID_HOME/build-tools/$ANDROID_BUILD_TOOLS_VERSION:$ANT_HOME/bin:$MAVEN_HOME/bin:$GRADLE_HOME/bin

WORKDIR /opt

RUN dpkg --add-architecture i386 && \
    apt-get -qq update && \
    apt-get -qq install -y wget curl maven ant gradle libncurses5:i386 libstdc++6:i386 zlib1g:i386 && \

    # Installs Android SDK
    mkdir android && cd android && \
    wget -O tools.zip ${ANDROID_SDK_URL} && \
    unzip tools.zip && rm tools.zip && \
    echo y | android update sdk -a -u -t platform-tools,${ANDROID_APIS},build-tools-${ANDROID_BUILD_TOOLS_VERSION} && \
    chmod a+x -R $ANDROID_HOME && \
    chown -R root:root $ANDROID_HOME && \

    # Clean up
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    apt-get autoremove -y && \
    apt-get clean

ENV NODEJS_VERSION=8.11.2 \
    PATH=$PATH:/opt/node/bin

WORKDIR "/opt/node"

RUN apt-get update && apt-get install -y curl git ca-certificates --no-install-recommends && \
    curl -sL https://nodejs.org/dist/v${NODEJS_VERSION}/node-v${NODEJS_VERSION}-linux-x64.tar.gz | tar xz --strip-components=1 && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

# Install fastlane
RUN apt-get update && apt-get -y install build-essential ruby ruby-dev && \
    gem install fastlane -NV

# Install yarn
RUN npm install --global yarn

# Accept licences
RUN echo y | ${ANDROID_HOME}/tools/bin/sdkmanager --update
