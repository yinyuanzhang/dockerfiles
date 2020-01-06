FROM golang:1-stretch as kops-builder

RUN go get k8s.io/kops
WORKDIR /go/src/k8s.io/kops
RUN make

FROM korekontrol/docker-jnlp-slave-docker

USER root

RUN curl -sL "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-linux-x86_64" -o /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose
RUN pip install awscli
RUN apt-get update \
  && apt-get install -y apt-transport-https
RUN curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg \
  | apt-key add -
RUN echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" \
  | tee -a /etc/apt/sources.list.d/kubernetes.list
RUN apt-get update \
  && apt-get install -y kubectl gettext-base

COPY --from=kops-builder /go/bin/kops /usr/bin/

ADD start.sh /

USER jenkins
