FROM hmcts/cnp-java-base:openjdk-8u181-jre-alpine3.8-1.0

# Mandatory!
ENV APP back-office.jar
ENV APPLICATION_TOTAL_MEMORY 1024M
ENV APPLICATION_SIZE_ON_DISK_IN_MB 66

COPY build/libs/$APP /opt/app/

HEALTHCHECK --interval=10s --timeout=10s --retries=10 CMD http_proxy="" wget -q --spider http://localhost:4104/health || exit 1

EXPOSE 4104

