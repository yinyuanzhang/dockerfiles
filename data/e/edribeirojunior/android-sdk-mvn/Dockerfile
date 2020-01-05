# ====================================================================== #
# Android SDK Docker Image
# ====================================================================== #

# Base image
# ---------------------------------------------------------------------- #
FROM maven:3.6.0-jdk-8

# Author
# ---------------------------------------------------------------------- #
LABEL maintainer "edribeirojunior@gmail.com"

# support multiarch: i386 architecture
# install Java
# install essential tools
# install Qt
RUN dpkg --add-architecture i386 && \
    apt-get update -y && \
    apt-get install -y libncurses5:i386 libc6:i386 libstdc++6:i386 lib32gcc1 lib32ncurses5 lib32z1 zlib1g:i386 && \
    apt-get install -y --no-install-recommends openjdk-8-jdk && \
    apt-get install -y git wget zip && \
    apt-get install -y qt5-default

# download and install Android SDK
# https://developer.android.com/studio/#downloads
ARG ANDROID_SDK_VERSION=4333796
ARG ANDROID_COMPILE_SDK=19
ARG ANDROID_BUILD_TOOLS=28.0.3


RUN mkdir -p /opt/android-sdk && cd /opt/android-sdk && \
    wget -q https://dl.google.com/android/repository/sdk-tools-linux-${ANDROID_SDK_VERSION}.zip && \
    unzip *tools*linux*.zip && \
    rm *tools*linux*.zip && \
    wget -q https://dl.google.com/android/repository/tools_r25.2.5-linux.zip && \
    unzip -o tools_r25.2.5-linux.zip && \
    rm tools_*linux.zip && \
    echo "y" | tools/bin/sdkmanager "platforms;android-${ANDROID_COMPILE_SDK}" >/dev/null && \
    echo "y" | tools/bin/sdkmanager "platform-tools" >/dev/null && \
    echo "y" | tools/bin/sdkmanager "build-tools;${ANDROID_BUILD_TOOLS}" >/dev/null

# set the environment variables
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
ENV ANDROID_HOME /opt/android-sdk
ENV PATH ${PATH}:${ANDROID_HOME}/emulator:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools:${ANDROID_HOME}/tools/bin
ENV _JAVA_OPTIONS -XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap

# accept the license agreements of the SDK components
ADD license_accepter.sh /opt/
RUN /opt/license_accepter.sh $ANDROID_HOME

# install and configure SSH server
EXPOSE 22
ADD sshd-banner /etc/ssh/
ADD authorized_keys /tmp/
RUN apt-get update -y && \
    apt-get install -y openssh-server supervisor locales && \
    mkdir -p /var/run/sshd /var/log/supervisord && \
    locale-gen en en_US en_US.UTF-8 && \
    FILE_SSHD_CONFIG="/etc/ssh/sshd_config" && \
    echo "\nBanner /etc/ssh/sshd-banner" >> $FILE_SSHD_CONFIG && \
    echo "\nPermitUserEnvironment=yes" >> $FILE_SSHD_CONFIG && \
    ssh-keygen -q -N "" -f /root/.ssh/id_rsa && \
    FILE_SSH_ENV="/root/.ssh/environment" && \
    touch $FILE_SSH_ENV && chmod 600 $FILE_SSH_ENV && \
    printenv | grep "JAVA_HOME\|ANDROID_HOME\|LD_LIBRARY_PATH\|PATH" >> $FILE_SSH_ENV && \
    FILE_AUTH_KEYS="/root/.ssh/authorized_keys" && \
    touch $FILE_AUTH_KEYS && chmod 600 $FILE_AUTH_KEYS && \
    for file in /tmp/*.pub; \
    do if [ -f "$file" ]; then echo "\n" >> $FILE_AUTH_KEYS && cat $file >> $FILE_AUTH_KEYS && echo "\n" >> $FILE_AUTH_KEYS; fi; \
    done && \
    (rm /tmp/*.pub 2> /dev/null || true)

ADD supervisord.conf /etc/supervisor/conf.d/
CMD ["/usr/bin/supervisord"]
