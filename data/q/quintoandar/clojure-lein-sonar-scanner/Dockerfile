FROM clojure:lein-2.8.3

ENV SONAR_SCANNER_CLI_VERSION=3.3.0.1492 \
    SONAR_SCANNER_CLI_HOME=/opt/sonar-scanner

RUN set -x \
    && (gpg --batch --keyserver ha.pool.sks-keyservers.net --recv-keys F1182E81C792928921DBCAB4CFCA4A29D26468DE \
	    || gpg --batch --keyserver ipv4.pool.sks-keyservers.net --recv-keys F1182E81C792928921DBCAB4CFCA4A29D26468DE) \
    && cd /opt \
    && curl -o sonar-scanner-cli.zip -fSL https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-$SONAR_SCANNER_CLI_VERSION.zip \
    && curl -o sonar-scanner-cli.zip.asc -fSL https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-$SONAR_SCANNER_CLI_VERSION.zip.asc \
    && gpg --batch --verify sonar-scanner-cli.zip.asc sonar-scanner-cli.zip \
    && unzip sonar-scanner-cli.zip \
    && mv sonar-scanner-$SONAR_SCANNER_CLI_VERSION $SONAR_SCANNER_CLI_HOME \
    && chmod +x $SONAR_SCANNER_CLI_HOME/bin/sonar-scanner \
    && rm sonar-scanner-cli.zip* \
    && mkdir -p /usr/src

ENV PATH ${SONAR_SCANNER_CLI_HOME}/bin:$PATH

CMD sonar-scanner -Dsonar.projectBaseDir=/usr/src
