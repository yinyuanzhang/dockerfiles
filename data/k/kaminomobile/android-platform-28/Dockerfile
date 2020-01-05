# ====================================================================== #
# Android SDK Docker Image
# ====================================================================== #

# Base image
# ---------------------------------------------------------------------- #
FROM kaminomobile/android-sdk:108

# Author
# ---------------------------------------------------------------------- #
LABEL blazsolar "blaz@kamino.si"

ARG PLATFORM_VERSION=28

# install build tools and platform
RUN sdkmanager "platform-tools" "build-tools;29.0.1" "platforms;android-${PLATFORM_VERSION}" "cmake;3.10.2.4988404" "ndk-bundle"

ENV ANDROID_NDK ${ANDROID_HOME}/ndk-bundle