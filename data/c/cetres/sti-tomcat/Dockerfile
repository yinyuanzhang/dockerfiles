FROM tomcat:8.0

MAINTAINER Gustavo Oliveira <cetres@gmail.com>

LABEL io.k8s.description="Platform for running Java applications on Tomcat" \
      io.k8s.display-name="Tomcat Java Applications" \
      io.openshift.expose-services="8080:http" \
      io.openshift.tags="builder,java,tomcat" \
      io.openshift.s2i.scripts-url="image:///usr/local/s2i"

COPY ./s2i/bin/ /usr/local/s2i

RUN chmod -R g+rw /usr/local/tomcat && \
    mkdir -p /usr/local/tomcat/webapps/healthz/WEB-INF/classes

COPY ./util/healthz.class /usr/local/tomcat/webapps/healthz/WEB-INF/classes/ 
COPY ./util/web.xml /usr/local/tomcat/webapps/healthz/WEB-INF/

USER 1001

EXPOSE 8080

CMD ["usage"]
