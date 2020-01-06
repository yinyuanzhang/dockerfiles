FROM healthcatalyst/fabric.docker.centos.tomcat:latest

LABEL maintainer="imran.qureshi@healthcatalyst.com"
LABEL version="2018.04.05"

# install mariadb-client (i.e., mysql client) so we can wait for our tables to become ready
ADD mariadb.repo /etc/yum.repos.d/

RUN yum -y install MariaDB-client; yum clean all

# copy all the files
# ADD https://fabricnlpfiles.blob.core.windows.net/war/nlpweb.war /opt/tomcat-nlp-nlpweb/webapps/

RUN mv opt/apache-tomcat /opt/tomcat-nlp-nlpweb \
	&& cd /opt/tomcat-nlp-nlpweb/webapps/ \
	&& mkdir -p nlpweb \
	&& cd nlpweb \
	&& curl -O https://fabricnlpfiles.blob.core.windows.net/war/nlpweb.war \
	&& ls \
	&& jar xvf nlpweb.war \
	&& rm -fv nlpweb.war \
	&& ls -al /opt/tomcat-nlp-nlpweb/webapps/ \
	&& rm --force --verbose WEB-INF/lib/hibernate-validator-6.0.5.Final.jar \
	&& ls -al /opt/tomcat-nlp-nlpweb/webapps/nlpweb/WEB-INF/lib/hib* \
	&& cd

RUN cd /opt \
    && echo "Fetching models files..." \
    && curl -O https://fabricnlpfiles.blob.core.windows.net/models/models.tar \
    && ls \
    && tar -xvf models.tar \
    && rm -vf models.tar \
    && ls -lah \
    && ls -lah models \
    && cd

ADD application.properties /etc/nlp/nlpweb/

COPY db/migration/ db/migration/

# RUN cp -r db/migration /opt/tomcat-nlp-nlpweb/webapps/nlpweb/WEB-INF/classes/db/

ADD log4j.xml /etc/nlp/nlpweb/
ADD server.xml /opt/tomcat-nlp-nlpweb/conf/server.xml
ADD tomcat-users.xml /opt/tomcat-nlp-nlpweb/conf/
ADD setenv.sh /opt/tomcat-nlp-nlpweb/bin/setenv.sh

COPY indexes/ /opt/indexes/
ADD searchConfig.json /etc/nlp/nlpweb/
ADD searchConfig.json /opt/nlp/

ADD docker-entrypoint.sh ./docker-entrypoint.sh
ADD update_tomcat_config.py ./update_tomcat_config.py
ADD updateconfig.sh /etc/nlp/nlpweb/

RUN dos2unix ./docker-entrypoint.sh &>/dev/null \
	&& chmod a+x ./docker-entrypoint.sh \
	&& dos2unix /etc/nlp/nlpweb/updateconfig.sh &>/dev/null \
	&& chmod a+x /etc/nlp/nlpweb/updateconfig.sh

EXPOSE 8083

ENTRYPOINT ["./docker-entrypoint.sh"]
