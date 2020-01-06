FROM moonshotinternet/ci-back:latest

LABEL vendor=Moonshot-Internet
LABEL com.moonshot.name=ci-serverless
LABEL com.moonshot.version=1.0.0

USER root
RUN userdel ciuser 
RUN groupadd --gid 1000 node \
  && useradd --uid 1000 --gid node --shell /bin/bash --create-home node

RUN apt-get update && apt-get install -y gnupg-agent && curl -sL https://deb.nodesource.com/setup_10.x | bash - && apt-get install -y nodejs
RUN curl https://www.npmjs.com/install.sh | sh

RUN npm install -g --unsafe-perm serverless dynalite
#RUN npm install -g dynalite

# due to node installing python2, ansible switch back to /usr/bin/python which point to py2
# this line force ansible to switch back to python3 for local task
RUN echo "\n\n[local:vars]\nansible_python_interpreter=/usr/local/bin/python3" >> /etc/ansible/hosts

USER node
