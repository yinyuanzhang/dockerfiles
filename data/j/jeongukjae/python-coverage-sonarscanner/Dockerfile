FROM python:3.6.8-stretch

LABEL maintainer="Ukjae Jeong <jeongukjae@gmail.com>"

RUN pip install coverage
RUN apt-get update && apt-get install -y curl git tmux htop maven sudo

# from https://github.com/newtmitch/docker-sonar-scanner/blob/master/Dockerfile.sonarscanner-3.2.0-full

WORKDIR /root

RUN curl --insecure -o ./sonarscanner.zip -L https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.2.0.1227-linux.zip && \
	unzip sonarscanner.zip && \
	rm sonarscanner.zip && \
	mv sonar-scanner-3.2.0.1227-linux sonar-scanner

ENV PATH $PATH:/root/sonar-scanner/bin
