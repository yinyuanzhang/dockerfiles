FROM openjdk:11-jre

ARG APACHEDS_VERSION=${APACHEDS_VERSION:-2.0.0.AM25}

ENV APACHEDS_ACCESS_CONTROL_ENABLED=1 \
    APACHEDS_ADMIN_PASSWORD=secret \
    APACHEDS_DOMAIN_NAME=example \
    APACHEDS_DOMAIN_SUFFIX=com \
    APACHEDS_INSTANCE_NAME=default \
    JMX_EXPORTER_VERSION=0.11.0 \
    DEBIAN_FRONTEND=noninteractive

ADD KEYS /tmp/KEYS

RUN set -x \
    && apt-get update -qq \
    && apt-get install -qq -y --no-install-recommends \
      ca-certificates \
      curl \
      dumb-init \
      gettext-base \
      gnupg \
      ldap-utils \
      netcat \
      procps \
      wget \
    && rm -rf /var/lib/apt/lists/* \
    && curl -sL -o /tmp/apacheds.deb http://www-eu.apache.org/dist//directory/apacheds/dist/${APACHEDS_VERSION}/apacheds-${APACHEDS_VERSION}-amd64.deb \
    && curl -sL -o /tmp/apacheds.deb.asc http://www-eu.apache.org/dist//directory/apacheds/dist/${APACHEDS_VERSION}/apacheds-${APACHEDS_VERSION}-amd64.deb.asc \
    && gpg --no-tty --import /tmp/KEYS \
    && gpg --no-tty --verify --trust-model always /tmp/apacheds.deb.asc /tmp/apacheds.deb \
    && dpkg -i /tmp/apacheds.deb \
    && rm \
      /tmp/apacheds.deb \
      /tmp/apacheds.deb.asc \
      /tmp/KEYS \
    && ln -s /opt/apacheds-${APACHEDS_VERSION}/bin/apacheds /usr/local/bin/ \
    && mv /var/lib/apacheds-${APACHEDS_VERSION} /var/lib/apacheds \
    && sed -ie 's/^INSTANCES_DIRECTORY=.*/INSTANCES_DIRECTORY="\/var\/lib\/apacheds"/g' /opt/apacheds-${APACHEDS_VERSION}/bin/apacheds \
    && curl -sL -o /usr/local/lib/jmx_prometheus_javaagent.jar https://repo1.maven.org/maven2/io/prometheus/jmx/jmx_prometheus_javaagent/${JMX_EXPORTER_VERSION}/jmx_prometheus_javaagent-${JMX_EXPORTER_VERSION}.jar \
    && (echo ; echo "wrapper.java.additional.6=-javaagent:/usr/local/lib/jmx_prometheus_javaagent.jar=8080:/usr/local/etc/jmx-exporter-config.yml") >> /opt/apacheds-${APACHEDS_VERSION}/conf/wrapper.conf \
    && apt-get purge -y --auto-remove \
      curl \
    && cp -a /var/lib/apacheds /var/lib/apacheds.tmpl

COPY ldif/ /ldif/
COPY templates/ /templates/
COPY entrypoint.sh /usr/local/bin/
COPY jmx-exporter-config.yml /usr/local/etc/

EXPOSE 10389 10636 8080
VOLUME ["/var/lib/apacheds"]

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["/usr/local/bin/entrypoint.sh"]
