FROM ubuntu:18.04

RUN echo "Android SDK 28.0.3"

ENV ANDROID_HOME "/sdk"
ENV PATH "$PATH:${ANDROID_HOME}/tools"
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -qq update && \
    apt-get install -qqy --no-install-recommends \
      bzip2 \
      curl \
      git-core \
      git \
      html2text \
      openjdk-8-jdk \
      libc6-i386 \
      lib32stdc++6 \
      lib32gcc1 \
      lib32ncurses5 \
      lib32z1 \
      unzip \
      gcc \
      g++ \
      gettext \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN rm -f /etc/ssl/certs/java/cacerts; \
    /var/lib/dpkg/info/ca-certificates-java.postinst configure

# see https://developer.android.com/studio/#downloads for version code
RUN curl -s https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip > sdk.zip && \
    unzip sdk.zip -d ${ANDROID_HOME} && \
    rm -v sdk.zip

ADD packages.txt /sdk
RUN mkdir -p /root/.android && \
  touch /root/.android/repositories.cfg && \
  ${ANDROID_HOME}/tools/bin/sdkmanager --update 

RUN yes | ${ANDROID_HOME}/tools/bin/sdkmanager --licenses

RUN while read -r package; do PACKAGES="${PACKAGES}${package} "; done < /sdk/packages.txt && \
    ${ANDROID_HOME}/tools/bin/sdkmanager ${PACKAGES}

RUN yes | ${ANDROID_HOME}/tools/bin/sdkmanager --licenses

RUN echo "Installing Node.JS repo" \
	&& curl -sL https://deb.nodesource.com/setup_10.x | bash -

RUN echo "Installing Additional Libraries" \
	 && apt-get install -qqy --no-install-recommends nodejs wget

ENV GRADLE_HOME /opt/gradle
ENV GRADLE_VERSION 5.4.1

RUN echo "Downloading Gradle" \
	&& wget --no-verbose --output-document=gradle.zip "https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip"

RUN echo "Installing Gradle" \
	&& unzip gradle.zip \
	&& rm gradle.zip \
	&& mv "gradle-${GRADLE_VERSION}" "${GRADLE_HOME}/" \
	&& ln --symbolic "${GRADLE_HOME}/bin/gradle" /usr/bin/gradle

