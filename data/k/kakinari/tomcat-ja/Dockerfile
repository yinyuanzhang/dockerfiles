FROM kakinari/openjdk-ja:jre-1.8.0
ENV container docker
ENV CATALINA_VERSION=8.5.39
ENV CATALINA_HOME=/opt/apache-tomcat-${CATALINA_VERSION}
ENV CATALINA_BASE=/opt/tomcat
COPY log4j.properties /opt/
COPY tomcat.service /etc/systemd/system/
RUN yum -y install unzip;\
yum -y upgrade;\
yum -y clean all; \
rm -rf /var/cache/yum/*;\
groupadd -g 1000 apache;\
useradd -u 1000 -g 1000 tomcat;\
(cd /opt ;\
curl -O http://archive.apache.org/dist/tomcat/tomcat-8/v${CATALINA_VERSION}/bin/apache-tomcat-${CATALINA_VERSION}.zip;\
unzip $CATALINA_HOME.zip);\
mkdir $CATALINA_BASE;\
(cd $CATALINA_BASE; mkdir bin conf logs webapps lib work temp;\
touch bin/setenv.sh;\
chmod +x bin/setenv.sh;\
cp $CATALINA_HOME/bin/tomcat-juli.jar bin;\
cp -r $CATALINA_HOME/conf/* conf;\
cp -r $CATALINA_HOME/lib/* lib);\
chown -R tomcat:apache $CATALINA_HOME;\
chown -R tomcat:apache $CATALINA_BASE;\
mv /opt/log4j.properties $CATALINA_HOME/lib/;\
rm -rf $CATALINA_HOME/webapps/*;\
chmod +x $CATALINA_HOME/bin/*.sh;\
rm -f $CATALINA_HOME.zip;\
rm -f $CATALINA_HOME/[A-Z]*;\
rm -f $CATALINA_HOME/bin/*.bat;\
rm -f $CATALINA_HOME/bin/*.tar.gz;\
ln -s /etc/systemd/system/tomcat.service /etc/systemd/system/multi-user.target.wants/tomcat.service;
EXPOSE 8080
VOLUME /sys/fs/cgroup
CMD /usr/sbin/init
