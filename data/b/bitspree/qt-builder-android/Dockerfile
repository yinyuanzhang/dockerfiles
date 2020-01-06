FROM bitspree/qt-builder

LABEL authors="garaone@co3.de"

ENV QT=5.12.4

ENV QT_ARCH ${QT_PATH}/${QT}/android_armv7
ENV ANDROID_HOME /opt/android-sdk-linux
ENV ANDROID_SDK_ROOT ${ANDROID_HOME}
ENV SDKMANAGER ${ANDROID_HOME}/tools/bin/sdkmanager
ENV ANDROID_NDK_ROOT /opt/android-ndk
ENV ANDROID_NDK_TOOLCHAIN_PREFIX arm-linux-androideabi
ENV ANDROID_NDK_TOOLCHAIN_VERSION 4.9
ENV ANDROID_NDK_HOST linux-x86_64
ENV ANDROID_NDK_PLATFORM android-27
ENV ANDROID_NDK_TOOLS_PREFIX ${ANDROID_NDK_TOOLCHAIN_PREFIX}
ENV QMAKESPEC android-g++
ENV PATH=${PATH}:${QT_ARCH}/bin:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools


# ADD ./sdk-tools-linux-4333796.zip /${ANDROID_SDK_ROOT}/sdk.zip
ADD https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip /${ANDROID_SDK_ROOT}/sdk.zip

# ADD ./android-ndk-r18b-linux-x86_64.zip /tmp/android/ndk.zip
ADD https://dl.google.com/android/repository/android-ndk-r18b-linux-x86_64.zip /tmp/android/ndk.zip

RUN apt-get update -q && \
    apt-get install -q -y --no-install-recommends \
        openjdk-8-jdk \
        expect \
        unzip \
    && apt-get clean \
    && rm /bin/sh && ln -s /bin/bash /bin/sh \
    \
    && echo /opt/qt/${QT}/android_armv7/lib > /etc/ld.so.conf.d/qt-${QT}.conf \
    \
    && cd ${ANDROID_SDK_ROOT} \
    && unzip ./sdk.zip \
    && rm ./sdk.zip \
    && ${SDKMANAGER} --list \
    && yes | ${SDKMANAGER} --licenses \
    && ${SDKMANAGER} --update \
    && ${SDKMANAGER} --list \
    && ${SDKMANAGER} platform-tools \
    && ${SDKMANAGER} "build-tools;27.0.3" \
    && ${SDKMANAGER} "sources;${ANDROID_NDK_PLATFORM}" \
    && ${SDKMANAGER} "extras;android;gapid;3" \
    && ${SDKMANAGER} "extras;android;m2repository" \
    && ${SDKMANAGER} "extras;google;google_play_services" \
    && ${SDKMANAGER} "extras;google;market_apk_expansion" \
    && ${SDKMANAGER} "extras;google;market_licensing" \
    && ${SDKMANAGER} "extras;google;m2repository" \
    && ${SDKMANAGER} "platforms;${ANDROID_NDK_PLATFORM}" \
    && ${SDKMANAGER} --update \
    \
    && cd /tmp/android \
    && unzip ndk.zip \
    && mv android-ndk-r18b $ANDROID_NDK_ROOT \
    && chmod -R +rX $ANDROID_NDK_ROOT \
    && rm -rf /tmp/android \
    \
    && apt-get clean autoclean \
    && apt-get autoremove -y \
    && rm -rf \
        /var/lib/apt/lists/* \
        /tmp/* \
        /var/tmp/* \
        /var/lib/dpkg/* \
        /var/lib/cache/* \
        /var/lib/log/*

CMD ["/bin/bash"]
