FROM openjdk:8-jre-alpine

ENV HOME=/opt/app-root \
STI_SCRIPTS_PATH=/usr/libexec/s2i \
PATH=$PATH:$STI_SCRIPTS_PATH \
AB_JOLOKIA_PASSWORD_RANDOM="true" \
AB_JOLOKIA_AUTH_OPENSHIFT="true"

ENV JAVA_TOOL_OPTIONS=-Duser.home=${HOME}

LABEL io.k8s.description="Platform for running plain Java applications (fat-jar) " \
      io.k8s.display-name="Java Applications" \
      io.openshift.expose-services="8080:http" \
      io.openshift.tags="builder,java,openjdk8,alpine" \
      io.openshift.s2i.scripts-url=image://${STI_SCRIPTS_PATH}

USER root

# Add user
RUN  mkdir -p ${HOME} \
&& mkdir -p ${STI_SCRIPTS_PATH} \
&& adduser -s /bin/sh -u 1001 -G root -h ${HOME} -S -D default \
&& chown -R 1001:0 ${HOME}


# Jolokia agent
RUN mkdir -p /opt/jolokia/etc \
&& wget http://central.maven.org/maven2/org/jolokia/jolokia-jvm/1.3.6/jolokia-jvm-1.3.6-agent.jar -O /opt/jolokia/jolokia.jar
ADD jolokia-opts /opt/jolokia/jolokia-opts
RUN chmod 444 /opt/jolokia/jolokia.jar \
 && chmod 755 /opt/jolokia/jolokia-opts \
 && chmod -R 775 /opt/jolokia/etc


EXPOSE 8778

COPY ./s2i/bin/ ${STI_SCRIPTS_PATH}

RUN chmod -R 755 ${STI_SCRIPTS_PATH}


USER 1001

WORKDIR ${HOME}

EXPOSE 8080


CMD ${STI_SCRIPTS_PATH}/usage


