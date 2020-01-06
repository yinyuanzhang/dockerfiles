FROM ubuntu:xenial

LABEL version="1.0.0" \
  maintainer="Stepan Beznosov" \
  maintainer.email="bez.stepan@gmail.com" \
  description="Base Android Unit Testing Docker image" \
  repository="https://github.com/BStepan/base-android-builder"

# setup deps & java
RUN apt-get update \
  && apt-get install lib32ncurses5 lib32z1 software-properties-common wget git unzip --yes \
  && echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections \
  && add-apt-repository ppa:webupd8team/java \
  && apt-get update \
  && apt-get install oracle-java8-set-default --yes \
  && apt-get install nano \
  && apt-get clean

# setup android sdk and android sdk licences
RUN wget -O /opt/android-tools.zip https://dl.google.com/android/repository/tools_r25.2.3-linux.zip \
  && unzip /opt/android-tools.zip -d /opt \
  && mkdir -p /opt/android-sdk/licenses \
  && mv /opt/tools /opt/android-sdk/tools \
  && rm /opt/android-tools.zip \
  && mkdir ~/.android; echo "count=0" >> ~/.android/repositories.cfg

ENV JAVA_HOME=/usr/lib/jvm/java-8-oracle \
  ANDROID_HOME=/opt/android-sdk \
  JAVA_OPTS="-Xms2048m -Xmx5120m"

#setting up helper script
RUN mkdir -p /opt/
COPY yes /tmp/yes 
RUN mv /tmp/yes /opt/yes 
RUN chmod +x /opt/yes 
#RUN source /opt/yes

#update SDK
RUN /opt/android-sdk/tools/bin/sdkmanager --update

WORKDIR /opt
