FROM microsoft/vsts-agent:ubuntu-16.04

MAINTAINER Alexandre Machado <agmachado@mmstech.com.br>

# Install basic command-line utilities
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    curl \
    dnsutils \
    file \
    ftp \
    iproute2 \
    iputils-ping \
    locales \
    openssh-client \
    rsync\
    shellcheck \
    sudo \
    telnet \
    time \
    unzip \
    wget \
    zip \
    tzdata \
	vim \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && rm -rf /etc/apt/sources.list.d/*

# Setup the locale
ENV LANG en_US.UTF-8
ENV LC_ALL ${LANG}
RUN locale-gen ${LANG} \
 && update-locale

# Accept EULA - needed for certain Microsoft packages like SQL Server Client Tools
ENV ACCEPT_EULA=Y

# Install essential build tools
RUN apt-get update \
 && apt-get install -y --no-install-recommends build-essential \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && rm -rf /etc/apt/sources.list.d/*

# Install Java Oracle JDK 8
RUN apt-get update -y \
 && apt-get install -y dos2unix software-properties-common curl \
 && add-apt-repository ppa:webupd8team/java -y \
 && apt-get update -y \
 && echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections \
 && apt-get install -y oracle-java8-set-default \ 
 && apt-get remove software-properties-common -y \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && rm -rf /etc/apt/sources.list.d/*
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# Install Java Tools (Ant, Maven)
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    ant \
    ant-optional \
    maven \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && rm -rf /etc/apt/sources.list.d/*
ENV ANT_HOME=/usr/share/ant \
    M2_HOME=/usr/share/maven

# Installs Android SDK
ENV ANDROID_SDK_VERSION 4333796
ENV ANDROID_BUILD_TOOLS_VERSION 28.0.3

# Installs i386 architecture required for running 32 bit Android tools
RUN dpkg --add-architecture i386 \
 && apt-get update -y \
 && apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386 lib32z1 unzip \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && rm -rf /etc/apt/sources.list.d/*

ENV ANDROID_SDK_FILENAME sdk-tools-linux-${ANDROID_SDK_VERSION}.zip
ENV ANDROID_SDK_URL https://dl.google.com/android/repository/${ANDROID_SDK_FILENAME}
ENV ANDROID_API_LEVELS android-23,android-24,android-25,android-26,android-27,android-28
ENV ANDROID_HOME /opt/sdk
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools
RUN mkdir -p ${ANDROID_HOME} \
 && cd /opt \
 && wget -q ${ANDROID_SDK_URL} \
 && wget -q https://dl.google.com/android/repository/tools_r25.2.3-linux.zip \
 && unzip ${ANDROID_SDK_FILENAME} -d ${ANDROID_HOME} \
 && unzip tools_r25.2.3-linux.zip tools/templates/* -d ${ANDROID_HOME} \
 && rm ${ANDROID_SDK_FILENAME} \
 && rm tools_r25.2.3-linux.zip \
 && yes | android update sdk --no-ui -a --filter tools,platform-tools,${ANDROID_API_LEVELS},build-tools-${ANDROID_BUILD_TOOLS_VERSION}	

# Install LTS Node.js and related tools
RUN curl -sL https://git.io/n-install | bash -s -- -ny - \
 && ~/n/bin/n lts \
 && npm install -g grunt \
 && npm install -g gulp \
 && npm install -g n \
 && npm install -g webpack webpack-cli --save-dev \
 && npm install -g parcel-bundler \
 && npm i -g npm \
 && rm -rf ~/n
ENV grunt=/usr/local/bin/grunt 

# Installs Cordova
# Forces a platform add in order to preload libraries
RUN npm install -g cordova@~6.4.0 \
 && cordova telemetry on

# Clean system
RUN apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && rm -rf /etc/apt/sources.list.d/*