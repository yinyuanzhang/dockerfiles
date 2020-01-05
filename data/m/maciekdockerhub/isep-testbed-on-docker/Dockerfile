FROM        java:8-jdk

ENV         JAVA_HOME         /usr/lib/jvm/java-8-openjdk-amd64
ENV         GLASSFISH_HOME    /usr/local/glassfish4
ENV         PATH              $PATH:$JAVA_HOME/bin:$GLASSFISH_HOME/bin

RUN         apt-get update && \
            apt-get install -y curl unzip zip inotify-tools && \
	    	apt-get install -y less && \
	    	apt-get install -y vim && \
	    	apt-get install -y multitail && \
            rm -rf /var/lib/apt/lists/* 
		

#RUN         curl -L -o /tmp/glassfish-4.1.zip http://download.java.net/glassfish/4.1/release/glassfish-4.1.zip && \
RUN         curl -L -o /tmp/glassfish-4.1.zip http://download.oracle.com/glassfish/4.1.1/nightly/latest-glassfish.zip && \
            unzip /tmp/glassfish-4.1.zip -d /usr/local && \
            rm -f /tmp/glassfish-4.1.zip

RUN  curl -L -o /tmp/eclipselink-plugins-2.6.2.v20151217-774c696.zip http://www.eclipse.org/downloads/download.php?file=/rt/eclipselink/releases/2.6.2/eclipselink-plugins-2.6.2.v20151217-774c696.zip&mirror_id=1190 

EXPOSE      8080 4848 8181 1521 50048 50086

WORKDIR     /tmp/

ADD isep-andromeda-domain-setup.sh /tmp/

ADD eclipselink-update.sh /tmp/
ADD isep-core-impl-0.1-SNAPSHOT-stage.war /usr/local/
ADD ojdbc7_g.jar /tmp/

ADD eclipselink-plugins-2.6.2.v20151217-774c696.zip /tmp/
RUN ["/bin/bash", "eclipselink-update.sh" , "eclipselink-plugins-2.6.2.v20151217-774c696.zip"]

#ADD eclipselink_full /usr/local/glassfish4/glassfish/modules/

#ADD ojdbc7.jar /usr/local/glassfish4/glassfish/modules/
RUN echo "10.11.131.124 tytan" >> /etc/hosts; echo "172.17.0.2 baza" >> /etc/hosts; cat /etc/hosts; /bin/bash isep-andromeda-domain-setup.sh;

ADD ojdbc7.jar /usr/local/glassfish4/glassfish/domains/isep-andromeda/lib/
#ADD setupAndDeploy.sh /usr/local/
#ADD passfile /usr/local/

VOLUME /usr/local/glassfish4/glassfish/domains/
WORKDIR /usr/local/glassfish4/glassfish/bin

env PATH /usr/local/glassfish4/glassfish/bin:$PATH
