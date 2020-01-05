FROM ubuntu:16.04
RUN apt-get update
RUN apt-get install unzip build-essential curl wget git --yes

RUN apt-get install openjdk-8-jdk --yes
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV PATH=${PATH}:${JAVA_HOME}/bin

RUN apt-get install android-sdk android-sdk-platform-tools android-sdk-build-tools --yes
ENV ANDROID_HOME=/usr/lib/android-sdk
RUN wget --quiet https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip
RUN unzip sdk-tools-linux-3859397.zip
RUN mkdir -p ${ANDROID_HOME}/tools/
RUN rsync -rv tools/ ${ANDROID_HOME}/tools/
ENV PATH=${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin
RUN sdkmanager --update
RUN sdkmanager "platforms;android-26" "build-tools;26.0.2" "extras;google;m2repository" "extras;android;m2repository"
# ENV PATH=${PATH}:${ANDROID_HOME}/build-tools/26.0.2/
RUN yes | sdkmanager --licenses

RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -
RUN apt-get install nodejs --yes
# RUN npm install -g --unsafe-perm node-sass
RUN npm install -g ionic cordova

RUN wget --quiet https://services.gradle.org/distributions/gradle-4.4-bin.zip
RUN unzip gradle-4.4-bin.zip
RUN mv -f gradle-4.4 /opt/gradle-4.4
ENV GRADLE_HOME=/opt/gradle-4.4
ENV PATH=${PATH}:${GRADLE_HOME}/bin
