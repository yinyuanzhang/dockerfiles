FROM openjdk:8-slim

LABEL maintainer="Pietrangelo Masala <p.masala@entando.com>"

#Environment Variables
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV JRE_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
ENV MAVEN_HOME=/usr/share/maven

RUN apt-get update && apt-get install --no-install-recommends -y maven imagemagick git acl \
&&  apt-get autoclean -y \
&& mkdir -p /opt/entando && mkdir -p /opt/entando/.m2/repository && chown -R 1001:1001 /opt/entando && chmod 0777 -R /opt/entando 

# run as user 1001 for OpenShift security constraints
USER 1001

# Install entando dependencies (core, components, archetypes)
RUN cd /opt/entando \
&& git clone https://github.com/entando/entando-core.git \
&& git clone https://github.com/entando/entando-components.git \
&& git clone https://github.com/entando/entando-archetypes.git \
&& cd entando-core && mvn -Dmaven.repo.local=/opt/entando/.m2/repository install -DskipTests && mvn clean && cd .. \
&& cd entando-components && mvn -Dmaven.repo.local=/opt/entando/.m2/repository install -DskipTests && mvn clean && cd .. \
&& cd entando-archetypes && mvn -Dmaven.repo.local=/opt/entando/.m2/repository install -DskipTests && mvn clean && cd .. \
&& chmod 777 -R /opt/entando/.m2/repository/ \
&& rm -rf entando-*
