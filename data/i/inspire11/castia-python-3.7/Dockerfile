FROM olivierhervieu/amazonlinux-python36-onbuild
RUN yum -y upgrade
RUN curl -sL https://rpm.nodesource.com/setup_10.x | bash -
RUN yum install -y gcc-c++ nodejs unixODBC-devel
RUN yum -y install jq-1.5 git-2.17.2 libtool-ltdl-devel-2.4.2 libxml2-devel-2.9.1 libxslt-devel-1.1.28 mariadb-5.5.60 pkgconfig-0.27.1 python3-3.7.1 tar-1.26 unzip-6.0 wget-1.14 xmlsec1-devel-1.2.20 xmlsec1-openssl-devel-1.2.20 which-2.20 java-1.8.0-openjdk-devel-1.8.0.201.b09
RUN wget -qO- https://repo1.maven.org/maven2/org/flywaydb/flyway-commandline/5.2.4/flyway-commandline-5.2.4-linux-x64.tar.gz | tar xvz && ln -s `pwd`/flyway-5.2.4/flyway /usr/local/bin
RUN pip3 install --upgrade setuptools==41.0.1
RUN pip3 install awscli==1.16.149
RUN npm install -g snyk@1.153.0
RUN wget -O sonar-scanner.zip --no-verbose https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.3.0.1492.zip
RUN unzip sonar-scanner.zip || true
RUN mv sonar-scanner-3.3.0.1492 ~/sonar-scanner
RUN ln -s ~/sonar-scanner/bin/sonar-scanner /usr/bin/sonar-scanner
RUN rm sonar-scanner.zip
