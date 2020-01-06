FROM centos:7.6.1810

# Java Env Variables
ENV JAVA_VERSION=1.8 \
    JAVA_TARBALL=server-jre-8u66-linux-x64.tar.gz \
    JAVA_7_HOME=/usr/lib/jvm/java-1.7.0-openjdk \
    JAVA_8_HOME=/usr/lib/jvm/java-1.8.0-openjdk \
    JAVA_9_HOME=/usr/lib/jvm/java-9.0.4-openjdk \
    JAVA_11_HOME=/usr/lib/jvm/java-11.0.2-openjdk
    
ENV JAVA_HOME=${JAVA_8_HOME}

# Swarm Env Variables (defaults)
ENV SWARM_MASTER=http://jenkins:8080/jenkins/ \
    SWARM_USER=jenkins \
    SWARM_PASSWORD=jenkins

# Slave Env Variables
ENV SLAVE_NAME="Swarm_Slave" \
    SLAVE_LABELS="java7 java8 java9 java11 sonar katalon" \
    SLAVE_MODE="exclusive" \
    SLAVE_EXECUTORS=1 \
    SLAVE_DESCRIPTION="Core Jenkins Slave"

ENV SONAR_RUNNER_VERSION=2.4
ENV SONAR_RUNNER_HOME=/opt/sonar-runner-${SONAR_RUNNER_VERSION} \
    SONAR_RUNNER_PACKAGE=sonar-runner-dist-${SONAR_RUNNER_VERSION}.zip \
    HOME=${SONAR_RUNNER_HOME}

# https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.0.3.778.zip
ENV SONAR_SCANNER_VERSION=3.0.3.778
ENV SONAR_SCANNER_HOME=/opt/sonar-scanner \
    SONAR_SCANNER_PACKAGE=sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip \
    HOME=${SONAR_SCANNER_HOME}


ENV NPM_VERSION=6.14.2
ENV NPM_URL=https://nodejs.org/dist/v${NPM_VERSION}/node-v${NPM_VERSION}-linux-x64.tar.xz

# Pre-requisites
RUN yum -y install epel-release
RUN yum install -y which \
    git subversion git-svn \
    wget \
    tar \
    openldap-clients \
    openssl \
    unzip bzip2 wget \
    java-1.7.0-openjdk-devel \
    java-1.8.0-openjdk-devel \
    git-core \
    zlib \
    zlib-devel \
    gcc-c++ \
    patch \
    readline \
    readline-devel \
    libyaml-devel \
    libffi-devel \
    openssl-devel \
    make \
    bzip2 \
    autoconf \
    automake \ 
    libtool \ 
    bison \
    curl \ 
    expect \
    devtoolset-3-strace \
    glibc.i686 \
    glibc.i386 \
    gcc-multilib \
    libfreetype.so \
    libfontconfig.so \
    libstdc++.so.6 \
    jq \
    sqlite-devel ; \
    yum clean all
    
RUN rm -rf /var/cache/yum

# Add Tini
ENV TINI_VERSION v0.15.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

# Install Ruby
RUN git clone git://github.com/rbenv/rbenv.git /usr/local/rbenv \
&&  git clone git://github.com/rbenv/ruby-build.git /usr/local/rbenv/plugins/ruby-build \
&&  /usr/local/rbenv/plugins/ruby-build/install.sh
ENV PATH /usr/local/rbenv/bin:$PATH
ENV RBENV_ROOT /usr/local/rbenv

RUN echo 'export RBENV_ROOT=/usr/local/rbenv' >> /etc/profile.d/rbenv.sh \
&&  echo 'export PATH=/usr/local/rbenv/bin:$PATH' >> /etc/profile.d/rbenv.sh \
&&  echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh

RUN echo 'export RBENV_ROOT=/usr/local/rbenv' >> /root/.bashrc \
&&  echo 'export PATH=/usr/local/rbenv/bin:$PATH' >> /root/.bashrc \
&&  echo 'eval "$(rbenv init -)"' >> /root/.bashrc

ENV CONFIGURE_OPTS --disable-install-doc
ENV PATH /usr/local/rbenv/bin:/usr/local/rbenv/shims:$PATH

