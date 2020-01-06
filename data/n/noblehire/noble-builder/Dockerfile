FROM adoptopenjdk/openjdk11:latest

# Install maven 3.6.1
RUN apt-get -qqy update && \
  apt-get -y install wget && \
  rm -rf /var/lib/apt/lists/*;
RUN wget -q https://www-us.apache.org/dist/maven/maven-3/3.6.1/binaries/apache-maven-3.6.1-bin.tar.gz -P /tmp; \
  tar xf /tmp/apache-maven-*.tar.gz -C /opt; \
  ln -s /opt/apache-maven-3.6.1 /opt/maven;
ENV M2_HOME=/opt/maven \
  MAVEN_HOME=/opt/maven
ENV PATH=$M2_HOME/bin:$PATH

# Install Google Cloud SDK (based on https://hub.docker.com/r/google/cloud-sdk/dockerfile)
ARG CLOUD_SDK_VERSION=232.0.0
ENV CLOUD_SDK_VERSION=$CLOUD_SDK_VERSION
RUN apt-get -qqy update && \
  apt-get install -y python-pip libpq-dev python-dev && \
  rm -rf /var/lib/apt/lists/*;
RUN python -m pip install --upgrade pip setuptools wheel
RUN apt-get -qqy update && apt-get install -y \
    curl \
    apt-transport-https \
    lsb-release \
  && easy_install -U pip && \
  pip install -U crcmod   && \
  export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
  echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" > /etc/apt/sources.list.d/google-cloud-sdk.list && \
  curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
  apt-get update && \
  apt-get install -y google-cloud-sdk=${CLOUD_SDK_VERSION}-0 \
    google-cloud-sdk-app-engine-java=${CLOUD_SDK_VERSION}-0 && \
  gcloud config set core/disable_usage_reporting true && \
  gcloud config set component_manager/disable_update_check true && \
  rm -rf /var/lib/apt/lists/*;
VOLUME ["/root/.config"]

# Install Node.js:
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - \
  && apt-get install -y nodejs

# Install Newman:
RUN npm install -g newman

# Install Mysql clients:
RUN apt-get -qqy update && \
  apt-get install -y mysql-client && \
  rm -rf /var/lib/apt/lists/*;

# Install rsync utility:
RUN apt-get -qqy update && \
  apt-get install -y rsync && \
  rm -rf /var/lib/apt/lists/*;

# Install Docker CE:
RUN apt-get -qqy update && \
  apt-get install -y apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common && \ 
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
  add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable" && \ 
  apt-get -qqy update && \
  apt-get install -y docker-ce docker-ce-cli containerd.io && \
  rm -rf /var/lib/apt/lists/*;

# Install docker-compose:
RUN curl -L \
  "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" \
  -o /usr/local/bin/docker-compose && \
  chmod +x /usr/local/bin/docker-compose

# Install SSH server:
RUN apt-get -qqy update && \
  apt-get install -y openssh-server && \
  rm -rf /var/lib/apt/lists/*;

# Setup authorised keys:
RUN mkdir /root/.ssh
COPY authorized_keys /root/.ssh/authorized_keys

# CMD ["java", "-version"]
# CMD ["printenv"]
# CMD ["ls", "-al", "/opt/maven"]
# CMD ["mvn", "--version"]
# CMD ["gcloud", "--version"]
# CMD ["node", "--version"]
# CMD ["npm", "--version"]
# CMD ["newman", "--version"]
# CMD ["mysqldump", "--version"]
# CMD ["rsync", "--version"]
# CMD ["docker", "--version"]
# CMD ["docker-compose", "--version"]

RUN mkdir /var/run/sshd
# RUN echo 'root:h@ck3r5un173!' | chpasswd
# RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 2222

ENTRYPOINT service ssh restart && bash
