FROM openjdk:8

ENV ANDROID_COMPILE_SDK "28"
ENV ANDROID_BUILD_TOOLS "28.0.2"
ENV ANDROID_SDK_TOOLS "4333796"
ENV GRADLE_VERSION 5.1.1


# get gradle and supporting libs
RUN apt-get update

RUN apt-get install -y curl ruby-dev ruby libstdc++ libc-dev g++ make locales;

RUN curl https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip > gradle.zip;

RUN unzip gradle.zip;

RUN rm gradle.zip;

# RUN apt-get remove -y curl;

RUN locale-gen en_US.UTF-8

ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'

ENV PATH=${PATH}:/gradle-${GRADLE_VERSION}/bin

RUN wget --quiet --output-document=android-sdk.zip https://dl.google.com/android/repository/sdk-tools-linux-${ANDROID_SDK_TOOLS}.zip

RUN mkdir android-sdk-linux

RUN unzip -d android-sdk-linux android-sdk.zip

RUN echo y | android-sdk-linux/tools/bin/sdkmanager "platforms;android-${ANDROID_COMPILE_SDK}" >/dev/null

RUN echo y | android-sdk-linux/tools/bin/sdkmanager "platform-tools" >/dev/null

RUN echo y | android-sdk-linux/tools/bin/sdkmanager "build-tools;${ANDROID_BUILD_TOOLS}" >/dev/null

ENV ANDROID_HOME=$PWD/android-sdk-linux

ENV ANDROID_SDK_ROOT=$PWD/android-sdk-linux

ENV PATH=$PATH:$PWD/android-sdk-linux/platform-tools/

RUN yes | android-sdk-linux/tools/bin/sdkmanager --licenses

RUN gem install fastlane -NV

#install imagemagick for generating app icons

RUN apt install imagemagick -y
