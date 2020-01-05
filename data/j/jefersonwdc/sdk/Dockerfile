FROM jefersonwdc/jdk:1.0

LABEL maintainer="jeferson.wc@outlook.com"

# URL do sdkmanager
ENV SDK_MANAGER_URL https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip

# Path do ANDROID_SDK_ROOT
ENV ANDROID_SDK_ROOT /opt/android-sdk-linux

# Path do GRADLE_DISTRIBUTION
ENV CORDOVA_ANDROID_GRADLE_DISTRIBUTION_URL https://services.gradle.org/distributions/gradle-5.6.2-all.zip

# Armazena o path do ANDROID_SDK_ROOT e do GRADLE_DISTRIBUTION
ENV PATH $PATH:${ANDROID_SDK_ROOT}/tools:${ANDROID_SDK_ROOT}/tools/bin:${ANDROID_SDK_ROOT}/platform-tools:${CORDOVA_ANDROID_GRADLE_DISTRIBUTION_URL}

# Baixa sdkmanager, gradle e api 29 com o tools e platform
RUN apt-get update -qq && \
    apt-get purge maven maven2 -y && \
    apt-get install wget unzip gradle maven -y && \
    mkdir -p ${ANDROID_SDK_ROOT} && \
    wget ${SDK_MANAGER_URL} -O android-sdk-tools.zip && \
    unzip -q android-sdk-tools.zip -d ${ANDROID_SDK_ROOT} && \
    rm android-sdk-tools.zip && \
    yes | sdkmanager --licenses && \
    yes | sdkmanager "tools" \
    "platform-tools" \
    "platforms;android-29" \
    "build-tools;29.0.0" \
    "build-tools;28.0.3" \
    "cmake;3.10.2.4988404" \
    "extras;google;google_play_services" \
    "patcher;v4" \
    "system-images;android-28;google_apis;x86"
