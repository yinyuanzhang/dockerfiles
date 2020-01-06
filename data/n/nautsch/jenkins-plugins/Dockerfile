FROM ubuntu:14.04

ENV JENKINS_HOME_PLUGINS /var/jenkins_home/plugins

# curl https://raw.githubusercontent.com/hgomez/devops-incubator/master/forge-tricks/batch-install-jenkins-plugins.sh -o batch-install-jenkins-plugins.sh
ADD batch-install-jenkins-plugins.sh /batch-install-jenkins-plugins.sh
ADD incl-plugins.txt /incl-plugins.txt
ADD excl-plugins.txt /excl-plugins.txt

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl python ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p "$JENKINS_HOME_PLUGINS" \
    && chmod +x /batch-install-jenkins-plugins.sh \
    && sync \
    && /batch-install-jenkins-plugins.sh -p /incl-plugins.txt -e /excl-plugins.txt -d "$JENKINS_HOME_PLUGINS" \
    && addgroup --gid 1000 jenkins \
    && adduser --system --disabled-password --disabled-login --no-create-home --uid 1000 --gid 1000 --shell /bin/bash jenkins \
    && chown -R jenkins:jenkins "$JENKINS_HOME_PLUGINS"

USER jenkins

VOLUME "$JENKINS_HOME_PLUGINS"

CMD ["echo", "Plugin container for Jenkins"]

