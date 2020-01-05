FROM owasp/modsecurity:2.9-apache-ubuntu
LABEL maintainer="Chaim Sanders <chaim.sanders@gmail.com>"

ARG COMMIT=v3.1/fixed
ARG REPO=vshn/owasp-modsecurity-crs
ENV PARANOIA=1

RUN apt-get update && \
  apt-get -y install python git ca-certificates iproute2 && \
  mkdir /opt/owasp-modsecurity-crs && \
  cd /opt/owasp-modsecurity-crs && \
  git init && \
  git remote add origin https://github.com/${REPO} && \
  git fetch --depth 1 origin ${BRANCH} && \
  git checkout ${COMMIT} && \
  mkdir -pv /etc/apache2/modsecurity.d && \
  cp -R /opt/owasp-modsecurity-crs/ /etc/apache2/modsecurity.d/owasp-crs/ && \
  mv /etc/apache2/modsecurity.d/owasp-crs/crs-setup.conf.example /etc/apache2/modsecurity.d/owasp-crs/crs-setup.conf && \
  cd /etc/apache2/modsecurity.d && \
  mv -v /etc/modsecurity.d/* . && \
  sed -i /etc/apache2/mods-available/modsecurity.conf \
    -e 's|/etc/modsecurity.d/|/etc/apache2/modsecurity.d/|' && \
  printf "include modsecurity.d/owasp-crs/crs-setup.conf\ninclude modsecurity.d/owasp-crs/rules/*.conf" > include.conf && \
  sed -i 's/SecRuleEngine DetectionOnly/SecRuleEngine On/g' modsecurity.conf && \
  a2enmod proxy proxy_http

COPY proxy.conf           /etc/apache2/modsecurity.d/proxy.conf
COPY docker-entrypoint.sh /

EXPOSE 80

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["apachectl", "-D", "FOREGROUND"]
