#FROM binhex/arch-base:latest
FROM binhex/arch-base:20170510-01
MAINTAINER binhex

# additional files
###################

# download subsonic
#ADD https://downloads.sourceforge.net/project/subsonic/subsonic/6.1.3/subsonic-6.1.3-standalone.tar.gz?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fsubsonic%2Ffiles%2Fsubsonic%2F6.1.3&ts=1510598673&use_mirror=superb-sea2  /var/subsonic/subsonic.tar.gz
#ADD  https://downloads.sourceforge.net/project/subsonic/subsonic/6.1.4/subsonic-6.1.4-standalone.tar.gz?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fsubsonic%2Ffiles%2Fsubsonic%2F6.1.4%ts=1542050840&use_mirror=superb-sea2 /var/subsonic/subsonic.tar.gz
#https://downloads.sourceforge.net/project/subsonic/subsonic/6.1.2/subsonic-6.1.2-setup.exe?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fsubsonic%2Ffiles%2Flatest%2Fdownload&ts=1544467975&use_mirror=superb-sea2
ADD  https://downloads.sourceforge.net/project/subsonic/subsonic/6.1.5/subsonic-6.1.5-standalone.tar.gz?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fsubsonic%2Ffiles%2Fsubsonic%2F6.1.5%ts=1544467312&use_mirror=superb-sea2 /var/subsonic/subsonic.tar.gz
# download madsonic transcoders
ADD http://www.madsonic.org/download/transcode/20141214_madsonic-transcode_latest_x64.zip /var/subsonic/transcode/transcode.zip
#ADD http://madsonic.org/download/transcode/20161208_madsonic-transcode-linux-x64.zip /var/subsonic/transcode/transcode.zip

# copy start bash script to Subsonic dir (checks ssl enabled/disabled and copies transcoders to madsonic install dir)
ADD start.sh /var/subsonic/start.sh

# add supervisor conf file for app
ADD subsonic.conf /etc/supervisor/conf.d/subsonic.conf

# install app
#############

# install install app using pacman, set perms, cleanup
RUN pacman -Sy --noconfirm && \
	pacman -S libcups jre7-openjdk-headless fontconfig unzip --noconfirm && \
	mkdir -p /var/subsonic/media && \
	mkdir -p /var/subsonic/transcode && \
	tar -xf /var/subsonic/subsonic.tar.gz -C /var/subsonic && \
	rm /var/subsonic/subsonic.tar.gz && \
	unzip /var/subsonic/transcode/transcode.zip -d /var/subsonic/transcode && \
	rm /var/subsonic/transcode/transcode.zip && \
	chown -R nobody:users /var/subsonic && \
	chmod -R 775 /var/subsonic && \	
	yes|pacman -Scc && \	
	rm -rf /usr/share/locale/* && \
	rm -rf /usr/share/man/* && \
	rm -rf /root/* && \
	rm -rf /tmp/*

# force process to run as foreground task
RUN sed -i 's/-jar subsonic-booter-jar-with-dependencies.jar > \${LOG} 2>\&1 \&/-jar subsonic-booter-jar-with-dependencies.jar > \${LOG} 2>\&1/g' /var/subsonic/subsonic.sh

# docker settings
#################

# set env variable for java
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk/jre

# map /config to host defined config path (used to store configuration from app)
VOLUME /config

# map /media to host defined media path (used to read/write to media library)
VOLUME /media

# expose port for http
EXPOSE 4040

# expose port for https
EXPOSE 4050

# run supervisor
################

# run supervisor
CMD ["supervisord", "-c", "/etc/supervisor.conf", "-n"]
