FROM maven:3.6.0-jdk-8-alpine AS MAVEN_TOOL_CHAIN
ADD https://jqassistant.org/wp-content/uploads/2018/12/jqassistant-commandline-neo4jv3-1.6.0-distribution.zip /opt/
RUN cd /opt && unzip jqassistant-commandline-neo4jv3-1.6.0-distribution.zip
ADD https://github.com/softvis-research/jqa-javascript-plugin/releases/download/0.0.1/jqassistant-javascript-plugin-0.0.1.jar /opt/jqassistant-commandline-neo4jv3-1.6.0/plugins
ADD https://github.com/softvis-research/jqa-typechef-plugin/releases/download/v0.0.1/jqa-c-plugin-0.0.1-SNAPSHOT.jar /opt/jqassistant-commandline-neo4jv3-1.6.0/plugins
RUN chmod 644 /opt/jqassistant-commandline-neo4jv3-1.6.0/plugins/jqassistant-javascript-plugin-0.0.1.jar /opt/jqassistant-commandline-neo4jv3-1.6.0/plugins/jqa-c-plugin-0.0.1-SNAPSHOT.jar

FROM jetty:9.4.12-jre8-alpine
COPY --from=MAVEN_TOOL_CHAIN /opt/jqassistant-commandline-neo4jv3-1.6.0/ /opt/jqassistant/
COPY start.sh /start.sh
RUN mkdir -p /var/lib/jetty/data-gen/ && mkdir -p /var/lib/jetty/logs/ && mkdir -p /var/lib/jetty/output/ && chown -R jetty:jetty /var/lib/jetty/logs/ /var/lib/jetty/output/ /var/lib/jetty/data-gen/
EXPOSE 8080
ENTRYPOINT ["/start.sh"]
USER root
RUN sed -i 's/\/home\/jetty:\/sbin\/nologin/\/home\/jetty:\/bin\/sh/g' /etc/passwd
VOLUME ["/var/lib/jetty/webapps/", "/opt/config/", "/var/lib/jetty/output/", "/var/lib/jetty/logs/", "/var/lib/jetty/data-gen/"]
user jetty
LABEL maintainer="david.baum@uni-leipzig.de" \
 version="1.0"
