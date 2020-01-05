FROM java

ADD . /ivid
RUN cd /ivid
RUN wget http://ffmpeg.org/releases/ffmpeg-3.0.1.tar.bz2
RUN tar -jxvf /ffmpeg-3.0.1.tar.bz2
RUN apt-get update
RUN apt-get -y install maven
RUN apt-get -y install tomcat7
RUN wget http://s3.amazonaws.com/wipro-digital-ivid/offlinepkgr.zip
RUN apt-get install unzip 
RUN pwd
RUN ls -l
RUN unzip /offlinepkgr.zip -d /ivid/encodingService/offlinepkgr
RUN mkdir /var/lib/tomcat7/webapps/savevideo
RUN mvn -version
RUN mvn package -f /ivid/encodingService/pom.xml
RUN ls -l /ivid/encodingService/target
RUN cp /ivid/encodingService/target/uploadvideo.war /var/lib/tomcat7/webapps
CMD ["/var/lib/tomcat7/bin/startup.sh"]
 