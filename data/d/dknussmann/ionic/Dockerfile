FROM ubuntu:16.04

ENV ANDROID_HOME="/var/opt/android"
ENV PATH="/var/opt/gradle/4.10.3/bin:/var/opt/android/tools:/var/opt/android/tools/bin:/var/opt/android/platform-tools:/var/opt/android/platform-tools/bin:${PATH}:/home/node/.npm-global/bin"

RUN apt-get update

RUN apt-get install -y curl git software-properties-common unzip zipalign

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g npm cordova ionic

RUN apt-get update
RUN yes | apt-get install openjdk-8-jdk
RUN update-alternatives --config java
RUN update-alternatives --config javac
RUN java -version
RUN javac -version

WORKDIR /var/opt

RUN curl -o sdk-tools.zip https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip
RUN unzip sdk-tools.zip -d android
RUN mkdir -p  /root/.android/
RUN touch /root/.android/repositories.cfg

RUN yes | sdkmanager "build-tools;29.0.2"
RUN yes | sdkmanager "platforms;android-28"
RUN yes | sdkmanager "extras;google;google_play_services"
RUN yes | sdkmanager --update
RUN sdkmanager "tools"
RUN yes | sdkmanager --licenses

RUN curl -o gradle-4.10.3-bin.zip https://downloads.gradle.org/distributions/gradle-4.10.3-bin.zip
RUN unzip gradle-4.10.3-bin.zip -d gradle
RUN mv gradle/gradle-4.10.3 gradle/4.10.3

WORKDIR /root