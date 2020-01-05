FROM tomcat

ENV CATALINA_HOME /usr/local/tomcat
ENV PATH $CATALINA_HOME/bin:$PATH

RUN mkdir -p "$CATALINA_HOME" \
    && apt-get update

WORKDIR $CATALINA_HOME

ADD ./petclinic.war $CATALINA_HOME/webapps/

EXPOSE 8080
CMD ["catalina.sh", "run"]
