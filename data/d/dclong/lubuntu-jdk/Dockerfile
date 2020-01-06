FROM dclong/lubuntu

RUN add-apt-repository ppa:cwchien/gradle 

RUN apt-get update -y \
    && apt-get install -y openjdk-8-jdk maven gradle \
    && apt-get autoremove \
    && apt-get autoclean
