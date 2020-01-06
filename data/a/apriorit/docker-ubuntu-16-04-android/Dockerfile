FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y apt-utils
RUN apt-get install -y curl
RUN apt-get install -y cmake
RUN apt-get install -y ant
RUN apt-get install -y zip unzip
RUN apt-get install -y file

RUN apt-get install nasm --yes
RUN apt-get install nano --yes
RUN apt-get install default-jdk --yes

RUN apt-get install lib32z1 --yes
RUN apt-get install lib32ncurses5 --yes

RUN dpkg --add-architecture i386
RUN apt-get update
RUN apt-get install -y lib32ncurses5 libbz2-1.0:i386 libstdc++6:i386 libfontconfig1:i386 libxext6:i386 libxrender1:i386 libgstreamer-plugins-base0.10-0:i386

RUN apt-get install lib32stdc++6 --yes

#Java 7, 8 install
RUN apt-get install software-properties-common --yes
RUN apt-get install python-software-properties --yes

RUN add-apt-repository ppa:openjdk-r/ppa --yes
RUN apt-get update
RUN apt-get install openjdk-7-jdk --yes
RUN apt-get install openjdk-7-jre --yes
RUN apt-get install openjdk-8-jdk --yes
RUN apt-get install openjdk-8-jre --yes

ENV NDK_URL_OLD="http://dl.google.com/android/repository/android-ndk-r10e-linux-x86_64.zip " \
    ANDROID_SDK="/usr/local/android-sdk-old" \
    JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 \
    SDK_URL="https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip" \
    NDK_URL="https://dl.google.com/android/repository/android-ndk-r16b-linux-x86_64.zip" \
    ANDROID_HOME="/usr/local/android-sdk" \
    ANDROID_VERSION=27 \
    ANDROID_BUILD_TOOLS_VERSION=27.0.3 \
    GIT_TF_URL="http://download.microsoft.com/download/A/E/2/AE23B059-5727-445B-91CC-15B7A078A7F4/git-tf-2.0.3.20131219.zip" \
    GIT_TF="/usr/git_tf" \
    PATH="$PATH:/usr/git_tf/git-tf-2.0.3.20131219"
	
# Download Android SDK

RUN mkdir "$ANDROID_SDK" .android ndk-bundle\
	&& cd "$ANDROID_SDK" \
	&& curl -O https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz \
	&& tar -xf android-sdk_r24.4.1-linux.tgz \
	&& cd android-sdk-linux

# All SDK components
RUN cd "$ANDROID_SDK" \
	&& cd android-sdk-linux \
    && ./tools/android list sdk --extended --no-ui --all
# Available SDK targets
RUN echo ----------------------------------------------------------- && cd "$ANDROID_SDK" && cd android-sdk-linux &&  ./tools/android list targets

# Install latest android tools and system images
RUN cd "$ANDROID_SDK" && cd android-sdk-linux &&  echo "y" |  ./tools/android update sdk --filter tools --no-ui --force
RUN cd "$ANDROID_SDK" && cd android-sdk-linux &&  echo "y" |  ./tools/android update sdk --filter platform-tools --no-ui --force

RUN cd "$ANDROID_SDK" && cd android-sdk-linux &&  echo "y" | ./tools/android update sdk --filter build-tools-22.0.1 --no-ui -a
RUN cd "$ANDROID_SDK" && cd android-sdk-linux &&  echo "y" | ./tools/android update sdk --filter build-tools-24.0.3 --no-ui -a
RUN cd "$ANDROID_SDK" && cd android-sdk-linux &&  echo "y" | ./tools/android update sdk --filter android-18 --no-ui -a
RUN cd "$ANDROID_SDK" && cd android-sdk-linux &&  echo "y" | ./tools/android update sdk --filter android-19 --no-ui -a
RUN cd "$ANDROID_SDK" && cd android-sdk-linux &&  echo "y" | ./tools/android update sdk --filter android-20 --no-ui -a
RUN cd "$ANDROID_SDK" && cd android-sdk-linux &&  echo "y" | ./tools/android update sdk --filter android-21 --no-ui -a
RUN cd "$ANDROID_SDK" && cd android-sdk-linux &&  echo "y" | ./tools/android update sdk --filter android-22 --no-ui -a

# Available SDK targets
RUN  cd "$ANDROID_SDK" && cd android-sdk-linux &&  ./tools/android list targets

RUN cd $ANDROID_SDK \
	&& mv  -v $ANDROID_SDK/android-sdk-linux/* $ANDROID_SDK/ \
	&& rmdir $ANDROID_SDK/android-sdk-linux/   \
	&& cp $ANDROID_SDK/build-tools/22.0.1/zipalign $ANDROID_SDK/tools \
	&& rm android-sdk_r24.4.1-linux.tgz 	
	
#Install Android NDK for SDK
RUN cd "$ANDROID_SDK" \
	&& ls \
	&& mkdir ndk-r10e \
	&& cd ndk-r10e \
	&& curl -o ndk.zip $NDK_URL_OLD \
	&& unzip ndk.zip \
	&& rm ndk.zip \
	&& mv  -v $ANDROID_SDK/ndk-r10e/android-ndk-r10e/* $ANDROID_SDK/ndk-r10e/ \
	&& rmdir $ANDROID_SDK/ndk-r10e/android-ndk-r10e/

#Building NDK Toolchains
RUN /bin/bash -c "$ANDROID_SDK/ndk-r10e/build/tools/make-standalone-toolchain.sh --arch=arm --platform=android-18 --install-dir=android-arm-toolchain"
RUN /bin/bash -c "$ANDROID_SDK/ndk-r10e/build/tools/make-standalone-toolchain.sh --arch=arm64 --platform=android-21 --install-dir=android-arm64-toolchain"
RUN /bin/bash -c "$ANDROID_SDK/ndk-r10e/build/tools/make-standalone-toolchain.sh --arch=x86_64 --platform=android-21 --install-dir=android-x86_64-toolchain"
RUN /bin/bash -c "$ANDROID_SDK/ndk-r10e/build/tools/make-standalone-toolchain.sh --arch=x86 --platform=android-18 --install-dir=android-x86-toolchain"
RUN /bin/bash -c "$ANDROID_SDK/ndk-r10e/build/tools/make-standalone-toolchain.sh --arch=mips --platform=android-18 --install-dir=android-mips-toolchain"

RUN echo "------------------------------------- NEW SDK and NDK ------------------------------------------------"

RUN	mkdir "$ANDROID_HOME"  \
    && cd "$ANDROID_HOME" \
    && curl -o sdk.zip $SDK_URL \
    && unzip sdk.zip \
    && rm sdk.zip \
    && yes | $ANDROID_HOME/tools/bin/sdkmanager --licenses

# Install Android Build Tool and Libraries
RUN $ANDROID_HOME/tools/bin/sdkmanager --update
RUN $ANDROID_HOME/tools/bin/sdkmanager "build-tools;${ANDROID_BUILD_TOOLS_VERSION}" \
    "platforms;android-${ANDROID_VERSION}" \
    "platform-tools"

#Install Android NDK
RUN cd "$ANDROID_HOME" \
	&& ls \
	&& mkdir ndk-bundle \
	&& cd ndk-bundle \
	&& curl -o ndk.zip $NDK_URL \
	&& unzip ndk.zip \
	&& rm ndk.zip \
	&& mv  -v $ANDROID_HOME/ndk-bundle/android-ndk-r16b/* $ANDROID_HOME/ndk-bundle/ \
	&& rmdir $ANDROID_HOME/ndk-bundle/android-ndk-r16b/  


#Install Git
RUN apt-get install -y git

#Install Git TF
RUN mkdir "$GIT_TF" \
		&& cd "$GIT_TF"  \
        && curl -o git_tf.zip $GIT_TF_URL \
        &&  unzip git_tf.zip \
        && rm git_tf.zip
RUN git tf --version

RUN mkdir /source
WORKDIR /source
