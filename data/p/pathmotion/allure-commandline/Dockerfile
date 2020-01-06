FROM ubuntu:trusty

RUN apt-get update

RUN apt-get install -y software-properties-common \
    && add-apt-repository ppa:openjdk-r/ppa \
    && apt-add-repository ppa:qameta/allure \
    && apt-get update \
    && apt-get install -y openjdk-8-jre allure \
    && rm -rf /var/lib/apt/lists/*

CMD allure help