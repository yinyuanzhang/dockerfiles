FROM jenkins/jnlp-slave

# Set desired Android Linux SDK version
ENV ANDROID_SDK_ZIP_URL https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip
ENV ANDROID_HOME /opt/android-sdk
ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/tools/bin:$ANDROID_HOME/platform-tools

USER root

# dependencies for setup process
RUN dpkg --add-architecture i386
RUN apt-get update && \
    apt-get install -y software-properties-common unzip \
    libc6:i386 libncurses5:i386 libstdc++6:i386 zlib1g:i386 # 32bit compatibility

# install android sdk
RUN mkdir -p $ANDROID_HOME
ADD $ANDROID_SDK_ZIP_URL $ANDROID_HOME
RUN cd $ANDROID_HOME && \
    unzip *tools*linux*.zip && \
    rm *tools*linux*.zip

# install build tools
RUN yes | sdkmanager "platform-tools" \
    "platforms;android-7" \
    "platforms;android-8" \
    "platforms;android-9" \
    "platforms;android-10" \
    "platforms;android-11" \
    "platforms;android-12" \
    "platforms;android-13" \
    "platforms;android-14" \
    "platforms;android-15" \
    "platforms;android-16" \
    "platforms;android-17" \
    "platforms;android-18" \
    "platforms;android-19" \
    "platforms;android-20" \
    "platforms;android-21" \
    "platforms;android-22" \
    "platforms;android-23" \
    "platforms;android-24" \
    "platforms;android-25" \
    "platforms;android-26" \
    "platforms;android-27" \
    "platforms;android-28" \
    "platforms;android-Q" \
    "build-tools;19.1.0" \
    "build-tools;20.0.0" \
    "build-tools;21.1.2" \
    "build-tools;22.0.1" \
    "build-tools;23.0.1" \
    "build-tools;23.0.2" \
    "build-tools;23.0.3" \
    "build-tools;24.0.0" \
    "build-tools;24.0.1" \
    "build-tools;24.0.2" \
    "build-tools;24.0.3" \
    "build-tools;25.0.0" \
    "build-tools;25.0.1" \
    "build-tools;25.0.2" \
    "build-tools;25.0.3" \
    "build-tools;26.0.0" \
    "build-tools;26.0.1" \
    "build-tools;26.0.2" \
    "build-tools;26.0.3" \
    "build-tools;27.0.0" \
    "build-tools;27.0.1" \
    "build-tools;27.0.2" \
    "build-tools;27.0.3" \
    "build-tools;28.0.0" \
    "build-tools;28.0.0-rc1" \
    "build-tools;28.0.0-rc2" \
    "build-tools;28.0.1" \
    "build-tools;28.0.2" \
    "build-tools;28.0.3" \
    "build-tools;29.0.0-rc1" \
    "add-ons;addon-google_apis-google-15" \
    "add-ons;addon-google_apis-google-16" \
    "add-ons;addon-google_apis-google-17" \
    "add-ons;addon-google_apis-google-18" \
    "add-ons;addon-google_apis-google-19" \
    "add-ons;addon-google_apis-google-21" \
    "add-ons;addon-google_apis-google-22" \
    "add-ons;addon-google_apis-google-23" \
    "add-ons;addon-google_apis-google-24" \
    && yes | sdkmanager --licenses \
    && chmod -R 777 $ANDROID_HOME
