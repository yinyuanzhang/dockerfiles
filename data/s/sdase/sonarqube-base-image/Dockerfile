FROM quay.io/sdase/openjdk:8u181-alpine-3.8 as builder

ENV USER worker
ENV HOME /home/$USER
WORKDIR $HOME

ENV VERSION=6.7.6 \
    AUTH_GITHUB_PLUGIN_VERSION=1.3 \
    GITHUB_PLUGIN_VERSION=1.4.2.1027 \
    JAVA_PLUGIN_VERSION=5.9.2.16552 \
    TYPESCRIPT_PLUGIN_VERSION=1.8.0.3332 \
    GO_PLUGIN_VERSION=1.0.0.1404 \
    SVG_BADGES_PLUGIN_VERSION=3.0.1

RUN apk add --no-cache --virtual build-dependencies gnupg \
    && (gpg --batch --keyserver ha.pool.sks-keyservers.net --recv-keys F1182E81C792928921DBCAB4CFCA4A29D26468DE \
	    || gpg --batch --keyserver ipv4.pool.sks-keyservers.net --recv-keys F1182E81C792928921DBCAB4CFCA4A29D26468DE) \
    && curl -o sonarqube.zip -fSL https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-${VERSION}.zip \
    && curl -o sonarqube.zip.asc -fSL https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-${VERSION}.zip.asc \
    && gpg --batch --verify sonarqube.zip.asc sonarqube.zip \
    && unzip sonarqube.zip \
    && mv sonarqube-${VERSION} sonarqube \
    && curl -o sonar-auth-github-plugin-${AUTH_GITHUB_PLUGIN_VERSION}.jar -fSL https://binaries.sonarsource.com/Distribution/sonar-auth-github-plugin/sonar-auth-github-plugin-${AUTH_GITHUB_PLUGIN_VERSION}.jar \
    && curl -o sonar-auth-github-plugin-${AUTH_GITHUB_PLUGIN_VERSION}.jar.asc -fSL https://binaries.sonarsource.com/Distribution/sonar-auth-github-plugin/sonar-auth-github-plugin-${AUTH_GITHUB_PLUGIN_VERSION}.jar.asc \
    && gpg --batch --verify sonar-auth-github-plugin-${AUTH_GITHUB_PLUGIN_VERSION}.jar.asc sonar-auth-github-plugin-${AUTH_GITHUB_PLUGIN_VERSION}.jar \
    && mv sonar-auth-github-plugin-${AUTH_GITHUB_PLUGIN_VERSION}.jar sonarqube/extensions/plugins \
    && curl -o sonar-github-plugin-${GITHUB_PLUGIN_VERSION}.jar -fSL https://binaries.sonarsource.com/Distribution/sonar-github-plugin/sonar-github-plugin-${GITHUB_PLUGIN_VERSION}.jar \
    && curl -o sonar-github-plugin-${GITHUB_PLUGIN_VERSION}.jar.asc -fSL https://binaries.sonarsource.com/Distribution/sonar-github-plugin/sonar-github-plugin-${GITHUB_PLUGIN_VERSION}.jar.asc \
    && gpg --batch --verify sonar-github-plugin-${GITHUB_PLUGIN_VERSION}.jar.asc sonar-github-plugin-${GITHUB_PLUGIN_VERSION}.jar \
    && mv sonar-github-plugin-${GITHUB_PLUGIN_VERSION}.jar sonarqube/extensions/plugins \
    && curl -o sonar-java-plugin-${JAVA_PLUGIN_VERSION}.jar -fSL https://binaries.sonarsource.com/Distribution/sonar-java-plugin/sonar-java-plugin-${JAVA_PLUGIN_VERSION}.jar \
    && curl -o sonar-java-plugin-${JAVA_PLUGIN_VERSION}.jar.asc -fSL https://binaries.sonarsource.com/Distribution/sonar-java-plugin/sonar-java-plugin-${JAVA_PLUGIN_VERSION}.jar.asc \
    && gpg --batch --verify sonar-java-plugin-${JAVA_PLUGIN_VERSION}.jar.asc sonar-java-plugin-${JAVA_PLUGIN_VERSION}.jar \
    && mv sonar-java-plugin-${JAVA_PLUGIN_VERSION}.jar sonarqube/extensions/plugins \
    && curl -o sonar-typescript-plugin-${TYPESCRIPT_PLUGIN_VERSION}.jar -fSL https://binaries.sonarsource.com/Distribution/sonar-typescript-plugin/sonar-typescript-plugin-${TYPESCRIPT_PLUGIN_VERSION}.jar \
    && curl -o sonar-typescript-plugin-${TYPESCRIPT_PLUGIN_VERSION}.jar.asc -fSL https://binaries.sonarsource.com/Distribution/sonar-typescript-plugin/sonar-typescript-plugin-${TYPESCRIPT_PLUGIN_VERSION}.jar.asc \
    && gpg --batch --verify sonar-typescript-plugin-${TYPESCRIPT_PLUGIN_VERSION}.jar.asc sonar-typescript-plugin-${TYPESCRIPT_PLUGIN_VERSION}.jar \
    && mv sonar-typescript-plugin-${TYPESCRIPT_PLUGIN_VERSION}.jar sonarqube/extensions/plugins \
    && curl -o sonar-go-plugin-${GO_PLUGIN_VERSION}.jar -fSL https://binaries.sonarsource.com/Distribution/sonar-go-plugin/sonar-go-plugin-${GO_PLUGIN_VERSION}.jar \
    && curl -o sonar-go-plugin-${GO_PLUGIN_VERSION}.jar.asc -fSL https://binaries.sonarsource.com/Distribution/sonar-go-plugin/sonar-go-plugin-${GO_PLUGIN_VERSION}.jar.asc \
    && gpg --batch --verify sonar-go-plugin-${GO_PLUGIN_VERSION}.jar.asc sonar-go-plugin-${GO_PLUGIN_VERSION}.jar \
    && mv sonar-go-plugin-${GO_PLUGIN_VERSION}.jar sonarqube/extensions/plugins \
    && curl -o qualinsight-sonarqube-badges-${SVG_BADGES_PLUGIN_VERSION}.jar -fSL https://github.com/QualInsight/qualinsight-plugins-sonarqube-badges/releases/download/qualinsight-plugins-sonarqube-badges-${SVG_BADGES_PLUGIN_VERSION}/qualinsight-sonarqube-badges-${SVG_BADGES_PLUGIN_VERSION}.jar \
    && mv qualinsight-sonarqube-badges-${SVG_BADGES_PLUGIN_VERSION}.jar sonarqube/extensions/plugins \
    && chown -R worker:worker sonarqube \
    && rm -f sonarqube.zip* \
    && rm -f .jar* \
    && rm -rf sonarqube/bin/*

FROM quay.io/sdase/openjdk:8u181-alpine-3.8

ENV USER worker
ENV HOME /home/$USER
WORKDIR $HOME/sonarqube

ENV VERSION=6.7.6 \
    AUTH_GITHUB_PLUGIN_VERSION=1.3 \
    GITHUB_PLUGIN_VERSION=1.4.2.1027 \
    JAVA_PLUGIN_VERSION=5.9.2.16552 \
    TYPESCRIPT_PLUGIN_VERSION=1.8.0.3332 \
    GO_PLUGIN_VERSION=1.0.0.1404 \
    SVG_BADGES_PLUGIN_VERSION=3.0.1

RUN apk add --no-cache bash ttf-dejavu

COPY --chown=1000:1000 --from=builder $HOME/sonarqube/ ./
COPY --chown=1000:1000 run.sh ./

USER $USER
EXPOSE 9000

ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]
CMD ["./run.sh"]
