FROM openjdk:8-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    unzip \
    xz-utils \
    git \
    lib32stdc++6 \
    libglu1-mesa &&\
    rm -rf /var/lib/apt/lists/*

# Installing android base on what found at https://github.com/valotas/flutter-android-sdk

ENV LANG C
ENV SDK_TOOLS "4333796"
ENV BUILD_TOOLS "28.0.3"
ENV TARGET_SDK "28"
ENV ANDROID_HOME "/opt/sdk"
ENV FLUTTER_HOME "/opt/flutter"
ENV PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/tools/bin:$ANDROID_HOME/platform-tools:$FLUTTER_HOME/bin

# Download and extract Android Tools
RUN curl -Ss http://dl.google.com/android/repository/sdk-tools-linux-${SDK_TOOLS}.zip -o /tmp/tools.zip && \
    mkdir -p ${ANDROID_HOME} && \
    unzip -qq /tmp/tools.zip -d ${ANDROID_HOME} && \
    rm -v /tmp/tools.zip

# Install SDK Packages
RUN mkdir -p ~/.android/ && touch ~/.android/repositories.cfg && \
    yes | ${ANDROID_HOME}/tools/bin/sdkmanager "--licenses" && \
    ${ANDROID_HOME}/tools/bin/sdkmanager "--update" && \
    ${ANDROID_HOME}/tools/bin/sdkmanager "platform-tools" "extras;android;m2repository" "extras;google;m2repository" "extras;google;instantapps" && \
    ${ANDROID_HOME}/tools/bin/sdkmanager "build-tools;${BUILD_TOOLS}" "platforms;android-${TARGET_SDK}"

# Create flutter user
RUN adduser \
	--disabled-password \
	--gecos "" \
	--no-create-home \
	--home ${FLUTTER_HOME} \
	flutter && \
	mkdir -p ${FLUTTER_HOME} && \
	chown -R flutter:flutter ${FLUTTER_HOME} && \
	chown -R flutter:flutter ${ANDROID_HOME}
USER flutter

# Install flutter
RUN git clone -b stable https://github.com/flutter/flutter.git ${FLUTTER_HOME}

# Upgrade flutter
RUN flutter config --no-analytics && \
	flutter upgrade --force 
