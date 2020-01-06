# docker build --rm -f Dockerfile -t netzon-docker-phusion-dotnet-core:latest .
# Use phusion/baseimage as base image. To make your builds reproducible, make
# sure you lock down to a specific version, not to `latest`!
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for
# a list of version numbers.
FROM phusion/baseimage:0.10.1

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Install Base Dependencies
RUN apt-get update && apt-get install -y wget \
    && wget -q https://packages.microsoft.com/config/ubuntu/16.04/packages-microsoft-prod.deb \
    && dpkg -i packages-microsoft-prod.deb \
    && apt-get install -y apt-transport-https

# Install all other apps
RUN AZ_REPO=$(lsb_release -cs) \
    && echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" >> /etc/apt/sources.list \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367 \
    && curl -sL https://deb.nodesource.com/setup_8.x | bash - \
    && echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" | tee /etc/apt/sources.list.d/azure-cli.list \
    && curl -L https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb \
    && dpkg -i erlang-solutions_1.0_all.deb \
    && wget -O - 'https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc' | apt-key add - \
    && echo "deb https://dl.bintray.com/rabbitmq/debian xenial main" | tee \
    && apt-get update \
    && apt-get -y install python erlang nodejs dotnet-sdk-2.2 azure-cli ansible postgresql postgresql-contrib rabbitmq-server \
    && npm install -g @angular/cli@1.6.5 \
    && easy_install pip && pip install pywinrm

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
ENTRYPOINT service postgresql start && /bin/bash