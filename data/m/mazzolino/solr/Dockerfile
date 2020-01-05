FROM ubuntu:14.04

RUN apt-get update
RUN apt-get -y install solr-tomcat

CMD ["/usr/bin/env", "/usr/lib/jvm/default-java/jre/bin/java", "-Djava.util.logging.config.file=/var/lib/tomcat6/conf/logging.properties", "-Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager", "-Djava.awt.headless=true", "-Xmx128m", "-XX:+UseConcMarkSweepGC", "-Djava.endorsed.dirs=/usr/share/tomcat6/endorsed", "-classpath", "/usr/share/tomcat6/bin/bootstrap.jar", "-Dcatalina.base=/var/lib/tomcat6", "-Dcatalina.home=/usr/share/tomcat6", "-Djava.io.tmpdir=/tmp/tomcat6-tomcat6-tmp", "-Dsolr.data.dir=/var/lib/solr/data", "org.apache.catalina.startup.Bootstrap", "start"]
VOLUME ["/var/lib/solr/data"]
EXPOSE 8080