RUN eval "$(rbenv init -)"; rbenv install 2.4.2 \
&&  eval "$(rbenv init -)"; rbenv global 2.4.2 \
&&  eval "$(rbenv init -)"; gem install bundler

RUN rbenv rehash

# Install Fastlane
RUN gem install fastlane -NV
RUN rbenv rehash

# Install NPM

# RUN yum -y install nodejs npm --enablerepo=epel ; yum clean all
# RUN rm -rf /var/cache/yum
# RUN npm install -g @angular/cli semver yarn ; npm install -g yo --allow-root ; npm cache clean

# ENV PATH "$PATH:/opt/bin/node/bin"

# Install NVM to manage different Node versions
ENV NVM_DIR /usr/local/nvm
ENV NODE_6_VERSION 6.14.3
ENV NODE_10_VERSION 10.15.1

# Install nvm with node and npm
RUN mkdir /usr/local/nvm
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash \
    && . $NVM_DIR/nvm.sh \
    && nvm install $NODE_6_VERSION \
    && nvm alias default $NODE_6_VERSION     \
    && nvm use default \
    && nvm install $NODE_10_VERSION \
    && nvm alias $NODE_10_VERSION 


ENV NODE_PATH $NVM_DIR/versions/node/v$NODE_6_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_6_VERSION/bin:$PATH


# Docker versions Env Variab
# Install Java

#RUN wget --no-check-certificate --directory-prefix=/tmp \
#         --header "Cookie: oraclelicense=accept-securebackup-cookie" \
#           http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.tar.gz 
#RUN           mkdir -p /opt/java && \
#              tar -xzf /tmp/jdk-8u131-linux-x64.tar.gz  -C /opt/java/ && \
#            alternatives --install /usr/bin/java java /opt/java/jdk1.8.0_131mmm/bin/java 100 && \
#                rm -rf /tmp/* && rm -rf /var/log/*

# Install open-jdk 9
RUN wget https://download.java.net/java/GA/jdk9/9.0.4/binaries/openjdk-9.0.4_linux-x64_bin.tar.gz && \
    tar -zxf openjdk-9.0.4_linux-x64_bin.tar.gz && \
    mv jdk-9.0.4 java-9.0.4-openjdk && \
    mv java-9.0.4-openjdk /usr/lib/jvm/ && \
    rm -f openjdk-9.0.4_linux-x64_bin.tar.gz

# Install open-jdk 11
RUN wget https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_linux-x64_bin.tar.gz && \
    tar -zxf openjdk-11.0.2_linux-x64_bin.tar.gz && \
    mv jdk-11.0.2 java-11.0.2-openjdk && \
    mv java-11.0.2-openjdk /usr/lib/jvm/ && \
    rm -f openjdk-11.0.2_linux-x64_bin.tar.gz 
				
# Install maven 3.3.9
RUN wget https://archive.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz && \
    tar -zxf apache-maven-3.3.9-bin.tar.gz && \
    mv apache-maven-3.3.9 /usr/local && \
    rm -f apache-maven-3.3.9-bin.tar.gz && \
    ln -s /usr/local/apache-maven-3.3.9/bin/mvn /usr/bin/mvn
	

# Install maven 3.0.4
RUN wget https://archive.apache.org/dist/maven/maven-3/3.0.4/binaries/apache-maven-3.0.4-bin.tar.gz && \
    tar -zxf apache-maven-3.0.4-bin.tar.gz && \
    mv apache-maven-3.0.4 /usr/local && \
    rm -f apache-maven-3.0.4-bin.tar.gz && \
    ln -s /usr/local/apache-maven-3.0.4/bin/mvn /usr/bin/mvn3.0.4

RUN wget https://archive.apache.org/dist/maven/maven-3/3.5.4/binaries/apache-maven-3.5.4-bin.tar.gz && \
    tar -zxf apache-maven-3.5.4-bin.tar.gz && \
    mv apache-maven-3.5.4 /usr/local && \
    rm -f apache-maven-3.5.4-bin.tar.gz && \
    ln -s /usr/local/apache-maven-3.5.4/bin/mvn /usr/bin/mvn-3.5.4

