FROM gableroux/unity3d:2018.2.3f1-android

MAINTAINER ***@***

RUN apt-get update && \
    apt-get install -y blender

# unity 2018 needs jdk 8 https://docs.unity3d.com/Manual/android-sdksetup.html
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:openjdk-r/ppa && \
    apt-get update && \
    apt-get install -y openjdk-8-jdk
    
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/jre/
ENV PATH ${PATH}:/usr/lib/jvm/java-8-openjdk-amd64/jre/bin


RUN apt-get update && \
    apt-get install unzip

# ------------------------------------------------------ 
# --- Download Android SDK tools into $ANDROID_HOME
ENV ANDROID_HOME /opt/android-sdk-linux


# newer SDK versions https://stackoverflow.com/questions/37505709/how-do-i-download-the-android-sdk-without-downloading-android-studio
RUN cd /opt && \
    wget -q https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip -O android-sdk.zip && \
    unzip -q android-sdk.zip -d android-sdk-linux && \
    rm -f android-sdk.zip && \
    ls -ahl android-sdk-linux

ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools

RUN chmod -R 755 .${ANDROID_HOME}/tools/*

# ------------------------------------------------------ 
# --- Install Android SDKs and other build packages 
# https://developer.android.com/studio/command-line/sdkmanager

# platform-tools,extra-android-support
RUN ${ANDROID_HOME}/tools/bin/sdkmanager "platform-tools"

# SDKs 
# android-23
RUN ${ANDROID_HOME}/tools/bin/sdkmanager "platforms;android-23"

# accept license
RUN yes | ${ANDROID_HOME}/tools/bin/sdkmanager --licenses
  
# ------------------------------------------------------ 
# --- Install Gradle from PPA 
# Gradle PPA 
RUN add-apt-repository ppa:cwchien/gradle
RUN apt-get update && \
    apt-get -y install gradle
RUN gradle -v

# Clean up
RUN rm -rf /tmp/* /var/tmp/*

RUN df -h
