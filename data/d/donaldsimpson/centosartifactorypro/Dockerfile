FROM centos:7

COPY tini /bin/
COPY bintray-jfrog-artifactory-pro-rpms.repo /etc/yum.repos.d/

RUN chmod +x /bin/tini && \
    yum update -y && \
    yum install -y java-1.8.0-openjdk-devel jfrog-artifactory-pro && \
    yum clean all && rm -rf /var/cache/yum/*
    
EXPOSE 8081

USER artifactory
 
ENTRYPOINT ["/bin/tini", "/opt/jfrog/artifactory/tomcat/bin/catalina.sh", "run"]