WORKDIR /opt

# Headless Browser Testing With Chrome Headless
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
RUN yum -y install google-chrome-stable_current_x86_64.rpm ; yum clean all
RUN rm google-chrome-stable_current_x86_64.rpm

RUN yum -y install net-tools ; yum clean all
ADD chrome-headless /usr/bin/chrome-headless
RUN mv /usr/bin/google-chrome /usr/bin/google-chrome.real  \
 && mv /opt/google/chrome/google-chrome /opt/google/chrome/google-chrome.real  \
 && rm /etc/alternatives/google-chrome \
 && ln -s /opt/google/chrome/google-chrome.real /etc/alternatives/google-chrome \
 && ln -s /usr/bin/chrome-headless /usr/bin/google-chrome

RUN yum install -y ipa-gothic-fonts xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-utils xorg-x11-fonts-cyrillic xorg-x11-fonts-Type1 xorg-x11-fonts-misc ; yum clean all

RUN wget http://repo1.maven.org/maven2/org/codehaus/sonar/runner/sonar-runner-dist/${SONAR_RUNNER_VERSION}/${SONAR_RUNNER_PACKAGE} && \
    unzip  sonar-runner-dist-2.4.zip && \
 rm ${SONAR_RUNNER_PACKAGE}

## Install sonar scanner
RUN wget dl.bintray.com/sonarsource/SonarQube/org/sonarsource/scanner/cli/sonar-scanner-cli/${SONAR_SCANNER_VERSION}/${SONAR_SCANNER_PACKAGE} && \
    unzip ${SONAR_SCANNER_PACKAGE} -d /opt && \
    mv /opt/sonar-scanner-${SONAR_SCANNER_VERSION} ${SONAR_SCANNER_HOME} && \
    rm ${SONAR_SCANNER_PACKAGE}
	
## Copy protractor config for selenium tests and dependencies
ADD protractor-selenium.conf.js /opt/protractor-selenium.conf.js
RUN npm install jasmine-spec-reporter ts-node typescript -g   
ENV NODE_PATH=/usr/lib/node_modules

## Install protractor globally and webdrivers for Selenium standalone
ENV CHROME_WEBDRIVER_VERSION=2.33
RUN npm i protractor -g
RUN webdriver-manager update --versions.chrome=${CHROME_WEBDRIVER_VERSION} --ignore_ssl
ENV CHROME_WEBDRIVER=$NODE_PATH/protractor/node_modules/webdriver-manager/selenium/chromedriver_${CHROME_WEBDRIVER_VERSION}
# Make Jenkins a slave by installing swarm-client
RUN curl -s -o /bin/swarm-client.jar -k https://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-client/3.9/swarm-client-3.9.jar

## Install Gradle, Ruby, Fastlane and Android SDK
# Install Gradle
RUN wget https://services.gradle.org/distributions/gradle-4.2.1-bin.zip
RUN mkdir /opt/gradle
RUN unzip -d /opt/gradle gradle-4.2.1-bin.zip
ENV PATH $PATH:/opt/gradle/gradle-4.2.1/bin
ENV GRADLE_OPTS -Dorg.gradle.daemon=true
# Support Gradle
ENV TERM xterm
ENV JAVA_OPTS -Xms256m -Xmx512m -Djdk.http.auth.tunneling.disabledSchemes=""

# Install Android SDK
ENV ANDROID_SDK_URL https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip
ENV ANDROID_HOME /usr/local/android-sdk-linux
ENV ANDROID_SDK /usr/local/android-sdk-linux
RUN wget -O sdk.zip $ANDROID_SDK_URL
RUN unzip -d $ANDROID_HOME sdk.zip
RUN rm sdk.zip
ENV PATH $ANDROID_HOME/tools:$ANDROID_HOME/platform-tools:$PATH

# Install Android SDK components
ADD android-sdk-packages $ANDROID_HOME/android-sdk-packages
RUN yes | $ANDROID_HOME/tools/bin/sdkmanager --licenses
RUN $ANDROID_HOME/tools/bin/sdkmanager --package_file=$ANDROID_HOME/android-sdk-packages
# Remove unneeded modules
RUN $ANDROID_HOME/tools/bin/sdkmanager --uninstall "system-images;andriod-26;google_apis_playstore;x86" "docs"

