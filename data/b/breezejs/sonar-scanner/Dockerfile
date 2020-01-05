FROM circleci/node:10.15

RUN mkdir -p /var/opt

RUN sudo wget -q https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.3.0.1492-linux.zip

RUN sudo unzip sonar-scanner-cli-3.3.0.1492-linux.zip

RUN sudo rm sonar-scanner-cli-3.3.0.1492-linux.zip

RUN sudo mv sonar-scanner-3.3.0.1492-linux /var/opt

ENV PATH "$PATH:/var/opt/sonar-scanner-3.3.0.1492-linux/bin"
