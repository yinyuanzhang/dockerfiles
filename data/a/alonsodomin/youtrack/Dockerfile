FROM java:7-jre

MAINTAINER Antonio Alonso Dominguez "alonso@codenibbles.com"

ENV YOUTRACK_VERSION 6.0.12619
ENV YOUTRACK_HOME /opt/lib/youtrack
ENV YOUTRACK_USER_HOME /opt/share/youtrack
ENV YOUTRACK_DB_DIR /var/lib/youtrack

RUN mkdir -p $YOUTRACK_HOME && \
	mkdir -p $YOUTRACK_DB_DIR && \
	mkdir -p /etc/youtrack && \
	mkdir -p $YOUTRACK_USER_HOME && \
	wget -nv https://download.jetbrains.com/charisma/youtrack-$YOUTRACK_VERSION.jar -O $YOUTRACK_HOME/youtrack-$YOUTRACK_VERSION.jar && \
	ln -s $YOUTRACK_HOME/youtrack-$YOUTRACK_VERSION.jar $YOUTRACK_HOME/youtrack.jar

COPY conf/* /etc/youtrack/
COPY docker-entrypoint.sh /docker-entrypoint.sh

VOLUME [ "/etc/youtrack", "/var/lib/youtrack", "/opt/share/youtrack" ]
	
EXPOSE 8080

ENTRYPOINT [ "/docker-entrypoint.sh" ]
