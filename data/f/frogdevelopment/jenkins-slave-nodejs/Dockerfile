FROM jenkins/slave

USER root

RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - \
     && apt-get install -y \
            nodejs \
            apt-transport-https \
            ca-certificates \
            curl \
            gnupg2 \
            software-properties-common \
     && curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - \
     && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" \
     && apt-get update \
     && apt-get install -y \
            docker-ce \
            docker-ce-cli \
            containerd.io \
     && usermod -a -G docker jenkins

#ENV NPM_CONFIG_PREFIX=/home/node/.npm-global
#ENV PATH=$PATH:/home/node/.npm-global/bin

USER jenkins
