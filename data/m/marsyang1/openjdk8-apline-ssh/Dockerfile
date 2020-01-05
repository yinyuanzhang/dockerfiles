FROM openjdk:8-jdk-alpine
# Install font var cURL , doc: https://www.jianshu.com/p/e39ee0cad05b
RUN echo -e "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.4/main\n\
https://mirror.tuna.tsinghua.edu.cn/alpine/v3.4/community" > /etc/apk/repositories

RUN apk add --update openssh curl bash ttf-dejavu tzdata

# Default to UTF-8 file.encoding
ENV LANG C.UTF-8
