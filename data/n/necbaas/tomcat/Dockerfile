FROM necbaas/openjdk:11.0.5

ENV TOMCAT_VERSION 9.0.30

# install tomcat
RUN mkdir /opt/tomcat && cd /opt/tomcat \
  && aria2c -x5 http://archive.apache.org/dist/tomcat/tomcat-9/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.tar.gz \
  && tar xzf apache-tomcat-$TOMCAT_VERSION.tar.gz --strip-components=1 \
  && rm apache-tomcat-$TOMCAT_VERSION.tar.gz \
  && rm -rf webapps/* \
  && chmod -R ugo+rwx conf webapps logs temp work
