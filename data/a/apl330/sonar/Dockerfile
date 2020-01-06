from ubuntu:12.04
maintainer zhaizhijun, zacker330@gmail.com

#ENV http_proxy http://127.0.0.1:8087
#ENV https_proxy https://127.0.0.1:8087
#RUN echo "Acquire::http::proxy \"proxy_server:port\";" >> /etc/apt/apt.conf
#RUN echo "Acquire::https::proxy \"proxy_server:port\";" >> /etc/apt/apt.conf


# Because docker replaces /sbin/init: https://github.com/dotcloud/docker/issues/1024 
RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -s /bin/true /sbin/initctl

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list


RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y dpkg
RUN apt-get install -y openjdk-6-jre
RUN export JAVA_HOME=/usr/lib/jvm/java-6-openjdk


RUN apt-get install -y wget

RUN wget http://dist.sonar.codehaus.org/sonarqube-4.1.zip

RUN apt-get install -y unzip
RUN unzip sonarqube-4.1.zip

RUN mv sonarqube-4.1 /opt

#RUN /opt/sonarqube-4.1/bin/linux-x86-64/sonar.sh start
#RUN /opt/sonarqube-4.1/bin/linux-x86-64/sonar.sh console


EXPOSE 22

CMD ["/opt/sonarqube-4.1/bin/linux-x86-64/sonar.sh", "console", "/bin/bash"]
