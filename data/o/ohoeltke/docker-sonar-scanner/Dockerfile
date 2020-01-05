
FROM java:7

RUN apt-get update
RUN apt-get install -y curl git tmux htop maven

# Don't need these right now. Java is covered in the FROM statement above,
# and build-essential might be overkill for now.
# RUN sudo apt-get install -y openjdk-7-jdk
# RUN sudo apt-get install -y build-essential

# Set timezone to CST
ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /root

RUN curl --insecure -OL https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.0.3.778.zip
RUN unzip sonar-scanner-cli-3.0.3.778.zip
RUN rm sonar-scanner-cli-3.0.3.778.zip

ENV SONAR_RUNNER_HOME=/root/sonar-scanner-3.0.3.778
ENV PATH $PATH:/root/sonar-scanner-3.0.3.778/bin

#COPY sonar-runner.properties ./sonar-scanner-3.0.3.778/conf/sonar-runner.properties

# Use bash if you want to run the environment from inside the shell, otherwise use the command that actually runs the underlying stuff
#CMD /bin/bash
CMD sonar-runner -Dsonar.projectBaseDir=./src
