FROM openjdk:8-alpine

RUN apk add --no-cache  curl grep sed unzip

WORKDIR /sonar

RUN curl --insecure -o ./sonarscanner.zip -L https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.2.0.1227-linux.zip
RUN unzip sonarscanner.zip
RUN rm sonarscanner.zip
RUN mv sonar-scanner-3.2.0.1227-linux sonar-scanner
RUN apk add --update bash curl nodejs && rm -rf /var/cache/apk/*

ENV SONAR_RUNNER_HOME=/sonar/sonar-scanner
ENV PATH $PATH:/sonar/sonar-scanner/bin
ENV SONAR_SERVER =localhost
ENV SECRET_PASSWORD=undef

COPY sonar-runner.properties ./sonar-scanner/conf/sonar-scanner.properties

RUN sed -i 's/use_embedded_jre=true/use_embedded_jre=false/g' /sonar/sonar-scanner/bin/sonar-scanner

ENV SONAR_SCANNER_OPTS="-Xmx512m"
WORKDIR /work
CMD /sonar/sonar-scanner/bin/sonar-scanner
