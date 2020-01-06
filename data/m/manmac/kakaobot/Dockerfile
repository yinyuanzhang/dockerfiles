FROM openjdk:8
MAINTAINER manmac
ENV TZ "Asia/Seoul"
ADD . /application
WORKDIR /application
RUN ./gradlew build -x test
WORKDIR /application/build/libs
USER nobody
CMD [ "java", "-jar", "kakaobot-0.0.1-SNAPSHOT.jar" ]
EXPOSE 8080