FROM openjdk:11.0-jre-slim
LABEL maintainer="hoenirvili <hoenirvili@gmail.com>" \
    version="0.1" \
    purpose=ci
RUN apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y
RUN apt-get install -y gradle 
