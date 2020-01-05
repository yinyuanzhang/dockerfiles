FROM ubuntu:18.04
MAINTAINER developers@khipu.com

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install openjdk-8-jdk -y && \
    apt-get install maven -y && \
    apt-get install git -y && \
    apt-get install gnupg -y && \
    apt-get install jq -y && \
    apt-get install python-pip -y && \
    apt-get install ruby -y && \
    apt-get install apt-transport-https -y && \
    apt-get install wget -y && \
    apt-get install curl -y && \
    apt-get install docker.io -y && \
    apt-get install zip -y && \
    apt-get install unzip -y && \
    pip install ytools

RUN curl -fsSL https://clis.cloud.ibm.com/install/linux | sh \
    && ibmcloud plugin install container-registry -r Bluemix

RUN curl -fsSL "https://get.sdkman.io" | bash

RUN wget -q https://packages.microsoft.com/config/ubuntu/18.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb && \
    dpkg -i packages-microsoft-prod.deb && \
    apt-get install software-properties-common -y && \
    add-apt-repository universe && \
    apt-get install apt-transport-https && \
    apt-get update && \
    apt-get install dotnet-sdk-2.2 -y

RUN apt-get install gnupg -y && \
    apt-get install ca-certificates -y && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
    echo "deb https://download.mono-project.com/repo/ubuntu stable-bionic main" | tee /etc/apt/sources.list.d/mono-official-stable.list && \
    apt-get update && \
    apt-get install mono-devel -y

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["/bin/true"]
