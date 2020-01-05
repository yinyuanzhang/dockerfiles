FROM inspire11/expo-deploy-sonar-scanner
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN apt-get update && apt-get -y upgrade && apt-get install -y python-dev jq
RUN apt -y autoremove
RUN npm install -g expo-cli@3.0.10
RUN npm install -g snyk@1.153.0
RUN wget -qO- https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/5.2.4/flyway-commandline-5.2.4-linux-x64.tar.gz | tar xvz
RUN ln -s `pwd`/flyway-5.2.4/flyway /usr/local/bin
RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip install --upgrade awscli==1.16.116 setuptools==41.0.1
