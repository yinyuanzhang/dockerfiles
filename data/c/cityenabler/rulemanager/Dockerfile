FROM maven:3.6.2-slim as builder
COPY /rules/. /usr/app 
WORKDIR /usr/app
RUN mvn install

FROM tomcat:9.0.20-jre8-alpine
MAINTAINER Filippo Giuffrida
ENV CATALINA_OPTS -Dsecurerandom.source=file:/dev/urandom
RUN rm -rf /usr/local/tomcat/webapps/ROOT
COPY --from=builder /usr/app/target/ROOT.war /usr/local/tomcat/webapps/ROOT.war
EXPOSE 8080