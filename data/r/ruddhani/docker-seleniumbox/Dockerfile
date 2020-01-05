FROM centos:7
MAINTAINER ruddhani

USER root

RUN yum install -y sudo wget git unzip Xvfb

RUN yum install -y centos-release-scl

RUN yum install -y java-1.8.0-openjdk && \
    cp /etc/profile /etc/profile_backup && \
    echo 'export JAVA_HOME=/usr/lib/jvm/jre-1.8.0-openjdk-1.8.0.161-0.b14.el7_4.x86_64' | sudo tee -a /etc/profile && \
    echo 'export JRE_HOME=/usr/lib/jvm/jre' | sudo tee -a /etc/profile && \
    source /etc/profile

RUN yum install -y java-1.8.0-openjdk-devel -y

COPY config/google-chrome.repo /etc/yum.repos.d/google-chrome.repo

RUN yumdownloader google-chrome-stable && \
	repoquery --requires --resolve google-chrome-stable | xargs sudo yum -y install && \
	wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm && \
	yum install -y ./google-chrome-stable_current_*.rpm

RUN cd / && mkdir app/ && cd /app/ && \
	git clone https://github.com/ruddhani/vagrant-seleniumbox.git && \
	ls -la

RUN	mv /app/vagrant-seleniumbox /app/seleniumdist && cd /app/seleniumdist && \
	unzip chromedriver_linux64.zip && \
	mv chromedriver /usr/bin/chromedriver -f && sudo chmod a+x /usr/bin/chromedriver && \
	chmod a+x /app/seleniumdist/lib/* && \
	# chmod a+x selenium-server-standalone-3.11.0.jar && \
	ls -la && \
	# wget http://www.java2s.com/Code/JarDownload/testng/testng-6.0.1.jar.zip && \
	# mv testng-6.0.1.jar.zip /app/seleniumdist/lib/ -f && cd /app/seleniumdist/lib/ && \
	# unzip testng-6.0.1.jar.zip && \	
	wget http://selenium-release.storage.googleapis.com/2.48/selenium-java-2.48.2.zip && \
	unzip selenium-java-2.48.2.zip && \
	# mv selenium-2.48.2/* /app/seleniumdist/lib/ -f && \
	# mv libs/* /app/seleniumdist/lib/ -f && \
	chmod a+x /app/seleniumdist/lib/* && \
	wget http://central.maven.org/maven2/com/google/auto/service/auto-service/1.0-rc4/auto-service-1.0-rc4.jar && \
	chmod a+x auto-service-1.0-rc4.jar && \
	mv auto-service-1.0-rc4.jar /app/seleniumdist/lib/ -f && \
	ls -la && \
	ln -s /app/seleniumdist/selenium-server.sh /usr/bin/seleniumserver && \
	chmod a+x runseleniumng.sh



COPY config/seleniumserver.sh /app/seleniumdist
COPY config/seleniumserver.sh /etc/init.d/seleniumserver

RUN chmod 755 /etc/init.d/seleniumserver && \
	chkconfig --add seleniumserver

RUN yum clean all && \
	rm -rf /var/cache/yum && \
    groupadd -f seluser && \
    useradd --no-log-init --no-create-home --shell /usr/sbin/nologin -g seluser seluser && \
    mkdir /tmp/session && \
    chmod 0777 /tmp/session && \
	chown -R seluser:seluser /app

USER seluser

EXPOSE 22 9000 4545 9515
# this is not working
# CMD service seleniumserver start
# this is working in travis build
# CMD /usr/bin/seleniumserver start
