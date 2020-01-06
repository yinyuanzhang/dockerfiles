FROM java:openjdk-8-jdk

MAINTAINER Viacheslav Blinov "blinov.vyacheslav@gmail.com"

# Installs i386 architecture required for running 32 bit Android tools
# rm -rf /var/lib/apt/lists/* && \
RUN dpkg --add-architecture i386 && \
    apt-get update -y && \
    apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 expect unzip && \
    apt-get autoremove -y && \
    apt-get clean


# Install android sdk related tools
COPY tools /opt/tools
ENV PATH ${PATH}:/opt/tools

ENV YESS /opt/tools/android-accept-licenses.sh 
ENV ANDROID_SDK_URL https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip
ENV ANDROID_HOME /opt/android-sdk-linux

# Install Android SDK
# chown -R root.root android-sdk-linux && \
RUN cd /opt && \
    wget --output-document=android-sdk.zip --quiet $ANDROID_SDK_URL && \
    unzip android-sdk.zip -d $ANDROID_HOME && \
    rm -f android-sdk.zip

# Setup environment
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools:${ANDROID_HOME}/tools/bin

# Check installation
RUN which sdkmanager

#RUN $YESS sdkmanager "ndk-bundle"
RUN $YESS sdkmanager "extras;intel;"
RUN $YESS sdkmanager "tools" "platform-tools"
RUN $YESS sdkmanager "emulator"
RUN $YESS sdkmanager "system-images;android-23;default;x86"
RUN $YESS sdkmanager "extras;android;m2repository;"
RUN $YESS sdkmanager "extras;google;m2repository"
RUN $YESS sdkmanager "extras;google;google_play_services"
RUN $YESS sdkmanager "platforms:android-22"
RUN $YESS sdkmanager "platforms;android-23"
RUN $YESS sdkmanager "platforms;android-25"
RUN $YESS sdkmanager "platforms;android-26"
RUN $YESS sdkmanager "build-tools;22.0.1"
RUN $YESS sdkmanager "build-tools;23.0.1"
RUN $YESS sdkmanager "build-tools;23.0.3"
RUN $YESS sdkmanager "build-tools;25.0.2"
RUN $YESS sdkmanager "build-tools;25.0.3"
RUN $YESS sdkmanager "build-tools;26.0.2"
RUN $YESS sdkmanager "build-tools;27.0.3"
RUN $YESS sdkmanager "build-tools;28.0.2"
RUN $YESS sdkmanager "platforms;android-28"
RUN $YESS sdkmanager "build-tools;28.0.3"
RUN $YESS sdkmanager --licenses

# create emulator to run tests:
# RUN echo "no" | android create avd \
#                 --force \
#                 --device "Nexus 5" \
#                 --name test \
#                 --target android-23 \
#                 --abi x86 \
#                 --skin WVGA800 \
#                 --sdcard 512M

# start this emulator:
# RUN emulator -avd test && /opt/tools/android-wait-emulator.sh

# Check android sdk packages installation
RUN which adb

# GO to workspace
RUN mkdir -p /opt/workspace
WORKDIR /opt/workspace
