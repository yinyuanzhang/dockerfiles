FROM node:13.5 AS client

#RUN npm i -g npm yarn
COPY client/package.json /src/app/package.json
WORKDIR /src/app
RUN yarn --no-cache --non-interactive --link-duplicates --network-timeout 600000

COPY client /src/app
RUN yarn run build
#&& rm -rf /src/app/node_modules

FROM gradle:6.0.1-jdk13 AS server

USER root
WORKDIR /home/gradle
# RUN apt-get update && apt-get install git unzip -y && apt-get clean
COPY --chown=gradle /gradle.properties /settings.gradle /build.gradle ./
COPY --chown=gradle /client/build.gradle /home/gradle/client/
COPY --chown=gradle /server /home/gradle/server
#COPY --from=0 /src/app /home/gradle/client/dist
#RUN chmod -R 0777 /home/gradle

USER gradle
WORKDIR /home/gradle
RUN gradle war && unzip server/build/libs/Oblivion-Web.war -d server/build/libs/Oblivion-Web && mv server/build/libs/Oblivion-Web/WEB-INF/lib server/build/libs/lib

FROM tomcat:9.0.30-jdk13-openjdk-oracle

RUN rm -rf /usr/local/tomcat/webapps/*
COPY --from=server /home/gradle/server/build/libs/lib /usr/local/tomcat/webapps/ROOT/WEB-INF/lib
#COPY --from=server /home/gradle/server/build/libs/Oblivion-Web/assets /usr/local/tomcat/webapps/ROOT/assets
COPY --from=client /src/app/dist /usr/local/tomcat/webapps/ROOT
COPY --from=server /home/gradle/server/build/libs/Oblivion-Web /usr/local/tomcat/webapps/ROOT

ENV PORT 8080
EXPOSE 8080

WORKDIR $CATALINA_HOME
CMD ["catalina.sh", "run"]

HEALTHCHECK --interval=1m --timeout=30s CMD curl -f http://localhost:8080/api/verify || exit 1
