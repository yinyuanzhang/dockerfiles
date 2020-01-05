FROM java:8

# Android app

#-------------------------------------------------------------------------------------------------

# Electron runtime libs for headless run (unit tests)
RUN apt-get --yes update
RUN apt-get --yes install libgtk2.0-0 libgconf-2-4 libasound2 libxtst6 libxss1 libnss3 xvfb

#-------------------------------------------------------------------------------------------------

# Ant
ENV ANT_VERSION 1.9.13
ENV ANT_FOLDER apache-ant-${ANT_VERSION}
ENV ANT_ARCHIVE ${ANT_FOLDER}-bin.tar.gz
ENV ANT_URL https://www.apache.org/dist/ant/binaries/${ANT_ARCHIVE}

WORKDIR /opt
RUN wget -q ${ANT_URL} && \
	tar -xzf ${ANT_ARCHIVE} && \
	mv ${ANT_FOLDER} ant && \
	rm ${ANT_ARCHIVE}

ENV PATH ${PATH}:/opt/ant/bin

RUN echo -n "Ant version: " && ant -version

#-------------------------------------------------------------------------------------------------

# Node.js
ENV NODE_VERSION 10.15.3
ENV NODE_FOLDER node-v${NODE_VERSION}-linux-x64
ENV NODE_ARCHIVE ${NODE_FOLDER}.tar.xz
ENV NODE_URL https://nodejs.org/dist/v${NODE_VERSION}/${NODE_ARCHIVE}

WORKDIR /opt
RUN wget -q ${NODE_URL} && \
	tar -xJf ${NODE_ARCHIVE} && \
	mv ${NODE_FOLDER} node && \
	rm ${NODE_ARCHIVE}

ENV PATH ${PATH}:/opt/node/bin

RUN mkdir /.npm
RUN chmod 777 /.npm

RUN echo -n "Node version: " && node --version

#-------------------------------------------------------------------------------------------------

# Android build tools

# Installs i386 architecture required for running 32 bit Android tools
RUN dpkg --add-architecture i386 && \
    apt-get update -y && \
    apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 unzip && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get autoremove -y && \
    apt-get clean

WORKDIR /opt

# Gradle
ENV GRADLE_HOME /opt/gradle
ENV GRADLE_VERSION 4.10.3
ENV GRADLE_HASH 781b6226969b20d353a5c5b5257b759d

ENV PATH $PATH:$GRADLE_HOME/bin
RUN wget -q "https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip" && \
    echo "${GRADLE_HASH} gradle-${GRADLE_VERSION}-bin.zip" > gradle-${GRADLE_VERSION}-bin.zip.md5 && \
    md5sum -c gradle-${GRADLE_VERSION}-bin.zip.md5 && \
    unzip -q "gradle-${GRADLE_VERSION}-bin.zip" && \
    ln -s "gradle-${GRADLE_VERSION}" "${GRADLE_HOME}" && \
    rm "gradle-${GRADLE_VERSION}-bin.zip"*

# Installs Android SDK
ENV ANDROID_SDK_HASH 444e22ce8ca0f67353bda4b85175ed3731cae3ffa695ca18119cbacef1c1bea0
ENV ANDROID_SDK_FILENAME sdk-tools-linux-3859397.zip
ENV ANDROID_SDK_URL https://dl.google.com/android/repository/${ANDROID_SDK_FILENAME}
ENV ANDROID_HOME /opt/android-sdk-linux

RUN wget -q ${ANDROID_SDK_URL} && \
    echo "${ANDROID_SDK_HASH} ${ANDROID_SDK_FILENAME}" > ${ANDROID_SDK_FILENAME}.sha256 && \
    sha256sum -c ${ANDROID_SDK_FILENAME}.sha256 && \
    mkdir -p ${ANDROID_HOME} && \
    unzip -q ${ANDROID_SDK_FILENAME} -d ${ANDROID_HOME} && \
    rm "${ANDROID_SDK_FILENAME}"*

RUN mkdir -p /root/.android && \
    touch /root/.android/repositories.cfg

ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-tools
RUN cd /opt && \
    (sleep 60; while true; do echo "y"; sleep 10; done) | \
    sdkmanager \
        "platform-tools" \
        "platforms;android-27" \
        "build-tools;27.0.0" \
        "add-ons;addon-google_apis-google-24" \
        "extras;google;google_play_services" \
        "extras;android;m2repository" \
        "extras;google;m2repository"

# workdir
RUN mkdir -p /work
WORKDIR /work

CMD ["bash", "-c", "sdkmanager --list; gradle -version;"]
