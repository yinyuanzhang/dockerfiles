FROM jboss/keycloak:4.5.0.Final

USER root

COPY scripts /opt/jboss/tools/

RUN mkdir -p /etc/x509/https

ENTRYPOINT ["/opt/jboss/tools/myEntryPoint.sh"]
