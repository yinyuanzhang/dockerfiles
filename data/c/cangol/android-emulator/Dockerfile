FROM cangol/android-gradle
LABEL MAINTAINER Cangol  <wxw404@gmail.com>

# android sdk|build-tools|image
ENV ANDROID_IMAGES="system-images;android-22;google_apis;x86_64"   
RUN echo yes | $ANDROID_HOME/tools/bin/sdkmanager --licenses
RUN echo yes | $ANDROID_HOME/tools/bin/sdkmanager ${ANDROID_IMAGES}

#android-wait-for-emulator
ENV PATH ${SDK_HOME}/bin:$PATH
RUN curl https://raw.githubusercontent.com/Cangol/android-gradle-docker/master/android-wait-for-emulator -o ${SDK_HOME}/bin/android-wait-for-emulator
RUN chmod u+x ${SDK_HOME}/bin/android-wait-for-emulator

#avdmanager create avd
RUN ${ANDROID_HOME}/tools/bin/avdmanager create avd --force --name test -k  ${ANDROID_IMAGES} --device "Nexus 4" --sdcard 500M
#RUN ${ANDROID_HOME}/platform-tools/adb kill-server
#RUN ${ANDROID_HOME}/platform-tools/adb start-server
#RUN ${ANDROID_HOME}/tools/emulator -avd test -noaudio -no-window &
#RUN android-wait-for-emulator
#RUN adb shell input keyevent 82 &
