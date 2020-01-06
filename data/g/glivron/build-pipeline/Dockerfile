FROM openjdk:8-jdk

RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - \
 && apt-get -qq install -y nodejs                           \
 && npm update  -g                                          \
 && npm install -g typescript typings @angular/cli || true

RUN ng version

ADD gradle /tmp
WORKDIR /tmp

RUN ./gradlew --no-daemon build \
 && rm -fR /tmp/*

WORKDIR /
