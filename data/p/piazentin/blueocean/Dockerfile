FROM jenkins/jenkins:lts

USER root 
RUN apt-get update && \
    apt-get install -y \
        apt-transport-https \
        ca-certificates \
        software-properties-common \
        sudo && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
    add-apt-repository \
        "deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial stable" && \
    apt-get update && \
    apt-get install -y docker-ce && \
    rm -rf /var/lib/apt/lists/*

# install all default plugins
RUN /usr/local/bin/install-plugins.sh \
        blueocean \
        ant \
        build-timeout \
        email-ext \
        gradle \
        ldap \
        matrix-auth \
        antisamy-markup-formatter \
        pam-auth \
        pipeline-github-lib \
        ssh-slaves \
        timestamper \
        ws-cleanup \
        amazon-ecr \
        ssh-agent \
        pipeline-aws \
        sonar \
        bitbucket-build-status-notifier \
        cucumber-reports
