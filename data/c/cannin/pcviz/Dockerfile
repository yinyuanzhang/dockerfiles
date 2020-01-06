FROM ubuntu:14.04.3

##### UBUNTU
# Update Ubuntu and add extra repositories
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install software-properties-common

# Install basic commands
RUN apt-get -y install links nano wget git maven

# Here comes the tomcat installation
RUN apt-get -y install openjdk-7-jdk tomcat7

# Make temporary directory 
RUN mkdir -p /data/pcviz 

RUN git clone https://github.com/PathwayCommons/pcviz.git

RUN wget -O /pcviz/src/main/resources/spring/pcviz.properties https://raw.githubusercontent.com/cannin/docker-pcviz/master/pcviz.properties

RUN cd /pcviz; mvn clean install

# Add war file to tomcat and make root project
RUN rm -rf /var/lib/tomcat7/webapps/ROOT
RUN cp -f /pcviz/target/pcviz-*.war /var/lib/tomcat7/webapps/ROOT.war

# NOTE: TEMPORARY HACK
RUN cp -f /pcviz/target/pcviz-*.war /var/lib/tomcat7/webapps/pcviz.war

# Expose the default tomcat port
EXPOSE 8080

ENV CATALINA_HOME /usr/share/tomcat7
ENV CATALINA_BASE /var/lib/tomcat7
ENV CATALINA_SH /usr/share/tomcat7/bin/catalina.sh

# Download cache files
RUN wget -O /data/pcviz.tar.gz https://www.dropbox.com/s/l0up7fbzuq8hc9r/pcviz.tar.gz?dl=0
RUN cd /data; tar xvfz pcviz.tar.gz 

RUN wget -O /data/pcviz/hgnc.txt "http://www.genenames.org/cgi-bin/hgnc_downloads?col=gd_app_sym&col=gd_aliases&col=md_prot_id&status=Approved&status_opt=2&where=&order_by=gd_hgnc_id&format=text&limit=&hgnc_dbtag=on&submit=submit"

RUN wget -O /data/pcviz/blacklist.txt "http://www.pathwaycommons.org/pc2/downloads/blacklist.txt"

# Start the tomcat (and leave it hanging)
CMD /usr/share/tomcat7/bin/catalina.sh run
