FROM frolvlad/alpine-glibc:alpine-3.10

RUN apk add --no-cache \
  openjdk8 \
  bash \
  unzip

ENV JAVA8_HOME /usr/lib/jvm/java-1.8-openjdk
ENV JAVA_HOME $JAVA8_HOME
ENV PATH $PATH:$JAVA_HOME/bin

ENV ANDROID_SDK_FILE sdk-tools-linux-4333796.zip
ENV ANDROID_SDK_URL https://dl.google.com/android/repository/${ANDROID_SDK_FILE}
ENV ANDROID_HOME /opt/android-sdk-linux
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:${ANDROID_HOME}/platform-tools

RUN mkdir -p ${ANDROID_HOME} && cd ${ANDROID_HOME} && \
  echo "Wget'ing ${ANDROID_SDK_URL} ..." && \
  wget -q ${ANDROID_SDK_URL} && \
  unzip ${ANDROID_SDK_FILE} && \
  rm ${ANDROID_SDK_FILE} && \
  yes | sdkmanager --channel=3 tools platform-tools \
    "platforms;android-29" \
    "build-tools;29.0.2" && \
  bash -c "rm -rf ${ANDROID_HOME}/tools/lib/{,monitor-}x86" && \
  mkdir -p ~/.gradle && echo "org.gradle.daemon=false" >> ~/.gradle/gradle.properties
