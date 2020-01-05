FROM java:jre-alpine

RUN apk add --update python py-pip
RUN pip install --upgrade pip && pip install -U setuptools && pip install -U pylint

ADD https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.2.0.1873.zip ./package.zip

RUN unzip package.zip && mv ./sonar-scanner* ./sonar-scanner

ADD entrypoint.sh .
RUN chmod +x /entrypoint.sh

ENV SONAR_SCANNER_OPTS="-Xmx512m"
ENV SONAR_SOURCES="."

WORKDIR /src
ENTRYPOINT [ "/entrypoint.sh" ]
