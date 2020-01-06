FROM alapshin/android-build-env AS androidsdk

FROM openjdk:11

# Create jenkins user matching with master user
ARG user=jenkins
ARG group=jenkins
ARG uid=1000
ARG gid=1000

ENV HOME /home/${user}
RUN groupadd -g ${gid} ${group}
RUN useradd -c "Jenkins user" -d $HOME -u ${uid} -g ${gid} -m ${user}

# Set environment variables for Android SDK
ENV ANDROID_HOME /opt/android-sdk
ENV ANDROID_NDK_HOME ${ANDROID_HOME}/ndk-bundle

# Copy Android SDK from previous stage
COPY --from=androidsdk --chown=jenkins:jenkins $ANDROID_HOME $ANDROID_HOME

# Declare volume for Android SDK
VOLUME ${ANDROID_HOME}
