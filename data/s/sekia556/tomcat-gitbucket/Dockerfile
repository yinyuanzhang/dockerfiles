FROM tomcat:8-jre8
## Gitbucket 4.1 is built/tested on java8

MAINTAINER sekia556 <sekia556 [at] yahoo.co.jp>

## Prepare GITBUCKET_HOME
## CATALINA_HOME is /usr/local/tomcat
ENV GITBUCKET_HOME $CATALINA_HOME/gitbucket
RUN mkdir -p $GITBUCKET_HOME

## Deploy gitbucket.war as ROOT.war
RUN rm -rf $CATALINA_HOME/webapps/*
ADD https://github.com/gitbucket/gitbucket/releases/download/4.1/gitbucket.war $CATALINA_HOME/webapps/ROOT.war

RUN ln -s $GITBUCKET_HOME /opt/gitbucket
RUN ln -s $CATALINA_HOME/logs /opt/tomcat_logs

# /usr/local/tomcat/gitbucket
VOLUME /opt/gitbucket    
# /usr/local/tomcat/logs
VOLUME /opt/tomcat_logs

# Web Page
EXPOSE 8080

# (Optional) port for SSH to git repository
EXPOSE 29418

CMD ["catalina.sh", "run"]

