FROM circleci/python:3.6
MAINTAINER Paul JEGOUIC <paul.jegouic@ifsalpha.com>

RUN sudo pip install --upgrade pip

##############
#   INIT     #
##############
RUN sudo apt-get update
RUN sudo apt-get install apt-transport-https lsb-release ca-certificates
RUN sudo pip install boto3 coverage mock requests cfn-lint urllib3 warrant python-jose flask Flask-Cors python-jose
RUN sudo apt-get update && sudo apt-get install -y r-base r-base-core r-base-dev r-base-core-dbg

##############
#    IONIC   #
##############
RUN curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -
RUN sudo apt-get install -y nodejs pwgen

###############
#    AWSCLI   #
###############
RUN sudo apt-get install -qq -y python-pip libpython-dev
RUN sudo pip install -q awscli --upgrade 
RUN aws configure set region eu-central-1

##############
#    MICLI   #
##############
COPY scripts/myimpact.sh /usr/local/bin/myimpact
RUN sudo chmod 777 /usr/local/bin/myimpact
COPY scripts/process.py /usr/local/bin/process.py
RUN sudo chmod 777 /usr/local/bin/process.py
COPY scripts/alpha.sh /usr/local/bin/alpha
RUN sudo chmod 777 /usr/local/bin/alpha
COPY scripts/export.py /usr/local/bin/export.py
RUN sudo chmod 777 /usr/local/bin/export.py

#######################
#    MAKE IT FUN      #
#######################

RUN sudo sh -c "curl https://raw.githubusercontent.com/mrowa44/emojify/master/emojify -o /usr/local/bin/emojify && chmod +x /usr/local/bin/emojify"

##########################
#    SONARQUBE PART      #
##########################

# INSTALL SONARQUBE SCANNER

RUN sudo wget https://dl.bintray.com/sonarsource/SonarQube/org/sonarsource/scanner/cli/sonar-scanner-cli/3.2.0.1227/sonar-scanner-cli-3.2.0.1227-linux.zip 
RUN sudo mkdir sonar-scanner && sudo unzip sonar-scanner-cli-3.2.0.1227-linux.zip -d sonar-scanner/
COPY sonar-scanner.properties sonar-scanner/sonar-scanner-3.2.0.1227-linux/conf/sonar-scanner.properties

# INSTALL JVM

RUN sudo apt-get install default-jre
RUN sudo apt-get install maven
ENV PATH "$PATH:/sonar-scanner/sonar-scanner-3.2.0.1227-linux/bin"

##########################
#    CFN_NAG PART        #
##########################

run sudo apt-get install ruby2.3