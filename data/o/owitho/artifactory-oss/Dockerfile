FROM docker.bintray.io/jfrog/artifactory-oss:6.5.2
USER root
RUN echo "Asia/Shanghai" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata
USER artifactory
