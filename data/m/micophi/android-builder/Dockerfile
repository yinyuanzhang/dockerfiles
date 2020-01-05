FROM gradle:4.6

USER root
RUN apt-get update 
RUN apt-get install -y curl unzip zip
RUN curl -L https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip -o sdk-tools-linux.zip
RUN unzip -o -q sdk-tools-linux.zip -d /opt/sdk-tools-linux
RUN chown -R gradle:gradle /opt/sdk-tools-linux


ENV ANDROID_HOME=/opt/sdk-tools-linux
ENV PATH="$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/tools/bin:$ANDROID_HOME/platform-tools"


USER gradle
RUN yes | sdkmanager --licenses
RUN sdkmanager --update
RUN sdkmanager --install "platforms;android-28" "build-tools;28.0.3" "extras;google;m2repository" "extras;android;m2repository"
RUN sdkmanager --install "platform-tools"


