FROM golang:1.11.0-stretch

RUN apt update &&\
    apt install unzip -y &&\
    apt autoremove -y && apt clean && rm -rf /var/lib/apt/lists* /tmp/* /var/tmp/* 

RUN mkdir -p /go/src/github.com/go-swagger/go-swagger &&\
    cd /go/src/github.com/go-swagger/go-swagger &&\
    wget https://github.com/go-swagger/go-swagger/archive/0.16.0.tar.gz &&\
    tar xzf 0.16.0.tar.gz --strip-components 1 &&\
    go install github.com/go-swagger/go-swagger/cmd/swagger &&\
    cd /go/src &&\
    rm -rf *

RUN wget https://github.com/getgauge/gauge/releases/download/v1.0.1/gauge-1.0.1-linux.x86_64.zip &&\
    unzip gauge-1.0.1-linux.x86_64.zip -d /usr/local/bin &&\
    rm -rf gauge-1.0.1-linux.x86_64.zip
    
RUN gauge install screenshot --version 0.0.1 &&\
    gauge install go --version 0.1.2 &&\
    gauge install html-report --version 4.0.5
