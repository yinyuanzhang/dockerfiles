FROM centos/httpd-24-centos7

ENV SUMMARY="Vault Documentation" \
    DESCRIPTION="Vault Documentation as it seen in https://www.vaultproject.io \
The image is based on centos/httpd-24-centos7 to run unprivileged httpd container."

LABEL summary="$SUMMARY" \
      description="$DESCRIPTION" \
      io.k8s.description="$DESCRIPTION" \
      io.k8s.display-name="Vault Documentation" \
      io.openshift.expose-services="8080:http,8443:https" \
      io.openshift.tags="documentation,docs,vault" \
      name="dockerized-docs/vault" \
      maintainer="Genadi Postrilko <genadipost@gmail.com>"

user root

# Install httrack to get docs
RUN yum -y install httrack

USER default

RUN mkdir -p /opt/app-root/src/vault-website \
    && cd /opt/app-root/src/vault-website \
    && httrack https://www.vaultproject.io

RUN cp -R /opt/app-root/src/vault-website/www.vaultproject.io/* /var/www/html/ \
    && rm -rf /opt/app-root/src/vault-website

CMD ["/usr/bin/run-httpd"]