RUN $ANDROID_HOME/tools/bin/sdkmanager --update

# Install Filebeat
RUN wget https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-6.3.0-linux-x86_64.tar.gz
RUN mkdir /opt/filebeat
RUN tar xvfz filebeat-6.3.0-linux-x86_64.tar.gz -C /opt/filebeat --strip-components=1
RUN rm filebeat-6.3.0-linux-x86_64.tar.gz
COPY resources/filebeat.yml /opt/filebeat/

## Install Katalon 6.2.0 and environment variables
# Install Katalon
RUN wget https://github.com/katalon-studio/katalon-studio/releases/download/v6.2.2/Katalon_Studio_Linux_64-6.2.2.tar.gz
RUN mkdir /opt/katalon
RUN tar xvfz Katalon_Studio_Linux_64-6.2.2.tar.gz -C /opt/katalon --strip-components=1
RUN rm Katalon_Studio_Linux_64-6.2.2.tar.gz
RUN chmod +x /opt/katalon/katalon
# Environment variables for Katalon
ENV KATALON_ROOT_DIR=/opt/katalon
ENV KATALON_INSTALL_DIR_PARENT=/opt
ENV KATALON_INSTALL_DIR=$KATALON_INSTALL_DIR_PARENT/katalonstudio

## Install Chromedriver 75.0.3770.8
# RUN curl -sS -o /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/75.0.3770.8/chromedriver_linux64.zip
# RUN unzip -qq /tmp/chromedriver_linux64.zip -d /opt/katalon/configuration/resources/drivers
# RUN rm /tmp/chromedriver_linux64.zip
# RUN chmod +x /opt/katalon/configuration/resources/drivers/chromedriver_linux64/chromedriver

#Install JMeter5.1.1
ARG JMETER_VERSION=5.1.1
ENV JMETER_HOME /opt/jmeter
ENV	JMETER_BIN	${JMETER_HOME}/bin

# download extract and install jmeter
RUN   mkdir /opt/jmeter \
      && cd /opt/jmeter/ \
      && wget https://archive.apache.org/dist/jmeter/binaries/apache-jmeter-$JMETER_VERSION.tgz \
      && tar -xzf apache-jmeter-$JMETER_VERSION.tgz \
      && rm apache-jmeter-$JMETER_VERSION.tgz
COPY resources/user.properties /opt/jmeter/apache-jmeter-$JMETER_VERSION/bin/

COPY ca/bil-infra-ca.pem /usr/share/pki/ca-trust-source/anchors/bil-infra-ca.crt
COPY ca/is4f-infra-ca.pem /usr/share/pki/ca-trust-source/anchors/is4f-infra-ca.crt
COPY ca/bnet-proxy-app.pem /usr/share/pki/ca-trust-source/anchors/bnet-proxw-app.crt

RUN   mkdir /opt/owasp-dep-check \
    && cd /opt/owasp-dep-check  \
    && wget https://dl.bintray.com/jeremy-long/owasp/dependency-check-5.2.4-release.zip \
    && unzip dependency-check-5.2.4-release.zip \
    && rm dependency-check-5.2.4-release.zip


RUN update-ca-trust

# Start Swarm-Client
CMD ${JAVA_8_HOME}/bin/java ${JAVA_OPTS} -jar /bin/swarm-client.jar \
    -disableClientsUniqueId \
    -deleteExistingClients \
    -disableSslVerification  \
    -executors ${SLAVE_EXECUTORS} \
    -description "${SLAVE_DESCRIPTION}" \
    -master ${SWARM_MASTER}  \
    -name "${SLAVE_NAME}" \
    -labels "${SLAVE_LABELS}" \
    -mode ${SLAVE_MODE} \
    -t java8=${JAVA_8_HOME} \
    -t java7=${JAVA_7_HOME} \
    -t java9=${JAVA_9_HOME} \
    -t java11=${JAVA_11_HOME} \
    -t maven3=/usr/local/apache-maven-3.3.9