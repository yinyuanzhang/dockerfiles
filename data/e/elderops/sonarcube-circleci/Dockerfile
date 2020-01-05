FROM openjdk:8-jdk-alpine
LABEL maintainer="matthew.ridehalgh@elder-studios.co.uk"
ENV SONAR_SCANNER_VERSION 3.0.3.778
RUN addgroup -S circleci && adduser -S circleci -G circleci \
  &&  apk add --no-cache wget nodejs bash git openssh \
  &&  wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip \
  &&  unzip sonar-scanner-cli-${SONAR_SCANNER_VERSION} \
  &&  cd /usr/bin && ln -s /sonar-scanner-${SONAR_SCANNER_VERSION}/bin/sonar-scanner sonar-scanner \
  &&  apk del wget
USER circleci
COPY --chown=circleci:circleci sonar.sh /usr/bin