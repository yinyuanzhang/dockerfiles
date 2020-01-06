FROM adoptopenjdk/openjdk13:alpine

ENV \
  GRADLE_VERSION=6.0 \
  GRADLE_HOME=/usr/local/gradle
  
# GRADLE
RUN \
  cd /usr/local && \
  apk add --no-cache wget bash libstdc++ && \
  wget https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-bin.zip && \
  unzip gradle-$GRADLE_VERSION-bin.zip && \
  rm -f gradle-$GRADLE_VERSION-bin.zip && \
  ln -s gradle-$GRADLE_VERSION gradle && \
  apk del wget

# AWS CLI
RUN \
  apk add --no-cache python3 && \
  pip3 install awscli

ENV PATH=${PATH}:${GRADLE_HOME}/bin
