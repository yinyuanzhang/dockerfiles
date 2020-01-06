FROM node:8

ENV ANDROID_HOME /opt/android-sdk-linux
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools
ENV PATH ${PATH}:/opt/tools

RUN dpkg --add-architecture i386
RUN apt-get -qqy update && apt-get -qqy install -y curl wget libncurses5:i386 libstdc++6:i386 zlib1g:i386 unzip

RUN cd /opt && wget -q --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u191-b12/2787e4a523244c269598db4e85c51e0c/jdk-8u191-linux-x64.tar.gz"
RUN cd /opt && tar xvzf jdk-8u191-linux-x64.tar.gz
RUN cd /opt/jdk1.8.0_191 && update-alternatives --install /usr/bin/java java /opt/jdk1.8.0_191/bin/java 2 && update-alternatives --config java
RUN cd /opt/jdk1.8.0_191 && update-alternatives --install /usr/bin/javac javac /opt/jdk1.8.0_191/bin/javac 2 && update-alternatives --config javac
RUN cd /opt && rm jdk-8u191-linux-x64.tar.gz

RUN cd /opt && wget -q https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip -O android-sdk.zip
RUN cd /opt && unzip -q android-sdk.zip && rm -f android-sdk.zip
RUN cd /opt  \
   && echo y | tools/bin/sdkmanager "platforms;android-25" "build-tools;27.0.3" "extras;google;m2repository" "extras;android;m2repository" \
   && echo y | tools/bin/sdkmanager "platforms;android-26" "build-tools;28.0.0" "extras;google;m2repository" "extras;android;m2repository" \
   && echo y | tools/bin/sdkmanager "build-tools;23.0.3" "build-tools;28.0.2" "build-tools;26.0.3"

RUN cd /opt && mkdir android-sdk-linux && mv tools android-sdk-linux/
RUN chown -R 1000:1000 $ANDROID_HOME
RUN yes | /opt/android-sdk-linux/tools/bin/sdkmanager --licenses

RUN npm install -g yarn react-native-cli

RUN apt-get clean

VOLUME ["/opt/android-sdk-linux"]
