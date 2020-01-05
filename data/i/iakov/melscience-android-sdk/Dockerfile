FROM runmymind/docker-android-sdk:latest
MAINTAINER jake.kirilenko@gmail.com
ENV _JAVA_OPTIONS="-Xmx3000m -XX:ParallelGCThreads=2 -XX:ConcGCThreads=2 -XX:ParallelGCThreads=2 -Djava.util.concurrent.ForkJoinPool.common.parallelism=2"

ENV PATH="/opt/android-sdk-linux/platform-tools:/opt/android-sdk-linux/tools/bin:/opt/android-sdk-linux/tools:/opt/android-sdk-linux/bin:/usr/local/bin:$PATH"

RUN apt-get update && apt-get full-upgrade -y \
&& apt-get install -y openssh-client valgrind cmake g++ zlib1g-dev libglib2.0-dev libjpeg-dev\
#seems like for 'artful' next line is not required
#git-lfs now can be installed directly from the 'universe' repo
&& curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash \
&& apt-get install git-lfs \
&& sdkmanager \
               "tools" \
               "ndk-bundle" \
               "platforms;android-28" \
               "cmake;3.10.2.4988404" \
               "lldb;3.1" \
               "platform-tools" \
               "build-tools;27.0.3" \
  && sdkmanager --update
#RUN sdkmanager \
    #"system-images;android-24;google_apis;armeabi-v7a" \
    #"system-images;android-19;google_apis;armeabi-v7a" \
    #"emulator" \

#RUN echo no | avdmanager create avd -n testEmulator24 -k "system-images;android-24;google_apis;armeabi-v7a"
#RUN echo no | avdmanager create avd -n testEmulator19 -k "system-images;android-19;google_apis;armeabi-v7a"

ENV ANDROID_HOME="/opt/android-sdk-linux"
ENV ANDROID_NDK_HOME="/opt/android-sdk-linux/ndk-bundle"
