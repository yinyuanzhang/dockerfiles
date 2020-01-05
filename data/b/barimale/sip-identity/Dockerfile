FROM jboss/keycloak:8.0.1
USER 1001
ADD import-realm.json /opt/jboss/keycloak/
ENTRYPOINT [ "/opt/jboss/tools/docker-entrypoint.sh" ]
CMD ["-b", "0.0.0.0", "-Dkeycloak.migration.action=import -Dkeycloak.migration.provider=singleFile -Dkeycloak.migration.file=/opt/jboss/keycloak/import-realm.json -Dkeycloak.migration.strategy=OVERWRITE_EXISTING"]