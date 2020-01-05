FROM ubuntu:bionic

MAINTAINER Nikolay Glushchenko <nick@nickalie.com>

RUN dpkg --add-architecture i386 && \
    apt-get update && apt-get install -y wget curl software-properties-common apt-transport-https && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
    wget -nc https://dl.winehq.org/wine-builds/winehq.key && \
    apt-key add winehq.key && \
    rm winehq.key && \
    apt-add-repository https://dl.winehq.org/wine-builds/ubuntu/ && \
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
    echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
    apt-get install -y --no-install-recommends winehq-stable build-essential nodejs git-core ssh openjdk-8-jdk unzip google-cloud-sdk imagemagick yarn google-chrome-stable libpng-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV CHROME_BIN /usr/bin/google-chrome

RUN wineboot && wineboot -s

# Install Android SDK
ENV ANDROID_HOME /opt/android-sdk

RUN mkdir -p $ANDROID_HOME && \
    cd $ANDROID_HOME && \
    wget https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip -O tools.zip && \
    unzip tools.zip && \
    rm -f tools.zip && \
    mkdir $ANDROID_HOME/licenses && \
    echo 8933bad161af4178b1185d1a37fbf41ea5269c55 > $ANDROID_HOME/licenses/android-sdk-license && \
    echo d56f5187479451eabf01fb78af6dfcb131a6481e >> $ANDROID_HOME/licenses/android-sdk-license && \
    echo 84831b9409646a918e30573bab4c9c91346d8abd > $ANDROID_HOME/licenses/android-sdk-preview-license

ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-tools

RUN yes | sdkmanager --licenses

RUN sdkmanager --verbose "build-tools;27.0.3" && \
    sdkmanager --verbose 'platform-tools' && \
    sdkmanager --verbose 'platforms;android-28' && \
    sdkmanager --verbose 'build-tools;28.0.3'

# Install Gradle
ENV GRADLE_HOME /opt/gradle
ENV GRADLE_VERSION 4.6

RUN wget -O gradle.zip "https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip" && \
	unzip gradle.zip && \
	rm gradle.zip && \
	mv "gradle-${GRADLE_VERSION}" "${GRADLE_HOME}/" && \
	ln --symbolic "${GRADLE_HOME}/bin/gradle" /usr/bin/gradle

# preloading cordova 8 dependencies
RUN yarn global add cordova npx && \
    cordova create hello com.example.hello HelloWorld && \
    cd hello && \
    cordova platform add --save android && \
    cordova plugin add --save cordova-plugin-splashscreen && \
    cordova plugin add --save cordova-plugin-fullscreen && \
    cordova build && \
    cd .. && rm -rf hello
