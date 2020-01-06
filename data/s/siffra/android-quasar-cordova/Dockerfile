FROM ubuntu

LABEL maintainer="Luiz Benevenuto <luiz@siffra.com.br>"

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

### JAVA
RUN set -x && \
    apt-get update && apt-get install -y software-properties-common --no-install-recommends && \
    # use WebUpd8 PPA
    add-apt-repository ppa:webupd8team/java -y && \
    apt-get update -y && \
    # automatically accept the Oracle license
    echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections && \
    apt-get install -y oracle-java8-installer --no-install-recommends && \
    apt-get install -y oracle-java8-set-default --no-install-recommends && \
    # clean up
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    apt-get purge -y --auto-remove software-properties-common && \
    apt-get autoremove -y && \
    apt-get clean

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

### Android SDKs
ENV ANDROID_SDK_URL="https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz" \
    ANDROID_BUILD_TOOLS_VERSION=28.0.2 \
    # Supported SDKs
    ANDROID_APIS="android-27" \
    ANT_HOME="/usr/share/ant" \
    MAVEN_HOME="/usr/share/maven" \
    GRADLE_HOME="/usr/share/gradle" \
    ANDROID_HOME="/opt/android-sdk-linux"

ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$ANDROID_HOME/build-tools/$ANDROID_BUILD_TOOLS_VERSION:$ANT_HOME/bin:$MAVEN_HOME/bin:$GRADLE_HOME/bin
RUN dpkg --add-architecture i386 && apt-get update && apt-get install -fy curl libstdc++6:i386 zlib1g:i386 --no-install-recommends && \
    # Installs Android SDK
    curl -sL ${ANDROID_SDK_URL} | tar xz -C /opt && \
    echo y | android update sdk -a -u -t platform-tools,${ANDROID_APIS},build-tools-${ANDROID_BUILD_TOOLS_VERSION} && \
    chmod a+x -R $ANDROID_HOME && \
    chown -R root:root $ANDROID_HOME && \
    # clean up
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    apt-get autoremove -y && \
    apt-get clean

### NODEJS
RUN apt-get update && apt-get install -fy curl ca-certificates wget gnupg unzip --no-install-recommends && \
    curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    apt-get update && apt-get install -fy nodejs && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    apt-get autoremove -y && \
    apt-get clean

## Yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update && apt-get install -fy yarn --no-install-recommends && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    apt-get autoremove -y && \
    apt-get clean
 
### Python 2.7 & Git
RUN apt-get update && \
    apt-get install -y git python --no-install-recommends && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    apt-get autoremove -y && \
    apt-get clean

## Cordova & Quasar & Vue
RUN npm install -g cordova && npm install -g quasar-cli @vue/cli @vue/cli-init

RUN cd /usr/share/ && \
    curl -L https://services.gradle.org/distributions/gradle-4.1-all.zip -o gradle-4.1-all.zip && \
    unzip gradle-4.1-all.zip && mv gradle-4.1 gradle && rm -rf gradle-4.1-all.zip

# Create, build, delete an empty cordova project to download necessary maven files and keep them in image
RUN cordova create tmp-project && \
    cd tmp-project && \
    cordova platform add android && \
    cordova build && \
    cd .. && \
    rm -rf tmp-project