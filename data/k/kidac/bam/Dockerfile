FROM alpine:latest

LABEL de.kdac.bam.maintainer = "Claus Böhmer"\
      de.kdac.bam.authors = "eso@bistum-eichstaett.de" \
      de.kdac.bam.url = "https://hub.docker.com/r/kidac/bam" \
      de.kdac.bam.documentation = "https://hub.docker.com/r/kidac/bam" \
      de.kdac.bam.source = "https://github.com/kidac/bam" \
      de.kdac.bam.version = "1.0" \
      de.kdac.bam.vendor = "KDAC - https://ews.kdac.de" \
      de.kdac.bam.licenses = "" \
      de.kdac.bam.title = "Backup and Maintenance (KDAC Version)" \
      de.kdac.bam.description = "Backup and Maintenance Dockerfile used by https://ews.kdac.de"

RUN apk --no-cache upgrade \
 && apk add --no-cache postgresql-client openldap openldap-clients openldap-overlay-memberof openldap-overlay-refint openldap-overlay-deref openldap-back-mdb openldap-overlay-ppolicy

ENV RUN_USER=daemon RUN_GROUP=daemon

RUN mkdir -p /mnt/bam /mnt/crowd /mnt/confluence /mnt/bitbucket /mnt/bamboo /mnt/jsd /mnt/jsw /mnt/ssl /mnt/openldap /mnt/postgresql

COPY backup_atlassian backup_databases backup_ldap maintenance restore_atlassian restore_databases restore_ldap /usr/bin/
COPY backup_atlassian backup_databases backup_ldap maintenance /etc/periodic/daily/
COPY maintenance /etc/periodic/weekly/
COPY slapd.conf /etc/openldap/slapd.conf

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
