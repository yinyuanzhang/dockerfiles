FROM ubuntu:18.04
ENV DEBIAN_FRONTEND noninteractive

# Fetching dependencies with apt
RUN apt-get update && \
    apt-get install -y \
        autoconf2.13 \
        build-essential \
        openjdk-8-jdk-headless \
        maven \
        python2.7 \
        python3 \
        rsync \
        unzip \
        wget \
        xz-utils \
        yasm \
        zip && \
        apt-get clean -y && \
        rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Installing maven installs also java10, but we need to use java8
RUN update-java-alternatives --jre-headless -s java-1.8.0-openjdk-amd64

ENV JAVA_TOOL_OPTIONS="-Dfile.encoding=UTF-8"

# Create the /sdk dir and install the Android dependencies
RUN mkdir /sdk; \
    cd /sdk; \
    wget --quiet "https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip" && \
    wget --quiet "https://dl.google.com/android/repository/android-ndk-r18b-linux-x86_64.zip" && \
    mkdir android-sdk && \
    cd android-sdk && \
    unzip ../sdk-tools-linux-4333796.zip && \
    cd tools/bin && \
    while true; do echo 'y'; done | ./sdkmanager --licenses && \
    ./sdkmanager \
        "platform-tools" \
        "build-tools;27.0.3" \
        "platforms;android-29" \
        "emulator" \
        "extras;android;m2repository" \
        "extras;google;m2repository" && \
    cd /sdk && \
    rm -f sdk-tools-linux-4333796.zip && \
    unzip android-ndk-r18b-linux-x86_64.zip && \
    rm -f android-ndk-r18b-linux-x86_64.zip

# Download dependencies from the web and unpack them
RUN cd /sdk && \
    for url in \
        "https://queue.taskcluster.net/v1/task/KnsfShKnS--AiV-EIhig9A/artifacts/public/build/node.tar.xz" \
        "https://queue.taskcluster.net/v1/task/LntQ_Kz_T_qdaDhjMRd8sQ/artifacts/public/build/nasm.tar.bz2" \
        "https://queue.taskcluster.net/v1/task/cJXQvHC0Q-2ng4dIsJHppw/artifacts/public/build/android-gradle-dependencies.tar.xz" \
        "https://queue.taskcluster.net/v1/task/a72HJnTIQ0CeWi-cRwMa4Q/artifacts/public/build/cbindgen.tar.xz" \
        "https://queue.taskcluster.net/v1/task/VkkosKAbQQObmuSNybdzdQ/artifacts/public/build/sccache.tar.xz" \
        "https://queue.taskcluster.net/v1/task/RoR5EZxVRLCQDiRm_7TB-Q/artifacts/public/build/clang.tar.xz" \
        "https://queue.taskcluster.net/v1/task/EkUKwsx-SlC4M9SqRuj7Zw/artifacts/public/build/rust-size.tar.xz" \
        "https://queue.taskcluster.net/v1/task/HguxIGnnSaGfu2PkeF0EEw/artifacts/public/build/rustc.tar.xz"; \
    do \
        package=`echo "${url}"|tr "/" "\n"|tail -1`; \
        echo "Installing ${package} from ${url}"; \
        wget --quiet "${url}" && \
        tar xf "${package}" && \
        rm -f "${package}" || \
        echo "Error installing ${package}"; \
    done

# Install extra aar to compile without MOZILLA_OFFICIAL=1
RUN mvn dependency:get \
        -Dmaven.repo.local=/sdk/android-gradle-dependencies/jcenter \
        -DremoteRepositories=jcenter::::https://jcenter.bintray.com \
        -DgroupId=com.squareup.leakcanary \
        -DartifactId=leakcanary-android-no-op \
        -Dversion=1.4-beta1 \
        -Dpackaging=aar && \
    mvn dependency:get \
        -Dmaven.repo.local=/sdk/android-gradle-dependencies/jcenter \
        -DremoteRepositories=jcenter::::https://jcenter.bintray.com \
        -DgroupId=com.squareup.leakcanary \
        -DartifactId=leakcanary-android \
        -Dversion=1.4-beta1 \
        -Dpackaging=aar

ENV SHELL=/bin/bash
ENV HOST_CC=clang
ENV PATH=/sdk/cbindgen:/sdk/clang/bin:/sdk/nasm:/sdk/node/bin:/sdk/rust-size:/sdk/rustc/bin:/sdk/sccache:$PATH
# Do not add empty spaces here, gradle will fail otherwise
ENV GRADLE_MAVEN_REPOSITORIES="file://sdk/android-gradle-dependencies/google,\
file://sdk/android-gradle-dependencies/jcenter,\
file://sdk/android-gradle-dependencies/gradle-plugins"
ENV ANDROID_HOME=/sdk/android-sdk
ENV ANDROID_NDK=/sdk/android-ndk-r18b
