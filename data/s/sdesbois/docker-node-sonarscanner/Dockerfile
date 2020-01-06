FROM node:10.16.0-alpine

ADD "https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.3.0.1492.zip" /

RUN apk add --no-cache unzip openjdk8-jre \
    && unzip sonar-scanner-cli-3.3.0.1492.zip \
	&& ln -s /sonar-scanner-3.3.0.1492 /usr/bin/sonar-scanner \
    && rm -f sonar-scanner-cli-*.zip
  
ENV PATH $PATH:/sonar-scanner/bin:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin
