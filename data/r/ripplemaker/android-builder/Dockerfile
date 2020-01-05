FROM openjdk:8

# Everything will be installed in the directory but jdk.
ENV SDK_HOME /usr/local

# Download and unzip Android SDK
ENV ANDROID_HOME ${SDK_HOME}/android-sdk-linux
ENV ANDROID_SDK ${SDK_HOME}/android-sdk-linux
ENV ANDROID_SDK_MANAGER ${SDK_HOME}/android-sdk-linux/tools/bin/sdkmanager

ENV ANDROID_SDK_VERSION sdk-tools-linux-3859397.zip
ENV ANDROID_SDK_URL https://dl.google.com/android/repository/${ANDROID_SDK_VERSION}
RUN curl -sSL "${ANDROID_SDK_URL}" -o ${ANDROID_SDK_VERSION} \
    && unzip ${ANDROID_SDK_VERSION} -d ${ANDROID_HOME} \
  && rm -rf ${ANDROID_SDK_VERSION}
  
ENV PATH ${ANDROID_HOME}/tools:${ANDROID_HOME}/tools/bin:$ANDROID_HOME/platform-tools:$PATH
RUN (while sleep 3; do echo "y"; done) | sdkmanager --update && (while sleep 3; do echo "y"; done) | sdkmanager --licenses

# Install Android SDK Components
ENV ANDROID_COMPONENTS "tools" \
                       "platform-tools" \
                       "build-tools;23.0.2" \
                       "platforms;android-23" 

RUN mkdir -p ${ANDROID_HOME}/licenses/ && \
    echo "8933bad161af4178b1185d1a37fbf41ea5269c55" > ${ANDROID_HOME}/licenses/android-sdk-license && \
    echo "d56f5187479451eabf01fb78af6dfcb131a6481e" >> ${ANDROID_HOME}/licenses/android-sdk-license && \
    echo "84831b9409646a918e30573bab4c9c91346d8abd" > ${ANDROID_HOME}/licenses/android-sdk-preview-license && \
    (while sleep 3; do echo "y"; done) | ${ANDROID_SDK_MANAGER}  ${ANDROID_COMPONENTS} 

ENV ANDROID_NDK_COMPONENTS "lldb;3.1" \
                           "cmake;3.6.4111459"                                                  
RUN (while sleep 3; do echo "y"; done) | ${ANDROID_SDK_MANAGER} ${ANDROID_NDK_COMPONENTS}  

#Install Ndk ver 14
ENV ANDROID_NDK_VERSION r14b
ENV ANDROID_NDK_URL http://dl.google.com/android/repository/android-ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip
RUN curl -L "${ANDROID_NDK_URL}" -o android-ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip  \
  && unzip android-ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip -d ${ANDROID_SDK}  \
  && rm -rf android-ndk-${ANDROID_NDK_VERSION}-linux-x86_64.zip

ENV ANDROID_NDK_HOME ${ANDROID_SDK}/android-ndk-${ANDROID_NDK_VERSION}
ENV PATH ${ANDROID_NDK_HOME}:$PATH


# Install GNU-make and LLVM 
#RUN apt-get -yq update &&\
#    apt-get -y install make
RUN wget http://llvm.org/apt/llvm-snapshot.gpg.key 
RUN apt-key add llvm-snapshot.gpg.key 
RUN apt-get update -qq -y
RUN apt-get install -qq -y \
    file \
    make \
    clang \
    lldb \
    build-essential



