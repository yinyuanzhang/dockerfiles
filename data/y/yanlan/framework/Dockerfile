FROM maven:alpine
COPY docker/settings.xml /usr/share/maven/ref/
RUN mvn -v
ADD ./ /usr/src/code
RUN ls /usr/src/code
WORKDIR /usr/src/code
RUN mvn package -s /usr/share/maven/ref/settings.xml
RUN ls /usr/src/code/target

ARG TZ
ENV TZ=${TZ:-"Asia/Shanghai"}
RUN mkdir /app
RUN cp /usr/src/code/target/framework.jar /app/wxapp.jar
WORKDIR /app/
EXPOSE 8886
ENTRYPOINT exec java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -Dsun.misc.URLClassPath.disableJarChecking=true -jar wxapp.jar --spring.profiles.active=test