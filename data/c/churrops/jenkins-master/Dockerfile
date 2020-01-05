ARG image_name=jenkins/jenkins:2.141-alpine

FROM $image_name

LABEL maintainer="Rodrigo Floriano de Souza" 

# $(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)
ENV kubectl_version v1.11.2

# Instalacao dos plugins
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

USER root

# Instalacao do Docker e do Kubectl
ADD https://storage.googleapis.com/kubernetes-release/release/$kubectl_version/bin/linux/amd64/kubectl /usr/local/bin/kubectl

ADD https://get.docker.com/builds/Linux/x86_64/docker-latest.tgz /tmp

RUN tar -xvzf /tmp/docker-latest.tgz && \
    mv docker/* /usr/bin/ && \
    chmod +x /usr/bin/docker && \
    rm -f /tmp/docker-latest.tgz \
    chmod +x /usr/local/bin/kubectl

RUN apk --no-cache add tzdata shadow && \
    addgroup $USER docker && \
    usermod -aG docker jenkins
