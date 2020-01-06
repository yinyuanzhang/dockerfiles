FROM cloudbees/java-build-tools:2.5.0

MAINTAINER Sébastien PAYEN <s.payen@nouvellemarque.com>

USER root

# Install Liferay Portal
RUN mkdir -p /opt && \
    curl -SL https://sourceforge.net/projects/lportal/files/Liferay%20Portal/7.2.0%20GA1/liferay-ce-portal-tomcat-7.2.0-ga1-20190531153709761.tar.gz | tar -zxC /opt && \
    ln -s /opt/liferay-portal-7.2.0-ga1 /opt/liferay-portal && \
    ln -s /opt/liferay-portal/tomcat-9.0.17 /opt/liferay-portal/tomcat && \
    chown -R 1000:1000 /opt/liferay-portal/*

ENTRYPOINT ["/bin/sh"]
