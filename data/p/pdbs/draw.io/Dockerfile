FROM tomcat:9-jre8-alpine
LABEL build="201905022040"
LABEL maintainer="marc.jakob@bs.ch"

RUN apk add \
    openjdk8 apache-ant git patch xmlstarlet curl && \
    cd /tmp && \
    curl -OL https://github.com/jgraph/drawio/archive/master.zip && \
    unzip master.zip && \
    cd /tmp/drawio-master && \
    sed -i 's/var result = new Object();/var result = new Object();\nresult["offline"]="1";\nresult["stealth"]="1";/g' /tmp/drawio-master/src/main/webapp/index.html && \
    cd /tmp/drawio-master/etc/build && \
    ant war && \
    cd /tmp/drawio-master/build && \
    mkdir -p $CATALINA_HOME/webapps/draw && \
    unzip /tmp/drawio-master/build/draw.war -d $CATALINA_HOME/webapps/draw && \
    apk del --purge openjdk8 apache-ant git patch && \
    rm -rf \
        /tmp/vmaster.zip \
        /tmp/drawio-master

# Update server.xml to set Draw.io webapp to root
RUN cd $CATALINA_HOME && \
    xmlstarlet ed \
    -P -S -L \
    -i '/Server/Service/Engine/Host/Valve' -t 'elem' -n 'Context' \
    -i '/Server/Service/Engine/Host/Context' -t 'attr' -n 'path' -v '/' \
    -i '/Server/Service/Engine/Host/Context[@path="/"]' -t 'attr' -n 'docBase' -v 'draw' \
    -s '/Server/Service/Engine/Host/Context[@path="/"]' -t 'elem' -n 'WatchedResource' -v 'WEB-INF/web.xml' \
    -i '/Server/Service/Engine/Host/Valve' -t 'elem' -n 'Context' \
    -i '/Server/Service/Engine/Host/Context[not(@path="/")]' -t 'attr' -n 'path' -v '/ROOT' \
    -s '/Server/Service/Engine/Host/Context[@path="/ROOT"]' -t 'attr' -n 'docBase' -v 'ROOT' \
    -s '/Server/Service/Engine/Host/Context[@path="/ROOT"]' -t 'elem' -n 'WatchedResource' -v 'WEB-INF/web.xml' \
    conf/server.xml


WORKDIR $CATALINA_HOME

EXPOSE 8080
CMD ["catalina.sh", "run"]
