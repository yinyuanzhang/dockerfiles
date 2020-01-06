###########################################################################
# Dockerfile that provides the image for jBPM Workbench 6.4.0.Final on Tomcat
###########################################################################

####### BASE ############
FROM tomcat:7.0

####### MAINTAINER ############
MAINTAINER "Wong Liong Hung" "lhwong@gmail.com"

####### ENVIRONMENT ############
ENV KIE_REPOSITORY https://repository.jboss.org/nexus/content/groups/public-jboss
ENV KIE_VERSION 6.4.0.Final
ENV KIE_CLASSIFIER webc
ENV KIE_CONTEXT_PATH kie-server
ENV JAVA_OPTS -XX:MaxPermSize=256m -Xms256m -Xmx512m


####### KIE-SERVER ############
RUN curl -o $HOME/$KIE_CONTEXT_PATH.war $KIE_REPOSITORY/org/kie/server/kie-server/$KIE_VERSION/kie-server-$KIE_VERSION-$KIE_CLASSIFIER.war && \
unzip -q $HOME/$KIE_CONTEXT_PATH.war -d $CATALINA_HOME/webapps/$KIE_CONTEXT_PATH &&  \
rm -rf $HOME/$KIE_CONTEXT_PATH.war

####### Drools KIE Server CUSTOM CONFIGURATION ############
RUN mkdir -p $HOME/.m2
ADD etc/lib/btm-2.1.4.jar $CATALINA_HOME/lib/btm-2.1.4.jar
ADD etc/lib/btm-tomcat55-lifecycle-2.1.4.jar $CATALINA_HOME/lib/btm-tomcat55-lifecycle-2.1.4.jar
ADD etc/lib/h2-1.3.168.jar $CATALINA_HOME/lib/h2-1.3.168.jar
ADD etc/lib/jacc-1.0.jar $CATALINA_HOME/lib/jacc-1.0.jar
ADD etc/lib/jta-1.1.jar $CATALINA_HOME/lib/jta-1.1.jar
ADD etc/lib/kie-tomcat-integration-$KIE_VERSION.jar $CATALINA_HOME/lib/kie-tomcat-integration-$KIE_VERSION.jar
ADD etc/lib/slf4j-api-1.7.2.jar $CATALINA_HOME/lib/slf4j-api-1.7.2.jar
ADD etc/lib/slf4j-jdk14-1.7.2.jar $CATALINA_HOME/lib/slf4j-jdk14-1.7.2.jar

ADD etc/btm-config.properties $CATALINA_HOME/conf/btm-config.properties
ADD etc/resources.properties $CATALINA_HOME/conf/resources.properties
ADD etc/tomcat-users.xml $CATALINA_HOME/conf/tomcat-users.xml

ADD etc/setenv.sh $CATALINA_HOME/bin/setenv.sh

####### Redis session manager #########
ADD etc/lib/tomcat-redis-session-manager-2.0.0.jar $CATALINA_HOME/lib/tomcat-redis-session-manager-2.0.0.jar
ADD etc/lib/jedis-2.9.0.jar $CATALINA_HOME/lib/jedis-2.9.0.jar
ADD etc/lib/commons-pool2-2.4.2.jar $CATALINA_HOME/lib/commons-pool2-2.4.2.jar

ADD etc/context.xml $CATALINA_HOME/conf/context.xml

####### Configure login-config #########
ADD etc/index.html $CATALINA_HOME/webapps/kie-server/index.html
ADD etc/login.html $CATALINA_HOME/webapps/kie-server/login.html
ADD etc/error.html $CATALINA_HOME/webapps/kie-server/error.html
ADD etc/web.xml $CATALINA_HOME/webapps/kie-server/WEB-INF/web.xml



####### RUNNING KIE-SERVER ############
WORKDIR $CATALINA_HOME/bin/
CMD ["catalina.sh", "run"]
