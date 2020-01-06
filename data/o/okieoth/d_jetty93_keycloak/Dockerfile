FROM jetty:9.3


ENV ADAPTER_DOWNLOAD_URL https://downloads.jboss.org/keycloak/2.5.1.Final/adapters/keycloak-oidc/keycloak-jetty93-adapter-dist-2.5.1.Final.tar.gz

RUN cd /usr/local/jetty && \
    curl -SL "$ADAPTER_DOWNLOAD_URL" -o keycloak_adapter.tgz && \
    tar -xzf keycloak_adapter.tgz && \
    chown -R 501:staff lib/keycloak && chown 501:staff modules/keycloak.mod && \
    cd /var/lib/jetty && java -jar $JETTY_HOME/start.jar --add-to-startd=keycloak

EXPOSE 8080
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["java","-jar","/usr/local/jetty/start.jar"]

