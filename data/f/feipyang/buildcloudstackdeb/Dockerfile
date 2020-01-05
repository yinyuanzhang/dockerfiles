# Based on Debian Wheezy
FROM ubuntu:trusty

# We want to record start time
RUN date>/root/time.txt
# Install Packages, via apt-get. 
RUN apt-get update && apt-get install -y \
	wget \
	vim \
	python-software-properties \
	ant \
	debhelper \
	openjdk-7-jdk \
	tomcat6 \
	libws-commons-util-java \
	genisoimage \
	python-mysqldb \
	libcommons-codec-java \
	libcommons-httpclient-java \
 	liblog4j1.2-java \
	maven && rm -rf /var/lib/apt/lists/*

# Now make the code directory and get the source code
RUN mkdir -p /opt/Code/
RUN wget -P /opt/Code/ http://www.eu.apache.org/dist/cloudstack/releases/4.5.2/apache-cloudstack-4.5.2-src.tar.bz2
RUN tar xjvf /opt/Code/apache-cloudstack-4.5.2-src.tar.bz2 -C /opt/Code/
RUN cd /opt/Code/apache-cloudstack-4.5.2-src/ && mvn -P deps -Dnonoss -DskipTests=true && dpkg-buildpackage -uc -us
RUN date>>/root/time.txt
