#
# Nuclos Dockerfile 
#
# https://bitbucket.org/nuccess/docker-nuclos
#

FROM openjdk:11.0-jdk

RUN apt-get install -y curl
# Node.js 12
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y nodejs
# npm
RUN curl -sL https://www.npmjs.com/install.sh | sh
RUN npm install -g grunt grunt-cli
RUN apt-get install -y rsync
RUN apt-get install -y netcat

# confirm environment
RUN java -version
RUN npm -v
RUN node -v

ARG DOWNLOAD_URL=ftp://nightly:thieP0ae@ftp.nuclos.de/nuclos-4.37.1/nuclos-4.37.1-installer-generic.jar
ARG DOWNLOAD_HASH=1463e1cd5efa857f6480e44b2f2ad51c
ENV NUCLOS_PORT=80 \
  NUCLOS_DEBUG_PORT=8000 \
  NUCLOS_HEAPSIZE=2048 \
  NUCLOS_DIR=/opt/nuclos \
  NUCLOS_WEBCLIENT_CONF=webapps/ROOT/webclient/assets/config.json \
  NUCLOS_WEBCLIENT1_CONF=webapps/ROOT/webclient1/app/server.json \
  NUCLOS_TOMCAT_CONF=conf/server.xml
ENV NUCLOS_HOME=$NUCLOS_DIR/home
ENV NUCLOS_CONF=$NUCLOS_HOME/conf \
  NUCLOS_STARTUP=$NUCLOS_HOME/bin/startup.sh
ENV DB_SCHEMA=nuclos \
  TOTAL_RAM_GB=2 \
  WEBCLIENT_PORT=80 \
  LIVE_SEARCH=true \
  DEVELOPMENT=false \
  LOCALE=de_DE.UTF-8 \
  TZ=Europe/Berlin \
  KEYSTORE_PASSWORD=password

WORKDIR $NUCLOS_DIR

RUN \
  wget --tries=3 --wait=60 --timeout=30 --no-dns-cache $DOWNLOAD_URL
RUN \
  export DOWNLOAD_FILE="${DOWNLOAD_URL##*/}" && \
  echo "Checking downloaded $DOWNLOAD_FILE ... " && \
  test `md5sum $DOWNLOAD_FILE | awk '{ print $1 }'` = $DOWNLOAD_HASH

ADD nuclos-template.xml .
ADD nuclos-run.sh .
ADD Docker-v417004.jar .
ADD Docker-v417004_01_application.sql .
ADD Docker-v427001_02_nucletparameter.sql .
ADD Docker-v417004_03_jobcontroller.sql .
ADD Docker-v417004_04_servercode.sql .
ADD Docker-v417004_05_servercode_job.sql .
ADD nuclos-db-cmd.sh /usr/local/bin
ADD nuclos-logs.sh /usr/local/bin
ADD nuclos-config.sh /usr/local/bin
ADD nuclos-install.sh /usr/local/bin
ADD nuclos-extensions.sh /usr/local/bin
ADD nuclos-shutdown.sh /usr/local/bin
ADD nuclos-restore.sh /usr/local/bin

RUN \
  chmod +x /usr/local/bin/*.sh

WORKDIR $NUCLOS_HOME

RUN \
  rm -f nuclos.xml && \
  cp $NUCLOS_DIR/nuclos-template.xml nuclos.xml

RUN \
  sed -i 's:NUCLOS_HOME:'"$NUCLOS_HOME"':g' nuclos.xml && \
  sed -i 's:NUCLOS_DOCUMENTS:'"$NUCLOS_HOME/data/documents"':g' nuclos.xml && \
  sed -i 's:NUCLOS_PORT:'"$NUCLOS_PORT"':g' nuclos.xml && \
  sed -i 's:NUCLOS_HEAPSIZE:'"$NUCLOS_HEAPSIZE"':g' nuclos.xml && \
  sed -i 's:JAVA_HOME:'"$JAVA_HOME"':g' nuclos.xml

RUN \
  export DOWNLOAD_FILE="${DOWNLOAD_URL##*/}" && \
  $JAVA_HOME/bin/java -jar $NUCLOS_DIR/$DOWNLOAD_FILE -s $NUCLOS_HOME/nuclos.xml && \
  mkdir -p $NUCLOS_DIR/update/backup && \
  mv $NUCLOS_DIR/$DOWNLOAD_FILE $NUCLOS_DIR/update/backup/$DOWNLOAD_FILE && \
  echo "$DOWNLOAD_HASH" > $NUCLOS_DIR/update/backup/$DOWNLOAD_FILE.md5

RUN \
  cp $NUCLOS_CONF/server.properties $NUCLOS_DIR/server.properties-template && \
  cp $NUCLOS_CONF/jdbc.properties $NUCLOS_DIR/jdbc.properties-template && \
  rsync -av --del $NUCLOS_HOME/client/ $NUCLOS_DIR/client/

# Change Tomcat defaults, remove templates, manager, etc.
# Place a redirect in ROOT to Nuclos webclient.
# Backup config files for updating with parameters during run.
RUN \
  export TOMCAT_DIR=$(find $NUCLOS_HOME -iname "apache-tomcat-*" -type d) && \
  rm -fdr $(find $TOMCAT_DIR/webapps/* -maxdepth 0 ! -name ROOT -type d) && \
  rm -f $(find $TOMCAT_DIR/webapps/ROOT -maxdepth 1 -type f) && \
  echo "<% response.sendRedirect(\"/webclient\"); %>" > $TOMCAT_DIR/webapps/ROOT/index.jsp && \
  mv $TOMCAT_DIR/$NUCLOS_WEBCLIENT_CONF $TOMCAT_DIR/$NUCLOS_WEBCLIENT_CONF-template && \
  mv $TOMCAT_DIR/$NUCLOS_TOMCAT_CONF $TOMCAT_DIR/$NUCLOS_TOMCAT_CONF-template && \
  mv $NUCLOS_STARTUP $NUCLOS_STARTUP-template

# Expose the nuclos ports
EXPOSE 80 8000 8009 8033

# Add VOLUMEs to access documents, logs and backups
VOLUME ["/opt/nuclos/home/data/documents", "/opt/nuclos/home/data/index", "/opt/nuclos/home/data/codegenerator", "/opt/nuclos/client", "/opt/nuclos/home/logs", "/opt/nuclos/backups", "/var/nuclos-db"]

# Set the default command to run when starting the container
CMD ["/opt/nuclos/nuclos-run.sh"]