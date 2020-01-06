FROM lsiobase/ubuntu:xenial

# set labels
LABEL maintainer="Nightah"

# package versions
ARG OKTA_LDAP_VERSION="05.04.06"

# copy local files
COPY root/ /

# install packages
RUN \
 apt-get update && \
    curl -o /tmp/okta-ldap.deb -L https://download.okta.com/static/ldap-agent/OktaLDAPAgent-${OKTA_LDAP_VERSION}_amd64.deb && \
    dpkg -i /tmp/okta-ldap.deb && \
 mv /opt/Okta/OktaLDAPAgent/conf/logback.xml /opt/Okta/OktaLDAPAgent/logback-default.xml && \
 echo "**** cleanup ****" && \
 apt-get clean && \
 rm -rf \
    /tmp/* \
    /var/lib/apt/lists/* \
    /var/tmp/*

# volumes
VOLUME /opt/Okta/OktaLDAPAgent/conf