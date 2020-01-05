FROM meitu/jdk:latest

LABEL maintainer "Ligboy.Liu <ligboy@gmail.com>"

ENV ANDROID_HOME /opt/android-sdk
ENV ANDROID_SDK_ROOT /opt/android-sdk

ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-tools
RUN mkdir -p /root/.android && touch /root/.android/repositories.cfg && mkdir -p ${ANDROID_SDK_ROOT}

RUN cd /opt \
  && wget -q https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip -O android-sdk-tools.zip \
  && unzip -qq android-sdk-tools.zip \
  && mv tools/ ${ANDROID_SDK_ROOT}/tools/ \
  && rm -f android-sdk-tools.zip \
  && yes | sdkmanager --licenses

RUN sdkmanager "build-tools;21.1.2"
RUN sdkmanager "build-tools;22.0.1"
RUN sdkmanager "build-tools;23.0.1"
RUN sdkmanager "build-tools;23.0.2"
RUN sdkmanager "build-tools;23.0.3"
RUN sdkmanager "build-tools;24.0.1"
RUN sdkmanager "build-tools;24.0.2"
RUN sdkmanager "build-tools;24.0.3"
RUN sdkmanager "build-tools;24.0.0"
RUN sdkmanager "build-tools;25.0.0"
RUN sdkmanager "build-tools;25.0.1"
RUN sdkmanager "build-tools;25.0.2"
RUN sdkmanager "build-tools;25.0.3"
RUN sdkmanager "build-tools;26.0.0"
RUN sdkmanager "build-tools;26.0.1"
RUN sdkmanager "build-tools;26.0.2"
RUN sdkmanager "build-tools;26.0.3"
RUN sdkmanager "build-tools;27.0.0"
RUN sdkmanager "build-tools;27.0.1"
RUN sdkmanager "build-tools;27.0.2"
RUN sdkmanager "build-tools;27.0.3"
RUN sdkmanager "build-tools;28.0.0"
RUN sdkmanager "build-tools;28.0.1"
RUN sdkmanager "build-tools;28.0.2"

RUN sdkmanager "extras;m2repository;com;android;support;constraint;constraint-layout-solver;1.0.0"
RUN sdkmanager "extras;m2repository;com;android;support;constraint;constraint-layout-solver;1.0.1"
RUN sdkmanager "extras;m2repository;com;android;support;constraint;constraint-layout;1.0.0"
RUN sdkmanager "extras;m2repository;com;android;support;constraint;constraint-layout;1.0.1"

RUN sdkmanager "platforms;android-21"
RUN sdkmanager "platforms;android-22"
RUN sdkmanager "platforms;android-23"
RUN sdkmanager "platforms;android-24"
RUN sdkmanager "platforms;android-25"
RUN sdkmanager "platforms;android-26"
RUN sdkmanager "platforms;android-27"

RUN sdkmanager "add-ons;addon-google_apis-google-21"
RUN sdkmanager "add-ons;addon-google_apis-google-22"
RUN sdkmanager "add-ons;addon-google_apis-google-23"
RUN sdkmanager "add-ons;addon-google_apis-google-24"
RUN sdkmanager "extras;android;m2repository"
RUN sdkmanager "extras;google;m2repository"

RUN apt-get clean -y && apt-get autoremove -y & rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/*

# Go to workspace
RUN mkdir -p /var/workspace
WORKDIR /var/workspace
