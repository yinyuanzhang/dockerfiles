FROM adoptopenjdk/openjdk8:alpine-slim

LABEL de.kdac.portal.maintainer = "Claus Böhmer" \
      de.kdac.portal.authors = "eso@bistum-eichstaett.de" \
      de.kdac.portal.url = "https://hub.docker.com/r/kidac/tomcat" \
      de.kdac.portal.documentation = "https://hub.docker.com/r/kidac/tomcat" \
      de.kdac.portal.source = "https://github.com/kidac/tomcat" \
      de.kdac.portal.version = "7.1.3.4" \
      de.kdac.portal.vendor = "KDAC - https://ews.kdac.de" \
      de.kdac.portal.licenses = "https://www.atlassian.com/legal/software-license-agreement, https://www.atlassian.com/legal/privacy-policy" \
      de.kdac.portal.title = "Tomcat (KDAC Version)" \
      de.kdac.portal.description = "Adapted Tomcat Dockerfile used by KDAC"

ENV PORTAL_MAJOR_VERSION=7.1.3
ENV PORTAL_VERSION=ga4-20190508171117552 
ENV CATALINA_HOME=/opt/portal/tomcat

RUN apk upgrade --update --no-cache \
 && apk add --no-cache curl ttf-dejavu p7zip

WORKDIR /opt

RUN curl -jkSL -o /opt/portal.7z https://sourceforge.net/projects/lportal/files/Liferay%20Portal/7.1.3%20GA4/liferay-ce-portal-tomcat-7.1.3-ga4-20190508171117552.7z/download \
 && p7zip -d /opt/portal.7z \
 && mv /opt/liferay-ce-portal-7.1.3-ga4/ /opt/portal \
 && mv /opt/portal/tomcat-9.0.17 /opt/portal/tomcat \
 && mv /opt/portal/tomcat/webapps/ROOT /opt/portal/tomcat/webapps/portal \
 && mv /opt/portal/tomcat/conf/Catalina/localhost/ROOT.xml /opt/portal/tomcat/conf/Catalina/localhost/portal.xml \
 && rm -rf /opt/portal/osgi/state

EXPOSE 8080

COPY entrypoint.sh              /entrypoint.sh
COPY portal-ext.properties      /opt/portal/tomcat/webapps/portal/WEB-INF/classes/portal-ext.properties

ENTRYPOINT /entrypoint.sh

WORKDIR $CATALINA_HOME
