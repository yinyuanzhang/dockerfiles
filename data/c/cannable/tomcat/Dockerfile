ARG tcorigin=7.0-jre8-alpine
FROM tomcat:${tcorigin}

ENV NAME HARDTC
ENV TC_USER tomcat
ENV TC_UID 6060

WORKDIR /usr/local/tomcat

COPY ["./data", "/data"]
COPY ["./overrides", "/data/overrides"]
RUN ["/bin/bash", "/data/build.sh"]

VOLUME ["/usr/local/tomcat/conf", \
        "/usr/local/tomcat/logs", \
        "/usr/local/tomcat/temp", \
        "/usr/local/tomcat/webapps", \
        "/usr/local/tomcat/work"]

EXPOSE 8443/tcp
EXPOSE 8080/tcp

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["/bin/bash", "/data/init.sh"]