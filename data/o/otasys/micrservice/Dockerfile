FROM otasys/java:1.8.0_66

WORKDIR /opt

RUN wget http://ftp.ps.pl/pub/apache/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz && \
	tar xvf apache-maven-3.3.9-bin.tar.gz && \
	rm -rf apache-maven-3.3.9-bin.tar.gz && \
	update-alternatives  --install /usr/bin/mvn mvn /opt/apache-maven-3.3.9/bin/mvn 1 && \
	update-alternatives  --set mvn /opt/apache-maven-3.3.9/bin/mvn

ADD settings.xml settings.xml
ADD extensions.xml extensions.xml
ADD setup.sh setup.sh

EXPOSE 8080

CMD ["sh", "setup.sh"]
