FROM postgres:9.5

ARG INIT_FILE=init-scripts/main.sql
ARG JIRA_VERSION=software-8.4.2
ARG INSTALL_DIR=/opt/atlassian/jira
ARG HOME_DIR=/var/atlassian/jira
ARG INIT_DIR=/docker-init
ARG PHANTOM_JS=phantomjs-2.1.1-linux-x86_64

ENV POSTGRES_INITDB_ARGS="--lc-ctype=C --lc-collate=C --encoding=UTF8"
ENV JIRA_MIN_MEM 512
ENV JIRA_MAX_MEM 1536

RUN apt-get update && apt-get install -y gettext wget curl ttf-liberation build-essential chrpath libssl-dev libxft-dev unzip

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs

RUN npm install -g --allow-root --unsafe-perm=true puppeteer@1.0.0
RUN echo "export NODE_PATH=$(npm root --quiet -g)" >> /etc/profile.d/lib.sh
RUN echo "alias node='node -e \"\`cat $1 | sed \"s/var config = {};/var config = {args: \[\'--no-sandbox\'\]};/\"\`' " >> /etc/profile.d/lib.sh

RUN set -x \
        && wget --progress=dot:mega https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2 \
        && tar xvjf $PHANTOM_JS.tar.bz2 \
        && mv $PHANTOM_JS /usr/local/share \
        && ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin

ADD $INIT_FILE prepare/init.sql
ADD init-scripts/zzz-update-last.sh /docker-init/

USER root

COPY ["docker-entrypoint.sh", "/"]
COPY ["db-config", "${INIT_DIR}/db"]
COPY ["jira-config", "${INIT_DIR}/jira"]
COPY ["filebeat.yml", "${INIT_DIR}/filebeat.yml"]


RUN set -x \
	&& wget --progress=dot:mega https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-${JIRA_VERSION}-x64.bin \
	&& chmod a+x atlassian-jira-*-x64.bin \
	&& ./atlassian-jira-*-x64.bin -q -varfile ${INIT_DIR}/jira/response.varfile \
	&& rm atlassian-jira-*-x64.bin \
	&& $INSTALL_DIR/bin/catalina.sh stop -force

RUN set -x \
	&& wget --progress=dot:mega https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-6.1.2-amd64.deb \
	&& dpkg -i filebeat-6.1.2-amd64.deb

RUN mkdir -p $HOME_DIR/plugins/installed-plugins
RUN chmod -R 777 $HOME_DIR
ADD rest-api-browser-3.2.2.jar $HOME_DIR/plugins/installed-plugins/rest-api-plugin.jar
RUN ln -sf /usr/share/zoneinfo/Europe/Warsaw /etc/localtime
RUN echo log4j.logger.com.softwareplant=DEBUG >> /opt/atlassian/jira/atlassian-jira/WEB-INF/classes/log4j.properties

COPY ["bigtemplate-local.properties", "/root/"]
RUN mkdir /opt/atlassian/jira/temp/node_modules
RUN ln -s /usr/lib/node_modules/puppeteer /opt/atlassian/jira/temp/node_modules/puppeteer

EXPOSE 8080
EXPOSE 8000
EXPOSE 5432

VOLUME ["$HOME_DIR", "$INSTALL_DIR", "$INIT_DIR"]

WORKDIR $HOME_DIR

RUN chmod a+x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
