FROM equemuelcompellon/hadoop-base:latest
MAINTAINER ezra.quemuel@gmail.com

RUN yum install -y zip unzip hostname patch

# Install Maven
ADD http://xenia.sote.hu/ftp/mirrors/www.apache.org/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz /root/
RUN cd /root && tar xfv apache-maven-3.3.9-bin.tar.gz && rm apache-maven-3.3.9-bin.tar.gz

# Download Oozie sources
ADD https://github.com/apache/oozie/archive/release-4.2.0.tar.gz /root/
RUN cd /root && tar xfv release-4.2.0.tar.gz && rm release-4.2.0.tar.gz

# Patch Oozie webapp pom.xml
ADD oozie-4.2.0-webapp-pom.xml.patch /root/oozie-release-4.2.0/webapp/
RUN cd /root/oozie-release-4.2.0/webapp && patch pom.xml oozie-4.2.0-webapp-pom.xml.patch

# Build Oozie. A single RUN because maven dependencies would inflate this layer to gigabytes
RUN cd /root/oozie-release-4.2.0 \
	&& export PATH=/root/apache-maven-3.3.9/bin:$PATH \
	&& mvn clean package assembly:single -DskipTests -P hadoop-2,uber -Dhadoop.version=2.7.1 \
    && mv /root/oozie-release-4.2.0/distro/target/oozie-4.2.0-distro.tar.gz /opt/ && cd /opt && tar xfv oozie-4.2.0-distro.tar.gz && rm oozie-4.2.0-distro.tar.gz \
	&& rm -fR /root/oozie-release-4.2.0 \
	&& rm -fR /root/apache-maven-3.3.9 \
	&& rm -fR /root/.m2

RUN mkdir -p /var/log/oozie && chown -R hdfs /var/log/oozie
RUN mkdir -p /var/lib/oozie/data && chown -R hdfs /var/lib/oozie
RUN ln -s /var/log/oozie /opt/oozie-4.2.0/log
RUN ln -s /var/lib/oozie/data /opt/oozie-4.2.0/data

RUN mkdir /opt/oozie-4.2.0/libext
ADD http://archive.cloudera.com/gplextras/misc/ext-2.2.zip /opt/oozie-4.2.0/libext/
RUN /opt/oozie-4.2.0/bin/oozie-setup.sh prepare-war

ADD https://github.com/jcassee/parameterized-entrypoint/releases/download/0.9.0/entrypoint_linux_amd64 /usr/local/bin/entrypoint
RUN chmod +rx /usr/local/bin/entrypoint
COPY core-site.xml.tmpl /templates/opt/oozie-4.2.0/conf/hadoop-conf/core-site.xml

# Oozie web ports ( API; admin ui )
EXPOSE 11000 11001

RUN chown -R hdfs /opt/oozie-4.2.0
USER hdfs
ENV PATH $PATH:/opt/oozie-4.2.0/bin

ENTRYPOINT ["entrypoint", "--"]
