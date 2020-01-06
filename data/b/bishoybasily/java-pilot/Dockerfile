FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    software-properties-common \
    git \
    curl \
    maven \
    build-essential \
    python-software-properties \
    debconf-utils \
    python \
    python-pip

RUN add-apt-repository universe

RUN pip install --upgrade pip 
RUN pip install --upgrade awscli
RUN pip install --upgrade awsebcli 

RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
    echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update -y && apt-get install google-cloud-sdk-app-engine-java -y

RUN add-apt-repository -y ppa:openjdk-r/ppa \
    && apt-get update && apt-get install -y \
    openjdk-8-jdk

#COPY pom.xml pom.xml

#RUN mvn clean compile install