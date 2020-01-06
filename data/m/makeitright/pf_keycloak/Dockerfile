FROM jboss/keycloak:4.8.3.Final

COPY ./theme /opt/jboss/keycloak/themes/make-it-right
ENTRYPOINT [ "/opt/jboss/tools/docker-entrypoint.sh" ]
CMD ["-b", "0.0.0.0"]
