FROM michaelpc/openshift:latest

USER 0

ADD files /tmp/setup

RUN sh /tmp/setup/install.sh

WORKDIR /app

USER 1000

ENV IN_RUN_NEW_DB_CERT new-db-cert
ENV IF_IN_RUN_NEW_DB_CERT 'is_dir($ENV{DB_CERT_DIR} // q{/app/cockroach-certs})'

ENV JUST_RUN_NEW_ADMIN new-admin wait yes
ENV IF_JUST_RUN_NEW_ADMIN 'is_dir($ENV{DB_CERT_DIR} // q{/app/cockroach-certs}) && has_env(qr/^DB_ADMIN_/)'

ENV KEEP_RUN_DB run-db
ENV IF_KEEP_RUN_DB 'is_dir($ENV{DB_CERT_DIR} // q{/app/cockroach-certs}) && is_dir($ENV{DB_STORAGE} // q{/app/cockroach-data}) && !is_empty($ENV{DB_DOMAIN})'

EXPOSE 26257
EXPOSE 8080
