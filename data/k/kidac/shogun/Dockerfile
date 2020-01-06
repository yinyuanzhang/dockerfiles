FROM kidac/tomcat:8.5.45.1936

LABEL de.kdac.shogun.maintainer = "Claus Böhmer" \
      de.kdac.shogun.authors = "eso@bistum-eichstaett.de" \
      de.kdac.shogun.url = "https://hub.docker.com/r/kidac/shogun" \
      de.kdac.shogun.documentation = "https://hub.docker.com/r/kidac/shogun" \
      de.kdac.shogun.source = "https://github.com/kidac/shogun" \
      de.kdac.shogun.version = "2.0" \
      de.kdac.shogun.vendor = "KDAC - https://ews.kdac.de" \
      de.kdac.shogun.licenses = "https://github.com/terrestris/shogun-core/blob/master/LICENSE.md" \
      de.kdac.shogun.title = "Shogun (KDAC Version)" \
      de.kdac.shogun.description = "Adapted Shogun Dockerfile used by KDAC"

ENV SHOGUN_VERSION=2.0

WORKDIR /tmp

RUN apk upgrade --update --no-cache \
 && apk add --no-cache curl openssl libressl2.7-libcrypto nss zip \
 && rm -rf $CATALINA_HOME/webapps/ROOT \
 && rm -rf $CATALINA_HOME/webapps/docs \
 && rm -rf $CATALINA_HOME/webapps/examples \
 && rm -rf $CATALINA_HOME/webapps/host-manager \
 && rm -rf $CATALINA_HOME/webapps/manager

COPY entrypoint.sh /entrypoint.sh
COPY binary/gis.war /opt/tomcat/webapps/

ENTRYPOINT /entrypoint.sh
