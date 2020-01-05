#
# GitLab CI-CD testfairy: Android v1.2
#
# Original Source
# https://hub.docker.com/r/jangrewe/gitlab-ci-android/
# https://git.faked.org/jan/gitlab-ci-android
#
# Source
# https://hub.docker.com/r/faerulsalamun/gitlab-ci-cd-testfairy-android
# https://github.com/faerulsalamun/gitlab-ci-cd-testfairy-android

FROM ubuntu:16.04
MAINTAINER Jan Grewe <jan@faked.org>, Faerul Salamun <faerulsalamun@gmail.com>

ENV VERSION_SDK_TOOLS "25.2.2"
ENV VERSION_BUILD_TOOLS "24.0.3"
ENV VERSION_TARGET_SDK "24"

ENV SDK_PACKAGES "build-tools-${VERSION_BUILD_TOOLS},android-${VERSION_TARGET_SDK},addon-google_apis-google-${VERSION_TARGET_SDK},platform-tools,extra-android-m2repository,extra-android-support,extra-google-google_play_services,extra-google-m2repository"

ENV ANDROID_HOME "/sdk"
ENV PATH "$PATH:${ANDROID_HOME}/tools"
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -qq update && \
    apt-get install -qqy --no-install-recommends \
      curl \
      html2text \
      openjdk-8-jdk \
      libc6-i386 \
      lib32stdc++6 \
      lib32gcc1 \
      lib32ncurses5 \
      lib32z1 \
      unzip \
      zip \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN rm -f /etc/ssl/certs/java/cacerts; \
    /var/lib/dpkg/info/ca-certificates-java.postinst configure

RUN curl -s http://dl.google.com/android/repository/tools_r${VERSION_SDK_TOOLS}-linux.zip > /tools.zip && \
    unzip /tools.zip -d /sdk && \
    rm -v /tools.zip

RUN mkdir -p $ANDROID_HOME/licenses/ \
  && echo "8933bad161af4178b1185d1a37fbf41ea5269c55" > $ANDROID_HOME/licenses/android-sdk-license \
  && echo "84831b9409646a918e30573bab4c9c91346d8abd" > $ANDROID_HOME/licenses/android-sdk-preview-license


#ENV for test fairy for CD
ENV CURL_POSITION "/usr/bin/curl"
ENV ZIP_POSITION "/usr/bin/zip"
ENV KEYTOOL_POSITION "/usr/bin/keytool"
ENV ZIPALIGN_POSITION "/sdk/build-tools/24.0.3/zipalign"
ENV JARSIGNER_POSITION "/usr/bin/jarsigner"

# Download testfairy for deployment
COPY testfairy.sh /home
COPY testfairy.jks /home

RUN (while [ 1 ]; do sleep 5; echo y; done) | ${ANDROID_HOME}/tools/android update sdk -u -a -t ${SDK_PACKAGES}
