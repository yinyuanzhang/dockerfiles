FROM node:10.15.3

RUN npm i -g bower eslint

RUN curl --insecure -o ./sonarscanner.zip -L https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.0.0.1744-linux.zip && \
    unzip ./sonarscanner.zip && \
    rm ./sonarscanner.zip && \
    mv ./sonar-scanner-4.0.0.1744-linux /usr/lib/sonar-scanner && \
    ln -s /usr/lib/sonar-scanner/bin/sonar-scanner /usr/local/bin/sonar-scanner
