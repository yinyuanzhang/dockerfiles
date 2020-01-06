FROM openjdk:8-jdk-alpine
ENV USER_NAME swuser
ENV APP_HOME /usr/$USER_HOME/app
ENV UID=1002
RUN mkdir -p /usr/app
WORKDIR /usr/app
COPY mysimpleproj.jar /usr/app/mysimpleproj.jar
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","mysimpleproj.jar"]
