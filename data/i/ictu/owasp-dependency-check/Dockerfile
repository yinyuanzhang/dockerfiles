FROM owasp/dependency-check:5.2.2

LABEL maintainer="Dick Snel <dick.snel@ictu.nl>"

ENV PROJECT_NAME "generic"

USER root

RUN mkdir -p /tmp/reports
RUN mkdir -p /tmp/dependency-check/data
RUN /usr/share/dependency-check/bin/dependency-check.sh --updateonly --data /tmp/dependency-check/data

ADD docker-entrypoint.sh /tmp/docker-entrypoint.sh

RUN chmod +x /tmp/docker-entrypoint.sh

#USER dependencycheck

VOLUME ["/tmp/dependency-check/data"]

WORKDIR /tmp/reports

ENTRYPOINT ["/tmp/docker-entrypoint.sh"]
