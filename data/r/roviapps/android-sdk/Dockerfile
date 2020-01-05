FROM openjdk:8-jdk

ENV ANDROID_COMPILE_SDK=29 \
    ANDROID_BUILD_TOOLS=29.0.2 \
    ANDROID_SDK_TOOLS=25.2.3 \
    ANDROID_HOME=${PWD}/android-sdk-linux \
    GRADLE_URL="https://services.gradle.org/distributions/gradle-5.6.2-all.zip"

RUN apt-get --quiet update --yes \
 && apt-get --quiet install --yes wget tar unzip lib32stdc++6 lib32z1

RUN wget --quiet --output-document=android-sdk.zip https://dl.google.com/android/repository/tools_r${ANDROID_SDK_TOOLS}-linux.zip
RUN unzip android-sdk.zip -d android-sdk-linux
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all --filter android-${ANDROID_COMPILE_SDK}
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all --filter platform-tools
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all --filter build-tools-${ANDROID_BUILD_TOOLS}
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all --filter extra-android-m2repository
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all --filter extra-google-google_play_services
RUN echo y | android-sdk-linux/tools/android --silent update sdk --no-ui --all --filter extra-google-m2repository

RUN yes | android-sdk-linux/tools/bin/sdkmanager "build-tools;${ANDROID_BUILD_TOOLS}"
RUN yes | android-sdk-linux/tools/bin/sdkmanager "platforms;android-${ANDROID_COMPILE_SDK}"

# Install Gradle
RUN wget $GRADLE_URL -O gradle.zip \
 && unzip gradle.zip \
 && mv gradle-5.6.2 gradle \
 && rm gradle.zip \
 && mkdir .gradle

ENV PATH ${PATH}:${PWD}/android-sdk-linux/platform-tools:${PWD}/gradle/bin
