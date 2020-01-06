FROM centos:7

MAINTAINER Ricardo Santana <rsantana@kenos.com.br>

RUN yum -y install java-1.6.0-openjdk-devel which \
	&& curl https://ufpr.dl.sourceforge.net/project/ireport/iReport/iReport-5.6.0/iReport-5.6.0.tar.gz --output /iReport-5.6.0.tar.gz \
	&& tar zxvf iReport-5.6.0.tar.gz \
	&& rm -rf /var/cache/yum \
	&& rm -rf /iReport-5.6.0.tar.gz

ENV JAVA_HOME /usr/lib/jvm/java-openjdk

CMD [ "/iReport-5.6.0/bin/ireport" ]