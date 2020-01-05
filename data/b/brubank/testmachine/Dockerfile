FROM golang:1.10.4-stretch
RUN apt-get update && apt-get install -y \
        default-jre\
        python3-pip
RUN pip3 install requests==2.13.0 Faker==0.7.17 nose==1.3.7 psycopg2==2.7.3.1 pytoml==0.1.14 pika==0.11.0 dpath==1.4.0 termcolor==1.1.0  xmltodict==0.11.0 concurrencytest==0.1.2
RUN curl -fsSL -o /usr/local/bin/dep https://github.com/golang/dep/releases/download/v0.4.1/dep-linux-amd64 && chmod +x /usr/local/bin/dep
RUN go get -u golang.org/x/lint/golint
RUN go get github.com/securego/gosec/cmd/gosec/...
RUN go get github.com/mjibson/esc
RUN go get github.com/jteeuwen/go-bindata/...
