FROM openjdk:8-jre-alpine
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone
EXPOSE 8035
VOLUME /dubbo
WORKDIR /dubbo
ENTRYPOINT  java -Djava.security.egd=file:/dev/./urandom -Duser.timezone=GMT+08 -jar /dubbo/dubbo.jar
