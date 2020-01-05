FROM sonarqube:latest
RUN set -x \
  && wget https://github.com/stevespringett/dependency-check-sonar-plugin/releases/download/1.2.1/sonar-dependency-check-plugin-1.2.1.jar -P /opt/sonarqube/extensions/plugins/ \
  && chown -R sonarqube:sonarqube /opt/sonarqube/extensions/plugins/
