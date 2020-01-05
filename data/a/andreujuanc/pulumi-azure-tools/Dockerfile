FROM ubuntu:bionic

RUN apt-get update
RUN apt-get install -my curl
RUN apt-get install -my gnupg

WORKDIR /azure

#AZURE
RUN echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ bionic main" | \
    tee /etc/apt/sources.list.d/azure-cli.list
RUN curl -L https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN apt-get install apt-transport-https
RUN apt-get update && apt-get install azure-cli

#KUBECTL
RUN az acs kubernetes install-cli

#PULUMI 
RUN curl -fsSL https://get.pulumi.com/ | sh
ENV PATH="/root/.pulumi/bin:${PATH}"