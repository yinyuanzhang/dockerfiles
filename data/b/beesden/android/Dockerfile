FROM java:8

ENV PYTHON_VERSION=2.7.13
ENV CORDOVA_VERSION=8.0.0
ENV GRADLE_VERSION=4.5.1

# Android SDK
ENV ANDROID_SDK_URL="https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip" \
    ANT_HOME="/usr/share/ant" \
    MAVEN_HOME="/usr/share/maven" \
    GRADLE_HOME="/opt/lib/gradle-${GRADLE_VERSION}" \
    ANDROID_HOME="/opt/lib/android"

ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$ANDROID_HOME/tools/bin:$ANDROID_HOME/build-tools/$ANDROID_BUILD_TOOLS_VERSION:$ANT_HOME/bin:$MAVEN_HOME/bin:$GRADLE_HOME/bin

WORKDIR /opt/lib

# Install minor deps
RUN echo "Installing libs..."
RUN dpkg --add-architecture i386 && \
    apt-get -qq update && \
    apt-get -qq install -y wget curl ca-certificates python maven ant libncurses5:i386 libstdc++6:i386 zlib1g:i386

# Install gradle - used by android
RUN echo "Installing gradle..."
RUN wget -q -O gradle-bin.zip https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip && \
    unzip -qq "gradle-bin.zip" && \
    rm "gradle-bin.zip"

# Installs Android SDK
WORKDIR /opt/lib/android
RUN echo "Installing android SDK..."
RUN wget -q -O tools.zip ${ANDROID_SDK_URL} && \
    unzip -qq tools.zip && \
    rm tools.zip && \
    chmod a+x -R $ANDROID_HOME && \
    chown -R root:root $ANDROID_HOME

# Install Android packages
RUN echo "Accepting android licenses..."
RUN yes | $ANDROID_HOME/tools/bin/sdkmanager --licenses && \
    touch /root/.android/repositories.cfg

RUN echo "Installing android packages..."
RUN $ANDROID_HOME/tools/bin/sdkmanager "tools" "platform-tools" && \
    $ANDROID_HOME/tools/bin/sdkmanager "build-tools;28.0.3" "build-tools;27.0.3" "build-tools;26.0.2" "build-tools;25.0.3" && \
    $ANDROID_HOME/tools/bin/sdkmanager "platforms;android-28" "platforms;android-27" "platforms;android-26" "platforms;android-25" "platforms;android-24" "platforms;android-23" && \
    $ANDROID_HOME/tools/bin/sdkmanager "extras;android;m2repository" "extras;google;m2repository" && \
    $ANDROID_HOME/tools/bin/sdkmanager "extras;m2repository;com;android;support;constraint;constraint-layout;1.0.2" && \
    $ANDROID_HOME/tools/bin/sdkmanager "extras;m2repository;com;android;support;constraint;constraint-layout-solver;1.0.2" && \
    $ANDROID_HOME/tools/bin/sdkmanager --update

# Clean up
RUN echo "Cleaning up..."
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    apt-get autoremove -y && \
    apt-get clean
