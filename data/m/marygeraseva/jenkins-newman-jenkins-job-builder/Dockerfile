FROM jenkins/jenkins
# drop back to the root
USER root
# install
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash
RUN apt-get -y install nodejs
RUN npm install -g newman
RUN apt-get install python3-pip -y
RUN pip3 install jenkins-job-builder
RUN apt-get -y install vim
# drop back to the regular jenkins user
USER jenkins
