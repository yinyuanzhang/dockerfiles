FROM gableroux/unity3d:2019.1.0f2-android

RUN apt-get update && \
    apt-get install -y unzip wget

# Install OpenJDK-8
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:openjdk-r/ppa && \
    apt-get update && \
    apt-get install -y openjdk-8-jdk

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/jre/
ENV PATH ${PATH}:/usr/lib/jvm/java-8-openjdk-amd64/jre/bin

# Download Android SDK Manager
ENV ANDROID_HOME /opt/android-sdk-linux

RUN cd /opt && \
    wget -q https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip -O android-sdk.zip && \
    unzip -q android-sdk.zip -d android-sdk-linux && \
    rm -f android-sdk.zip && \
    ls -ahl android-sdk-linux

ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools

RUN chmod -R 755 .${ANDROID_HOME}/tools/*

# Install Android SDK
RUN ${ANDROID_HOME}/tools/bin/sdkmanager "platform-tools"
RUN ${ANDROID_HOME}/tools/bin/sdkmanager "platforms;android-23"
RUN yes | ${ANDROID_HOME}/tools/bin/sdkmanager --licenses

# Clean Up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
RUN rm -rf /tmp/* /var/tmp/*
