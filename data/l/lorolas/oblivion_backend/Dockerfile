FROM gradle:6.0.1-jdk13 AS backend

USER root
COPY --chown=gradle settings.gradle.kts /home/gradle/
COPY --chown=gradle build.gradle.kts /home/gradle/
COPY --chown=gradle /backend/shared /home/gradle/backend/shared
COPY --chown=gradle /backend/monolith /home/gradle/backend/monolith
# COPY --chown=gradle /backend/monolith/gradle.properties /home/gradle/backend/monolith/

USER gradle
WORKDIR /home/gradle
RUN gradle clean

USER gradle
WORKDIR /home/gradle
RUN gradle war && unzip backend/monolith/build/libs/backend.war -d backend/monolith/build/libs/backend && mv backend/monolith/build/libs/backend/WEB-INF/lib backend/monolith/build/libs/lib
# && find backend/monolith/build

FROM tomcat:9.0.29-jdk13-openjdk-oracle

RUN rm -rf /usr/local/tomcat/webapps/*
COPY --from=backend /home/gradle/backend/monolith/build/libs/lib /usr/local/tomcat/webapps/ROOT/WEB-INF/lib
COPY --from=backend /home/gradle/backend/monolith/build/libs/backend /usr/local/tomcat/webapps/ROOT

ENV PORT 8080
EXPOSE 8080

WORKDIR $CATALINA_HOME
CMD ["catalina.sh", "run"]

HEALTHCHECK --interval=1m --timeout=30s CMD curl -f http://localhost:8080/bnet/verify || exit 1
