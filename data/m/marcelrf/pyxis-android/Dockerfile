FROM java:8

# Dockerfile author / maintainer 
MAINTAINER Marcel <marcel@unoceros.com>

# Version 0.4

# Environments
ENV LANG "en_US.UTF-8"
ENV LANGUAGE "en_US.UTF-8"
ENV LC_ALL "en_US.UTF-8"

# --- Base pre-installed tools
RUN apt-get update -qq
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install git curl wget rsync sudo expect
# Common, useful
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python build-essential unzip zip tree
# For PPAs
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install software-properties-common

WORKDIR /opt/
ENV ANDROID_HOME /opt/android-sdk
# ------------------------------------------------------
# --- Install required tools

RUN apt-get update -qq

# Dependencies to execute Android builds
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libc6-i386 lib32stdc++6 lib32gcc1 lib32ncurses5 lib32z1
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y cmake tofrodos libtool-bin automake pkg-config



# ------------------------------------------------------
# --- Download Android SDK tools into $ANDROID_HOME
RUN cd /opt
RUN wget https://dl.google.com/android/repository/tools_r25.2.4-linux.zip -O tools.zip
RUN unzip tools.zip -d android-sdk
RUN rm -f tools.zip
ENV ANDROID_HOME '/opt/android-sdk'
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}
RUN export PATH=$PATH:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}

# ------------------------------------------------------
# --- Download Android NDK

#RUN cd /opt && rm -rf android-ndk && rm -f ndk
#RUN cd /opt && wget -q https://dl.google.com/android/repository/android-ndk-r16b-linux-x86_64.zip -O android-ndk.zip
#RUN cd /opt && unzip android-ndk.zip
#RUN cd /opt && rm -f android-ndk.zip
#RUN cd /opt
#RUN ln -s android-ndk-r16b ndk
#RUN ls -l /opt/ndk
#RUN mkdir -p /opt/ndk/build
#RUN /opt/ndk/build/tools/make_standalone_toolchain.py --api 21 --stl=libc++ --arch arm --install-dir /opt/ndk/tool/arm && \
#    /opt/ndk/build/tools/make_standalone_toolchain.py --api 21 --stl=libc++ --arch arm64 --install-dir /opt/ndk/tool/arm64 && \
#    /opt/ndk/build/tools/make_standalone_toolchain.py --api 21 --stl=libc++ --arch x86 --install-dir /opt/ndk/tool/x86 && \
#    /opt/ndk/build/tools/make_standalone_toolchain.py --api 21 --stl=libc++ --arch x86_64 --install-dir /opt/ndk/tool/x86_64




# ------------------------------------------------------
# --- Install Android SDKs and other build packages

# Other tools and resources of Android SDK
#  you should only install the packages you need!
# To get a full list of available options you can use:
#  android list sdk --no-ui --all --extended
RUN echo y | android update sdk --no-ui --all --filter \
  platform-tools,extra-android-support

#Update sdk manager
#RUN yes | sdkmanager --licenses
RUN yes | sdkmanager --update

# google apis
# Please keep these in descending order!
#RUN echo y | android update sdk --no-ui --all --filter \
#  addon-google_apis-google-22,addon-google_apis-google-21

# SDKs
# Please keep these in descending order!
RUN echo y | android update sdk --no-ui --all --filter \
  android-27,android-26,android-23,android-22,android-21
# build tools
# Please keep these in descending order!
RUN echo y | android update sdk --no-ui --all --filter \
  build-tools-27.0.3,build-tools-26.0.2,build-tools-23.0.2,build-tools-23.0.1,build-tools-22.0.1,build-tools-21.1.2

# Android System Images, for emulators
# Please keep these in descending order!
#RUN echo y | android update sdk --no-ui --all --filter \
#  sys-img-armeabi-v7a-android-23,sys-img-armeabi-v7a-android-22,sys-img-armeabi-v7a-android-21

# Extras
RUN echo y | android update sdk --no-ui --all --filter \
  extra-android-m2repository,extra-google-m2repository,extra-google-google_play_services


RUN apt-get clean
