FROM jenkins
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"
ENV ANT_HOME=/opt/ant
USER root
COPY plugins.txt /usr/share/jenkins/ref/
COPY custom.groovy /usr/share/jenkins/ref/init.groovy.d/custom.groovy
COPY apicreateJob.sh /usr/share/apicreateJob.sh
COPY config_comment.xml /usr/share/config_comment.xml
COPY config_deploy.xml /usr/share/config_deploy.xml
COPY choices.txt /usr/share/choices.txt
RUN chmod 777 /usr/share/apicreateJob.sh
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt
RUN mkdir -p /var/jenkins_home/workspace
WORKDIR /tmp
RUN wget --no-check-certificate --no-cookies http://archive.apache.org/dist/ant/binaries/apache-ant-1.10.3-bin.tar.gz \
    && wget --no-check-certificate --no-cookies http://archive.apache.org/dist/ant/binaries/apache-ant-1.10.3-bin.tar.gz.sha512 \
    && echo "$(cat apache-ant-1.10.3-bin.tar.gz.sha512) apache-ant-1.10.3-bin.tar.gz" | sha512sum -c \
    && tar -zvxf apache-ant-1.10.3-bin.tar.gz -C /opt/ \
    && ln -s /opt/apache-ant-1.10.3 /opt/ant \
    && rm -f apache-ant-1.10.3-bin.tar.gz \
    && rm -f apache-ant-1.10.3-bin.tar.gz.sha512
COPY lib/ant-contrib-0.6.jar /opt/ant/lib
COPY lib/jsch-0.1.54.jar /opt/ant/lib