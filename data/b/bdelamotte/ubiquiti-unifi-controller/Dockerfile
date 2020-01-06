FROM library/ubuntu:14.04
RUN echo 'deb http://www.ubnt.com/downloads/unifi/debian stable ubiquiti' | sudo tee -a /etc/apt/sources.list.d/100-ubnt.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv C0A52C50 && apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10
RUN apt-get update && apt-get install -y \
      unifi \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*
EXPOSE 8080
EXPOSE 8443
CMD ["/usr/bin/jsvc", "-nodetach" , "-home", "/usr/lib/jvm/java-6-openjdk-amd64", "-cp", "/usr/share/java/commons-daemon.jar:/usr/lib/unifi/lib/ace.jar", "-pidfile", "/var/run/unifi/unifi.pid", "-procname", "unifi", "-outfile", "SYSLOG", "-errfile", "SYSLOG", "-Djava.awt.headless=true", "-Dfile.encoding=UTF-8", "-Xmx1024M", "com.ubnt.ace.Launcher", "start"]
