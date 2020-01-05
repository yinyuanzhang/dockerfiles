# docker build --build-arg="SSH_PRIVATE_KEY=`cat ~/.ssh/id_rsa`" .

# STAGE0
FROM golang:latest as builder

LABEL Christian Sakshaug <christian@dx.no>

COPY . /ci/

WORKDIR /ci

RUN mkdir -p /go/src/github.com/dialogexe
RUN make
RUN mv bin outputs
RUN mkdir bin
RUN mv outputs/ciset-linux-amd64 /ci/bin/ciset
RUN mv .docker-cmd.sh /ci/bin/execute.sh
RUN mkdir /o
RUN cp -R /ci/bin /o/bin
RUN cp -R tools/* /o

# STAGE1
FROM ubuntu:latest

RUN apt-get update && apt-get install -y openssh-client bash git curl wget vim build-essential software-properties-common && curl --silent --location https://raw.githubusercontent.com/nodesource/distributions/master/deb/setup_10.x | bash && apt-get install nodejs -y && add-apt-repository ppa:gophers/archive -y && apt-get update && apt-get install -y golang-1.10-go && ln -s /usr/lib/go-1.10/bin/go /usr/local/bin/go && ln -s /usr/lib/go-1.10/bin/gofmt /usr/local/bin/gofmt

# COPY FROM STAGE0 SO WE DONT TAKE WITH SECRETS
COPY --from=builder /o/. /ci

RUN chmod +x /ci/bin/* /ci/scripts/*.sh

WORKDIR /ci/bin

CMD ["/ci/bin/execute.sh"]
