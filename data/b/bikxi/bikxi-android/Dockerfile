FROM ruby:2.5.0

ENV SDK_TOOLS_VERSION=3859397 \
    COMPILE_SDK_VERSION=25 \
    BUILD_TOOLS_VERSION=26.0.2

ENV BUILD_PATH=/build
ENV ANDROID_HOME="$BUILD_PATH/vendor/android-sdk"
ENV SDK_TOOLS_ZIP="sdk-tools-linux-$SDK_TOOLS_VERSION.zip" \
    PATH="$ANDROID_HOME/tools/bin:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$PATH" \
    JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64/" \
    JAVA_OPTS="-Xms4096m -Xmx4096m" \
    GRADLE_OPTS="-XX:+UseG1GC -XX:MaxGCPauseMillis=1000" \
    LANG="en_US.UTF-8" \
    LC_ALL="en_US.UTF-8"

WORKDIR $BUILD_PATH

# Install java and unzip
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    openjdk-8-jdk \
    unzip && \
    apt-get clean

RUN mkdir -p $ANDROID_HOME
RUN wget -q https://dl.google.com/android/repository/$SDK_TOOLS_ZIP && \
    unzip -q $SDK_TOOLS_ZIP -d $ANDROID_HOME && \
    rm $SDK_TOOLS_ZIP

# http://stackoverflow.com/questions/38096225/automatically-accept-all-sdk-licences
RUN mkdir -p "$ANDROID_HOME/licenses" && \
echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" > "$ANDROID_HOME/licenses/android-sdk-license" && \
echo -e "\nd56f5187479451eabf01fb78af6dfcb131a6481e" > "$ANDROID_HOME/licenses/android-sdk-license" && \
echo -e "\n84831b9409646a918e30573bab4c9c91346d8abd" > "$ANDROID_HOME/licenses/android-sdk-preview-license"

# Install Android tools
RUN sdkmanager "platforms;android-$COMPILE_SDK_VERSION" "platform-tools" "build-tools;$BUILD_TOOLS_VERSION"

WORKDIR /project
