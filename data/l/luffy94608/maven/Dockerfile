FROM maven:3.5.3-jdk-7

ENV M2_HOME=/opt/tool/maven

COPY add_settings.xml /usr/share/maven/ref/custom_settings.xml
RUN cat /usr/share/maven/ref/custom_settings.xml >> /usr/share/maven/ref/settings-docker.xml
