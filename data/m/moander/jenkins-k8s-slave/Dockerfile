FROM jenkins/jnlp-slave:3.29-1

USER root

# Install docker
RUN apt-get update \
    && apt-get install -y nano git apt-transport-https ca-certificates curl make software-properties-common gcc g++ make \
    && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - \
    && apt-key fingerprint 0EBFCD88 \
    && add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" \
    && apt-get update \
    && apt-get install -y docker-ce=5:18.09.6~3-0~debian-stretch \
    && rm -r /var/lib/apt/lists/* 

# Install nodejs and yarn
RUN curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && curl -sS https://deb.nodesource.com/setup_10.x | bash \
    && apt-get -y install nodejs yarn  \
    && rm -r /var/lib/apt/lists/* 

# Install kubectl
RUN curl -sSLo /bin/kubectl https://storage.googleapis.com/kubernetes-release/release/v1.14.0/bin/linux/amd64/kubectl && chmod a+x /bin/kubectl

USER jenkins
