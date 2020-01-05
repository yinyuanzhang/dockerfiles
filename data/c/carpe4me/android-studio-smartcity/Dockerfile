# ====================================================================== #
# SEC Android Package Development Docker Image
# http://mobilerndhub.sec.samsung.net/wiki/pages/viewpage.action?pageId=116859078
# ====================================================================== #

# ====================================================================== #
# Base image 설정
FROM ubuntu:18.04

# ====================================================================== #
# Author
LABEL maintainer KIM WAN SEOK "carpe4me@gmail.com"

# ====================================================================== #
## Install Essential tools
# support multiarch: i386 architecture
# install 32bit library 참고: 64비트 버전의 Ubuntu를 실행하는 경우, 다음 명령으로 일부 32비트 라이브러리를 설치해야 합니다.
#                             (https://developer.android.com/studio/install)
# install Java
# install essential tools
# install Qt
# Clean up
RUN dpkg --add-architecture i386 \
    && apt-get update -y \
    && apt-get install -y --no-install-recommends \
        libncurses5:i386 libc6:i386 libstdc++6:i386 zlib1g:i386 lib32z1 lib32ncurses5 lib32stdc++6 lib32gcc1 \
        git wget zip unzip vim sudo curl gpg gnupg2 openssh-server \
        qt5-default \
        openjdk-8-jdk \
    && apt-get clean \
    && apt-get purge \
    && rm -rf /var/lib/apt/lists/*

# ====================================================================== #
# Add smartCity.cert
ADD smartCity.crt /root
RUN cp /root/smartCity.crt /usr/local/share/ca-certificates/ && \
	update-ca-certificates

# ====================================================================== #
# Network Proxy Configuration (http://mobilerndhub.sec.samsung.net/wiki/display/DP/UBUNTU+14.04+Desktop+amd64)
# Inotify Watches Limit (https://confluence.jetbrains.com/display/IDEADEV/Inotify+Watches+Limit)
RUN echo 'http_proxy="http://168.219.61.252:8080"' >> /etc/environment && \
    echo 'https_proxy="http://168.219.61.252:8080"' >> /etc/environment && \
    echo 'ftp_proxy="ftp://168.219.61.252:8080"' >> /etc/environment && \
    echo 'socks_proxy="socks://168.219.61.252:8080"' >> /etc/environment \
    echo 'no_proxy="sec.samsung.net,165.213.180.100,localhost,127.0.0.1"' >> /etc/environment \
    echo 'fs.inotify.max_user_watches = 524288' >> /etc/sysctl.conf
#    echo 'proxy = http://168.219.61.252:8080' >> /root/.curlrc && \

# ======================================================================== #
# 개발자 Font 추가
# [D2Coding] https://github.com/naver/d2codingfont/releases
# [Bitstream Vera Sans Mono] http://ftp.gnome.org/pub/GNOME/sources/ttf-bitstream-vera/1.10/
RUN wget -q https://github.com/naver/d2codingfont/releases/download/VER1.3.2/D2Coding-Ver1.3.2-20180524.zip && \
    mkdir -p /usr/share/fonts/truetype/D2Coding && \
    unzip D2Coding-*.zip -d /usr/share/fonts/truetype/D2Coding && \
    wget -q http://ftp.gnome.org/pub/GNOME/sources/ttf-bitstream-vera/1.10/ttf-bitstream-vera-1.10.zip &&\
    mkdir -p /usr/share/fonts/truetype/ttf-bitstream-vera && \
    unzip ttf-bitstream-vera*.zip -d /usr/share/fonts/truetype/ttf-bitstream-vera &&\
    fc-cache -f -v &&\
    rm -f /tmp/D2Coding-Ver*.zip &&\
    rm -f /tmp/ttf-bitstream-vera-*.zip
# ------------------------------------------------------------------------ #

# ======================================================================== #
# Jenkins Configuration
ARG user=jenkins
ARG group=jenkins
ARG uid=1000
ARG gid=1000
ARG http_port=8080
ARG agent_port=50000
ARG JENKINS_HOME=/var/jenkins_home

ENV JENKINS_HOME $JENKINS_HOME
ENV JENKINS_SLAVE_AGENT_PORT ${agent_port}

# Jenkins is run with user `jenkins`, uid = 1000
# If you bind mount a volume from the host or a data container,
# ensure you use the same uid
RUN mkdir -p $JENKINS_HOME \
  && chown ${uid}:${gid} $JENKINS_HOME \
  && groupadd -g ${gid} ${group} \
  && useradd -d "$JENKINS_HOME" -u ${uid} -g ${gid} -m -s /bin/bash ${user}

# Jenkins home directory is a volume, so configuration and build history
# can be persisted and survive image upgrades
VOLUME $JENKINS_HOME

# `/usr/share/jenkins/ref/` contains all reference configuration we want
# to set on a fresh new installation. Use it to bundle additional plugins
# or config file with your custom jenkins Docker image.
RUN mkdir -p /usr/share/jenkins/ref/init.groovy.d

# Use tini as subreaper in Docker container to adopt zombie processes
ARG TINI_VERSION=v0.16.1
COPY tini_pub.gpg ${JENKINS_HOME}/tini_pub.gpg
RUN curl -fsSL https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-static-$(dpkg --print-architecture) -o /sbin/tini \
  && curl -fsSL https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-static-$(dpkg --print-architecture).asc -o /sbin/tini.asc \
  && gpg --no-tty --import ${JENKINS_HOME}/tini_pub.gpg \
  && gpg --verify /sbin/tini.asc \
  && rm -rf /sbin/tini.asc /root/.gnupg \
  && chmod +x /sbin/tini

COPY init.groovy /usr/share/jenkins/ref/init.groovy.d/tcp-slave-agent-port.groovy

# jenkins version being bundled in this docker image
ARG JENKINS_VERSION
ENV JENKINS_VERSION ${JENKINS_VERSION:-2.150.1}

# jenkins.war checksum, download will be validated using it
# http://mirrors.jenkins.io/war-stable/2.150.1/jenkins.war.sha256
ARG JENKINS_SHA=7a38586d5a3a1a83498809a83715728bb2f01b58a7dd3a88366f076efdaf6669

# Can be used to customize where jenkins.war get downloaded from
ARG JENKINS_URL=https://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war

# could use ADD but this one does not check Last-Modified header neither does it allow to control checksum
# see https://github.com/docker/docker/issues/8331
RUN curl -fsSL ${JENKINS_URL} -o /usr/share/jenkins/jenkins.war \
  && echo "${JENKINS_SHA}  /usr/share/jenkins/jenkins.war" | sha256sum -c -

ENV JENKINS_UC https://updates.jenkins.io
ENV JENKINS_UC_EXPERIMENTAL=https://updates.jenkins.io/experimental
ENV JENKINS_INCREMENTALS_REPO_MIRROR=https://repo.jenkins-ci.org/incrementals
RUN chown -R ${user} "$JENKINS_HOME" /usr/share/jenkins/ref

# for main web interface:
EXPOSE ${http_port}

# will be used by attached slave agents:
EXPOSE ${agent_port}

ENV COPY_REFERENCE_FILE_LOG $JENKINS_HOME/copy_reference_file.log

######################################################################
# https://engineering.riotgames.com/news/docker-jenkins-data-persists
RUN mkdir /var/log/${user}
RUN chown -R  ${user}:${group}  /var/log/${user}

RUN mkdir /var/cache/${user}
RUN chown -R ${user}:${group} /var/cache/${user}

# Set default options
ENV JAVA_OPTS="-Xmx8192m"
ENV JENKINS_OPTS="--handlerCountMax=300 --logfile=/var/log/jenkins/jenkins.log --webroot=/var/cache/jenkins/war"
######################################################################

# ======================================================================== #
ENV HOME_DIR=$JENKINS_HOME \
    TOOL_DIR=/opt

RUN chown -R ${user}:${group} $TOOL_DIR

WORKDIR ${TOOL_DIR}
USER ${user}
# ======================================================================== #
# Gradle configuration
ENV GRADLE_VERSION=4.5.1
ENV GRADLE_HOME=$TOOL_DIR/gradle/gradle-$GRADLE_VERSION \
     GRADLE_USER_HOME=$HOME_DIR/tools_build/gradle
ENV PATH=${PATH}:${GRADLE_HOME}/bin

#VOLUME $GRADLE_USER_HOME

RUN wget https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip && \
    unzip gradle*.zip -d $TOOL_DIR/gradle && \
    mkdir -p $GRADLE_USER_HOME && \
    rm gradle*.zip 

### http://mobilerndhub.sec.samsung.net/wiki/pages/viewpage.action?pageId=112754956
# gradle.properties & init.gradle 설정
COPY --chown=1000:1000 gradle.properties init.gradle $GRADLE_USER_HOME/
# ------------------------------------------------------------------------ #

# ====================================================================== #
# Kotlin compiler configuration
ENV KOTLIN_VERSION=1.2.50 \
    KOTLIN_HOME=$TOOL_DIR/kotlinc
ENV PATH=${PATH}:${KOTLIN_HOME}/bin

RUN wget https://github.com/JetBrains/kotlin/releases/download/v${KOTLIN_VERSION}/kotlin-compiler-${KOTLIN_VERSION}.zip && \
    unzip *kotlin*.zip -d $TOOL_DIR/ && \
    rm kotlin-compiler-*.zip
# ------------------------------------------------------------------------ #

# ======================================================================== #
# Install Android SDK
ENV ANDROID_SDK_VERSION=4333796 \
    ANDROID_HOME=$TOOL_DIR/android-sdk
ENV PATH=${PATH}:${ANDROID_HOME}/emulator:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools:${ANDROID_HOME}/tools/bin

RUN wget https://dl.google.com/android/repository/sdk-tools-linux-${ANDROID_SDK_VERSION}.zip && \
    mkdir -p $ANDROID_HOME &&\
    unzip *tools*linux*.zip -d $ANDROID_HOME && \
    chmod -R a+w ${ANDROID_HOME} && \
    rm *tools*linux*.zip

# setup adb server
EXPOSE 5037
# ------------------------------------------------------------------------ #

## ======================================================================== #
## https://developer.android.com/studio/archive
## Android Studio v3.1.4
#ENV ANDROID_STUDIO=$TOOL_DIR/android-studio \
#    STUDIO_CONFIG_HOME=$USER_HOME/.AndroidStudio3.1
#ENV PATH=${PATH}:${ANDROID_STUDIO}/bin
#
#RUN wget https://dl.google.com/dl/android/studio/ide-zips/3.1.4.0/android-studio-ide-173.4907809-linux.zip && \
#    unzip android-studio-ide-*.zip -d $TOOL_DIR && \
#    rm android-studio-ide-*.zip &&\
#    mkdir -p $HOME_DIR/${STUDIO_CONFIG_HOME}/config/options
#
## Add the proxy settings for Android Studio
#COPY --chown=1000:1000 proxy.settings.xml $HOME_DIR/${STUDIO_CONFIG_HOME}/config/options
#COPY --chown=1000:1000 studio64.vmoptions $HOME_DIR/${STUDIO_CONFIG_HOME}/config
# ------------------------------------------------------------------------ #

# ======================================================================== #
# Set the environment variables
ENV JAVA_HOME "/usr/lib/jvm/java-8-openjdk-amd64"
COPY --chown=1000:1000 .bashrc $HOME_DIR

# ======================================================================== #
# Update SDKManager
ENV SDK_PROXY "--no_https --proxy=http --proxy_host=168.219.61.252 --proxy_port=8080"

RUN mkdir ~/.android && \
    echo '### User Sources for Android SDK Manager' > ~/.android/repositories.cfg && \
    sdkmanager --update && yes | sdkmanager --licenses 
#    sdkmanager --update $SDK_PROXY && yes | sdkmanager --licenses $SDK_PROXY

# Update SDK manager and install system image, platform and build tools
RUN sdkmanager \
  "tools" \
  "platform-tools" \
  "emulator" \
  "extras;android;m2repository" \
  "extras;google;m2repository" \
  "extras;google;google_play_services" \
  "build-tools;26.0.1" \
  "build-tools;27.0.3" \
  "build-tools;28.0.0" \
  "build-tools;28.0.3" \
  "sources;android-28" \
  "platforms;android-28" 
#  $SDK_PROXY
# ------------------------------------------------------------------------ #
WORKDIR ${HOME_DIR}

COPY jenkins-support /usr/local/bin/jenkins-support
COPY jenkins.sh /usr/local/bin/jenkins.sh
COPY tini-shim.sh /bin/tini
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/jenkins.sh"]

# from a derived Dockerfile, can use `RUN plugins.sh active.txt` to setup /usr/share/jenkins/ref/plugins from a support bundle
COPY plugins.sh /usr/local/bin/plugins.sh
COPY install-plugins.sh /usr/local/bin/install-plugins.sh
