FROM gradle:4.10.1-jdk8-alpine

USER root

# Creating Application Source Code Directory
RUN mkdir -p /usr/src/app

# Setting Home Directory for containers
WORKDIR /usr/src/app

# Copying src code to Container
ADD . /usr/src/app

# Building From Source Code
RUN ./gradlew build

# Exposing Port
EXPOSE 8888

# Running Kotlin Application
CMD ["java","-Djava.security.egd=file:/dev/./urandom","-jar","build/libs/footprint-0.1.0.jar"]