FROM cptactionhank/atlassian-jira

# Configuration variables.

ENV JIRA_HOME     /var/atlassian/jira
ENV JIRA_INSTALL  /opt/atlassian/jira
ENV JIRA_VERSION  7.7.0

ENV SUMMARY="Atlassian Jira Core Docker Container" \
    DESCRIPTION="Atlassian Jira $JIRA_VERSION available as docker container is the core platform for \
the Jira issue tracker."

LABEL summary="$SUMMARY" \
      description="$DESCRIPTION" \
      io.k8s.description="$DESCRIPTION" \
      io.k8s.display-name="Atlassian Jira $JIRA_VERSION" \
      io.openshift.tags="other" \
      maintainer="John McCawley <john.mccawley@thedigitalgarage.io>" \
      usage="docker run thedigitalgarage/atlassian-jira"

USER root

# Setup initial home directory structure.

RUN set -x \
    && chown -R 1001:0  "${JIRA_HOME}" \
    && chown -R 1001:0  "${JIRA_INSTALL}/conf" \
    && chown -R 1001:0  "${JIRA_INSTALL}/logs" \
    && chown -R 1001:0  "${JIRA_INSTALL}/temp" \
    && chown -R 1001:0  "${JIRA_INSTALL}/work"

# Expose default HTTP connector port.
EXPOSE 8080

# Use the standard UID for openshift.
USER 1001

# Run Atlassian JIRA as a foreground process by default.
CMD ["/opt/atlassian/jira/bin/catalina.sh", "run"]
